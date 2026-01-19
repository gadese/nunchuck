"""Plan execution helpers.

This module is intentionally deterministic:
- reads/writes YAML frontmatter for active plan tasks
- validates schemas and invariants (including exactly one in_progress unless terminal)
- archives the active plan once terminal
"""

from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft7Validator, FormatChecker


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for parent in [current, *current.parents]:
        if (parent / "nunchuck.toml").exists() or (parent / ".git").exists():
            return parent
    return current


REPO_ROOT = find_repo_root(Path(__file__).resolve())

PLAN_DIR = REPO_ROOT / ".plan"
ACTIVE_INTENT_PATH = PLAN_DIR / "active.yaml"
ACTIVE_DIR = PLAN_DIR / "active"
ARCHIVE_DIR = PLAN_DIR / "archive"

SKILL_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = SKILL_DIR / "assets"
ROOT_SCHEMA_PATH = ASSETS_DIR / "plan-root-schema.json"
SUBPLAN_SCHEMA_PATH = ASSETS_DIR / "plan-subplan-schema.json"
TASK_SCHEMA_PATH = ASSETS_DIR / "plan-task-schema.json"
RECEIPT_SCHEMA_PATH = ASSETS_DIR / "plan-archive-receipt-schema.json"

ROMAN_NUMERALS = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]
TERMINAL_TASK_STATUSES = {"complete", "deferred"}


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def to_rfc3339(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_plan_dir() -> None:
    PLAN_DIR.mkdir(exist_ok=True)


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _schema_errors(schema: dict[str, Any], instance: dict[str, Any]) -> list[str]:
    validator = Draft7Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    formatted: list[str] = []
    for err in errors:
        path = ".".join(str(p) for p in err.path) or "(root)"
        formatted.append(f"{path}: {err.message}")
    return formatted


@dataclass(frozen=True)
class FrontmatterParseResult:
    frontmatter: dict[str, Any] | None
    body: str
    errors: list[str]


def parse_frontmatter_strict(content: str) -> tuple[dict[str, Any], str]:
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing YAML frontmatter (expected leading '---' line)")

    end_idx: int | None = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        raise ValueError("unterminated YAML frontmatter (missing closing '---' line)")

    fm_text = "".join(lines[1:end_idx])
    body = "".join(lines[end_idx + 1 :]).lstrip("\n")

    try:
        fm = yaml.safe_load(fm_text)
    except yaml.YAMLError as e:  # pragma: no cover
        raise ValueError(f"invalid YAML frontmatter: {e}") from e

    if not isinstance(fm, dict):
        raise ValueError("frontmatter must be a YAML mapping/object")

    return fm, body


def read_frontmatter(path: Path) -> FrontmatterParseResult:
    if not path.exists():
        return FrontmatterParseResult(frontmatter=None, body="", errors=["file does not exist"])
    try:
        fm, body = parse_frontmatter_strict(path.read_text(encoding="utf-8"))
        return FrontmatterParseResult(frontmatter=fm, body=body, errors=[])
    except ValueError as e:
        return FrontmatterParseResult(frontmatter=None, body="", errors=[str(e)])


def _dump_frontmatter(frontmatter: dict[str, Any]) -> str:
    return yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).rstrip() + "\n"


def _write_markdown_with_frontmatter(path: Path, frontmatter: dict[str, Any], body: str) -> None:
    content = "---\n" + _dump_frontmatter(frontmatter) + "---\n\n" + body.lstrip("\n")
    path.write_text(content, encoding="utf-8")


def validate_root_frontmatter(frontmatter: dict[str, Any]) -> list[str]:
    if not ROOT_SCHEMA_PATH.exists():
        return [f"missing schema: {ROOT_SCHEMA_PATH}"]
    return _schema_errors(_load_json(ROOT_SCHEMA_PATH), frontmatter)


def validate_subplan_frontmatter(frontmatter: dict[str, Any]) -> list[str]:
    if not SUBPLAN_SCHEMA_PATH.exists():
        return [f"missing schema: {SUBPLAN_SCHEMA_PATH}"]
    return _schema_errors(_load_json(SUBPLAN_SCHEMA_PATH), frontmatter)


def validate_task_frontmatter(frontmatter: dict[str, Any]) -> list[str]:
    if not TASK_SCHEMA_PATH.exists():
        return [f"missing schema: {TASK_SCHEMA_PATH}"]
    return _schema_errors(_load_json(TASK_SCHEMA_PATH), frontmatter)


def _task_paths() -> list[Path]:
    if not ACTIVE_DIR.exists():
        return []
    paths: list[Path] = []
    for letter_dir in sorted([p for p in ACTIVE_DIR.iterdir() if p.is_dir() and len(p.name) == 1]):
        for md in sorted(letter_dir.glob("*.md")):
            if md.stem.lower() in ("index",):
                continue
            if md.suffix.lower() != ".md":
                continue
            roman = md.stem.lower()
            if roman in ROMAN_NUMERALS:
                paths.append(md)
    return paths


