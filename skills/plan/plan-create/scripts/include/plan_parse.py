"""Deterministic plan compilation and validation.

State model:
- Plan intent artifact: `.plan/active.yaml` (plan-discuss)
- Compiled plan: `.plan/active/` (plan-create)
- Archive: `.plan/archive/<id>/` (plan-exec)
"""

from __future__ import annotations

import json
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
INTENT_SCHEMA_PATH = ASSETS_DIR / "plan-discuss-artifact-schema.json"
ROOT_SCHEMA_PATH = ASSETS_DIR / "plan-root-schema.json"
SUBPLAN_SCHEMA_PATH = ASSETS_DIR / "plan-subplan-schema.json"
TASK_SCHEMA_PATH = ASSETS_DIR / "plan-task-schema.json"

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


def validate_intent(intent: dict[str, Any]) -> list[str]:
    if not INTENT_SCHEMA_PATH.exists():
        return [f"missing schema: {INTENT_SCHEMA_PATH}"]
    return _schema_errors(_load_json(INTENT_SCHEMA_PATH), intent)


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


def load_intent() -> dict[str, Any] | None:
    if not ACTIVE_INTENT_PATH.exists():
        return None
    return yaml.safe_load(ACTIVE_INTENT_PATH.read_text(encoding="utf-8"))


def _default_surface_scan(intent: dict[str, Any]) -> dict[str, Any]:
    surface = intent.get("surface")
    if isinstance(surface, dict):
        return surface
    return {
        "root": ".",
        "globs": ["**/*.md", "**/*.py", "**/*.ts", "**/*.js", "**/*.yaml", "**/*.yml", "**/*.json"],
        "excludes": ["**/.git/**", "**/.venv/**", "**/node_modules/**", "**/__pycache__/**", "**/.plan/**"],
        "max_files": 200,
    }


def _match_any_glob(rel: Path, globs: list[str]) -> bool:
    s = str(rel).replace("\\", "/")
    for g in globs:
        # Simple globbing: Path.match uses platform separators; normalize pattern too.
        if Path(s).match(g) or rel.match(g):
            return True
    return False


def surface_scan(root: Path, *, globs: list[str], excludes: list[str], max_files: int) -> list[str]:
    root = root.resolve()
    results: list[str] = []
    for p in sorted(root.rglob("*")):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        rel_str = str(rel).replace("\\", "/")

        if any(Path(rel_str).match(ex) for ex in excludes):
            continue
        if not _match_any_glob(rel, globs):
            continue

        results.append(rel_str)
        if len(results) >= max_files:
            break
    return results


def _active_paths() -> tuple[Path, Path]:
    return ACTIVE_DIR / "plan.md", ACTIVE_DIR


def _subplan_dir(letter: str) -> Path:
    return ACTIVE_DIR / letter


def _subplan_index(letter: str) -> Path:
    return _subplan_dir(letter) / "index.md"


def _task_path(letter: str, roman: str) -> Path:
    return _subplan_dir(letter) / f"{roman}.md"