def list_tasks() -> list[tuple[Path, dict[str, Any]]]:
    tasks: list[tuple[Path, dict[str, Any]]] = []
    for p in _task_paths():
        res = read_frontmatter(p)
        if res.frontmatter is not None:
            tasks.append((p, res.frontmatter))
    return tasks


def validate_active_plan() -> list[str]:
    errors: list[str] = []

    root_path = ACTIVE_DIR / "plan.md"
    if not root_path.exists():
        return [f"missing active plan root: {root_path}"]

    root = read_frontmatter(root_path)
    if root.errors or root.frontmatter is None:
        return [f"{root_path}: " + "; ".join(root.errors or ["invalid frontmatter"])]

    errors.extend([f"{root_path}: {e}" for e in validate_root_frontmatter(root.frontmatter)])

    # Validate subplan index files (schema + linkage)
    for letter_dir in sorted([p for p in ACTIVE_DIR.iterdir() if p.is_dir() and len(p.name) == 1]):
        idx = letter_dir / "index.md"
        idx_res = read_frontmatter(idx)
        if idx_res.errors or idx_res.frontmatter is None:
            errors.append(f"{idx}: " + "; ".join(idx_res.errors or ["invalid frontmatter"]))
            continue
        errors.extend([f"{idx}: {e}" for e in validate_subplan_frontmatter(idx_res.frontmatter)])
        if idx_res.frontmatter.get("subplan") != letter_dir.name:
            errors.append(f"{idx}: subplan must be '{letter_dir.name}'")

    tasks = list_tasks()
    in_progress = [t for t in tasks if t[1].get("status") == "in_progress"]

    if len(in_progress) > 1:
        errors.append(f"expected at most 1 in_progress task, found {len(in_progress)}")

    for path, fm in tasks:
        errors.extend([f"{path}: {e}" for e in validate_task_frontmatter(fm)])

        # Path ↔ frontmatter linkage checks
        letter = path.parent.name
        roman = path.stem.lower()
        if fm.get("subplan") != letter:
            errors.append(f"{path}: subplan must be '{letter}'")
        if fm.get("task") != roman:
            errors.append(f"{path}: task must be '{roman}'")

    return errors


def _ordered_task_paths() -> list[Path]:
    # Deterministic ordering: subplan a→z, tasks i→x.
    def sort_key(p: Path) -> tuple[str, int]:
        letter = p.parent.name
        roman = p.stem.lower()
        idx = ROMAN_NUMERALS.index(roman) if roman in ROMAN_NUMERALS else 999
        return (letter, idx)

    return sorted(_task_paths(), key=sort_key)


def _update_frontmatter_status(path: Path, *, status: str, extra: dict[str, Any] | None = None) -> None:
    res = read_frontmatter(path)
    if res.frontmatter is None:
        raise ValueError(f"cannot update status: invalid frontmatter: {path}")

    fm = dict(res.frontmatter)
    fm["status"] = status
    fm["updated_at"] = to_rfc3339(now_utc())
    if extra:
        fm.update(extra)

    _write_markdown_with_frontmatter(path, fm, res.body)


def _sync_index_for_subplan(letter_dir: Path) -> None:
    idx_path = letter_dir / "index.md"
    idx_res = read_frontmatter(idx_path)
    if idx_res.frontmatter is None:
        return

    # Build status map from task files.
    task_status: dict[str, str] = {}
    for md in sorted(letter_dir.glob("*.md")):
        roman = md.stem.lower()
        if roman == "index" or roman not in ROMAN_NUMERALS:
            continue
        t_res = read_frontmatter(md)
        if t_res.frontmatter is None:
            continue
        st = str(t_res.frontmatter.get("status", "pending"))
        task_status[roman] = st

    fm = dict(idx_res.frontmatter)
    tasks = fm.get("tasks", [])
    if isinstance(tasks, list):
        new_tasks: list[dict[str, Any]] = []
        for t in tasks:
            if not isinstance(t, dict):
                continue
            roman = str(t.get("task", "")).lower()
            if roman and roman in task_status:
                new_tasks.append({**t, "status": task_status[roman]})
            else:
                new_tasks.append(t)
        fm["tasks"] = new_tasks

    # Derive subplan status.
    statuses = [task_status[r] for r in sorted(task_status.keys(), key=lambda x: ROMAN_NUMERALS.index(x))]
    if statuses:
        if any(s == "in_progress" for s in statuses):
            fm["status"] = "in_progress"
        elif any(s == "pending" for s in statuses):
            fm["status"] = "pending"
        elif any(s == "blocked" for s in statuses):
            fm["status"] = "blocked"
        elif all(s == "deferred" for s in statuses):
            fm["status"] = "deferred"
        else:
            # all terminal (complete/deferred/abandoned) => complete
            fm["status"] = "complete"

    fm["updated_at"] = to_rfc3339(now_utc())
    _write_markdown_with_frontmatter(idx_path, fm, idx_res.body)