def compile_active_plan(*, overwrite: bool) -> Path:
    """
    Compile `.plan/active.yaml` into `.plan/active/`.

    Design invariant: there is exactly one `in_progress` task unless the plan is terminal.
    """
    ensure_plan_dir()

    intent = load_intent()
    if intent is None:
        raise ValueError(f"missing plan intent: {ACTIVE_INTENT_PATH}")

    if not isinstance(intent, dict):
        raise ValueError("plan intent is not a mapping/object")

    intent_errors = validate_intent(intent)
    if intent_errors:
        raise ValueError("plan intent does not match schema: " + "; ".join(intent_errors))

    if intent.get("status") != "ready":
        raise ValueError("plan intent is not ready (run plan-discuss --mark-ready)")

    if ACTIVE_DIR.exists():
        if not overwrite:
            raise ValueError(f"active plan already exists at {ACTIVE_DIR} (use --force to overwrite)")
        import shutil

        shutil.rmtree(ACTIVE_DIR)

    ACTIVE_DIR.mkdir(parents=True, exist_ok=True)

    now = to_rfc3339(now_utc())
    intent_obj = intent.get("intent", {})
    if not isinstance(intent_obj, dict):
        intent_obj = {}

    title = str(intent_obj.get("title") or "Plan")
    objective = str(intent_obj.get("objective") or "")
    success_criteria = intent_obj.get("success_criteria") or []
    if not isinstance(success_criteria, list):
        success_criteria = []

    structure = intent.get("structure", {})
    subplans = structure.get("subplans", []) if isinstance(structure, dict) else []
    if not isinstance(subplans, list) or not subplans:
        subplans = [{"letter": "a", "title": "Sub-plan A", "tasks": [{"task": "i", "title": "Task 1"}]}]

    # Bake in deterministic surface scan for auditable coverage.
    surface_cfg = _default_surface_scan(intent)
    root_rel = Path(str(surface_cfg.get("root", ".")))
    globs = surface_cfg.get("globs", [])
    excludes = surface_cfg.get("excludes", [])
    max_files = int(surface_cfg.get("max_files", 200))
    if not isinstance(globs, list):
        globs = []
    if not isinstance(excludes, list):
        excludes = []

    scanned_files = surface_scan(
        (REPO_ROOT / root_rel).resolve(),
        globs=[str(g) for g in globs],
        excludes=[str(e) for e in excludes],
        max_files=max_files,
    )

    root_frontmatter = {
        "version": "1",
        "kind": "plan_root",
        "plan": 1,
        "status": "pending",
        "created_at": now,
        "updated_at": now,
        "title": title,
        "objective": objective,
        "success_criteria": [str(x) for x in success_criteria if str(x).strip()],
        "subplans": [{"letter": str(sp.get("letter")), "title": str(sp.get("title"))} for sp in subplans],
        "surface_scan": {
            "root": str(root_rel),
            "globs": [str(g) for g in globs],
            "excludes": [str(e) for e in excludes],
            "max_files": max_files,
            "files": scanned_files,
        },
    }

    root_errors = validate_root_frontmatter(root_frontmatter)
    if root_errors:  # pragma: no cover
        raise ValueError("root plan frontmatter does not match schema: " + "; ".join(root_errors))

    root_body = """# Active Plan

The YAML frontmatter is the authoritative state.
This Markdown body is non-authoritative and is for narrative, rationale, and notes.
"""
    _write_markdown_with_frontmatter(ACTIVE_DIR / "plan.md", root_frontmatter, root_body)

    for sp in subplans:
        letter = str(sp.get("letter", "")).strip() or "a"
        sp_title = str(sp.get("title", "")).strip() or f"Sub-plan {letter.upper()}"
        tasks = sp.get("tasks", [])
        if not isinstance(tasks, list) or not tasks:
            tasks = [{"task": "i", "title": "Task 1"}]

        _subplan_dir(letter).mkdir(exist_ok=True)

        idx_frontmatter = {
            "version": "1",
            "kind": "plan_subplan",
            "plan": 1,
            "subplan": letter,
            "status": "pending",
            "created_at": now,
            "updated_at": now,
            "title": sp_title,
            "tasks": [],
        }

        for t in tasks:
            if not isinstance(t, dict):
                continue
            roman = str(t.get("task", "i")).lower()
            if roman not in ROMAN_NUMERALS:
                continue
            t_title = str(t.get("title", "")).strip() or f"Task {roman}"
            status = "pending"
            idx_frontmatter["tasks"].append({"task": roman, "title": t_title, "status": status})

            focus = str(t.get("focus", "") or "")
            inputs = t.get("inputs", [])
            work = t.get("work", [])
            criteria = t.get("success_criteria", [])
            validation_steps = t.get("validation_steps", [])
            risk = str(t.get("risk", "low") or "low")

            task_frontmatter = {
                "version": "1",
                "kind": "plan_task",
                "plan": 1,
                "subplan": letter,
                "task": roman,
                "status": status,
                "created_at": now,
                "updated_at": now,
                "title": t_title,
                "focus": focus,
                "inputs": [str(x) for x in inputs] if isinstance(inputs, list) else [],
                "work": [str(x) for x in work] if isinstance(work, list) else [],
                "success_criteria": [str(x) for x in criteria] if isinstance(criteria, list) else [],
                "outputs": [],
                "handoff": "",
                "assumptions": [],
                "constraints": [],
                "risk": risk,
                "validation_steps": [str(x) for x in validation_steps] if isinstance(validation_steps, list) else [],
            }

            task_errors = validate_task_frontmatter(task_frontmatter)
            if task_errors:  # pragma: no cover
                raise ValueError("task frontmatter does not match schema: " + "; ".join(task_errors))

            task_body = f"""# {t_title}

The YAML frontmatter is the authoritative state.
Use this body for supporting context only.
"""
            _write_markdown_with_frontmatter(_task_path(letter, roman), task_frontmatter, task_body)

        idx_errors = validate_subplan_frontmatter(idx_frontmatter)
        if idx_errors:  # pragma: no cover
            raise ValueError("subplan frontmatter does not match schema: " + "; ".join(idx_errors))

        idx_body = f"""# {sp_title}

The YAML frontmatter declares tasks and their statuses. Keep it in sync with task files.
"""
        _write_markdown_with_frontmatter(_subplan_index(letter), idx_frontmatter, idx_body)

    return ACTIVE_DIR


def list_active_tasks() -> list[tuple[str, str, Path, dict[str, Any]]]:
    tasks: list[tuple[str, str, Path, dict[str, Any]]] = []
    if not ACTIVE_DIR.exists():
        return tasks
    for letter_dir in sorted([p for p in ACTIVE_DIR.iterdir() if p.is_dir() and len(p.name) == 1]):
        letter = letter_dir.name
        for md in sorted(letter_dir.glob("*.md")):
            roman = md.stem.lower()
            if roman == "index" or roman not in ROMAN_NUMERALS:
                continue
            fm_res = read_frontmatter(md)
            if fm_res.frontmatter:
                tasks.append((letter, roman, md, fm_res.frontmatter))
    return tasks


def validate_active_plan() -> list[str]:
    errors: list[str] = []
    if not (ACTIVE_DIR / "plan.md").exists():
        return [f"missing active plan: {ACTIVE_DIR / 'plan.md'}"]

    root = read_frontmatter(ACTIVE_DIR / "plan.md")
    if root.errors or root.frontmatter is None:
        return [f"{ACTIVE_DIR / 'plan.md'}: " + "; ".join(root.errors or ["invalid frontmatter"])]

    root_schema_errors = validate_root_frontmatter(root.frontmatter)
    errors.extend([f"{ACTIVE_DIR / 'plan.md'}: {e}" for e in root_schema_errors])

    tasks = list_active_tasks()
    in_progress = [t for t in tasks if t[3].get("status") == "in_progress"]

    # Execution invariant: at most one in_progress task at a time.
    if len(in_progress) > 1:
        errors.append(f"expected at most 1 in_progress task, found {len(in_progress)}")

    for letter, roman, path, fm in tasks:
        schema_errors = validate_task_frontmatter(fm)
        errors.extend([f"{path}: {e}" for e in schema_errors])

        if fm.get("subplan") != letter:
            errors.append(f"{path}: subplan must be '{letter}'")
        if fm.get("task") != roman:
            errors.append(f"{path}: task must be '{roman}'")

    return errors