def sync_derived_state() -> None:
    """
    Deterministically sync derived status fields (index.md + plan.md) from task files.
    This is safe to rerun and improves auditability.
    """
    root_path = ACTIVE_DIR / "plan.md"
    root_res = read_frontmatter(root_path)
    if root_res.frontmatter is None:
        return

    # Sync all subplan indexes first.
    for letter_dir in sorted([p for p in ACTIVE_DIR.iterdir() if p.is_dir() and len(p.name) == 1]):
        _sync_index_for_subplan(letter_dir)

    # Derive root status from tasks.
    tasks = list_tasks()
    statuses = [str(fm.get("status", "pending")) for _, fm in tasks]

    fm = dict(root_res.frontmatter)
    if statuses:
        if any(s == "in_progress" for s in statuses):
            fm["status"] = "in_progress"
        elif any(s == "pending" for s in statuses):
            fm["status"] = "pending"
        elif any(s == "blocked" for s in statuses):
            fm["status"] = "blocked"
        elif all(s == "deferred" for s in statuses):
            fm["status"] = "deferred"
        else:
            fm["status"] = "complete"

    fm["updated_at"] = to_rfc3339(now_utc())
    _write_markdown_with_frontmatter(root_path, fm, root_res.body)


def ensure_one_in_progress_task() -> tuple[Path, dict[str, Any]] | None:
    """
    Ensure there is exactly one `in_progress` task unless the plan is terminal.
    If none exists, deterministically selects the next pending task and marks it in_progress.
    """
    if is_terminal():
        return None

    tasks = list_tasks()
    in_progress = [(p, fm) for p, fm in tasks if fm.get("status") == "in_progress"]
    if len(in_progress) > 1:
        raise ValueError(f"expected at most 1 in_progress task, found {len(in_progress)}")
    if len(in_progress) == 1:
        return in_progress[0]

    # No in_progress: pick first pending in deterministic order.
    for path in _ordered_task_paths():
        res = read_frontmatter(path)
        if res.frontmatter is None:
            continue
        if res.frontmatter.get("status") != "pending":
            continue

        proposed = dict(res.frontmatter)
        proposed["status"] = "in_progress"
        proposed["updated_at"] = to_rfc3339(now_utc())
        schema_errors = validate_task_frontmatter(proposed)
        if schema_errors:
            raise ValueError(
                f"cannot start task {path}: task would violate schema when set to in_progress: "
                + "; ".join(schema_errors[:10])
            )

        _write_markdown_with_frontmatter(path, proposed, res.body)
        sync_derived_state()
        return path, proposed

    return None


def current_task() -> tuple[Path, dict[str, Any]] | None:
    tasks = list_tasks()
    for p, fm in tasks:
        if fm.get("status") == "in_progress":
            return p, fm
    return None


def is_terminal() -> bool:
    tasks = list_tasks()
    if not tasks:
        return False
    return all((fm.get("status") in TERMINAL_TASK_STATUSES) for _, fm in tasks)


def _compute_archive_id(root_frontmatter: dict[str, Any]) -> str:
    title = str(root_frontmatter.get("title", "plan"))
    h = hashlib.sha256(title.encode("utf-8")).hexdigest()[:8]
    ts = to_rfc3339(now_utc()).replace(":", "-")
    return f"{ts}-{h}"


def archive_active_plan() -> Path:
    ensure_plan_dir()
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    root_path = ACTIVE_DIR / "plan.md"
    root = read_frontmatter(root_path)
    if root.frontmatter is None:
        raise ValueError("cannot archive: missing/invalid active plan root frontmatter")

    archive_id = _compute_archive_id(root.frontmatter)
    dest = ARCHIVE_DIR / archive_id

    if dest.exists():
        raise ValueError(f"archive destination already exists: {dest}")

    shutil.move(str(ACTIVE_DIR), str(dest))

    # Move intent artifact alongside archived plan if it exists.
    if ACTIVE_INTENT_PATH.exists():
        shutil.move(str(ACTIVE_INTENT_PATH), str(dest / "intent.yaml"))

    # Write receipt.json
    tasks = []
    for p in sorted(dest.rglob("*.md")):
        if p.name == "plan.md":
            continue
        if p.stem.lower() == "index":
            continue
        if p.stem.lower() not in ROMAN_NUMERALS:
            continue
        res = read_frontmatter(p)
        if res.frontmatter:
            tasks.append(res.frontmatter)

    complete = sum(1 for t in tasks if t.get("status") == "complete")
    deferred = sum(1 for t in tasks if t.get("status") == "deferred")
    total = len(tasks)

    receipt = {
        "version": "1",
        "archived_at": to_rfc3339(now_utc()),
        "archive_id": archive_id,
        "plan_title": str(root.frontmatter.get("title", "")),
        "status_summary": {"complete": complete, "deferred": deferred, "total": total},
        "paths": {"repo_root": str(REPO_ROOT), "archive_dir": str(dest)},
    }

    if not RECEIPT_SCHEMA_PATH.exists():
        raise ValueError(f"missing receipt schema: {RECEIPT_SCHEMA_PATH}")
    receipt_errors = _schema_errors(_load_json(RECEIPT_SCHEMA_PATH), receipt)
    if receipt_errors:  # pragma: no cover
        raise ValueError("archive receipt does not match schema: " + "; ".join(receipt_errors))

    (dest / "receipt.json").write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    return dest
