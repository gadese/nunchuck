"""Parse and manage prompt artifacts."""

import hashlib
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


PROMPT_DIR = Path(".prompt")
ACTIVE_PATH = PROMPT_DIR / "active.yaml"
RECEIPTS_DIR = PROMPT_DIR / "receipts"

VALID_STATUSES = ("drafting", "ready")


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def to_rfc3339(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def compute_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def ensure_prompt_dir() -> None:
    PROMPT_DIR.mkdir(exist_ok=True)


def ensure_receipts_dir() -> None:
    ensure_prompt_dir()
    RECEIPTS_DIR.mkdir(exist_ok=True)


def artifact_exists() -> bool:
    return ACTIVE_PATH.exists()


def load_artifact() -> dict[str, Any] | None:
    if not artifact_exists():
        return None
    content = ACTIVE_PATH.read_text(encoding="utf-8")
    return yaml.safe_load(content)


def save_artifact(artifact: dict[str, Any]) -> None:
    ensure_prompt_dir()
    artifact["updated_at"] = to_rfc3339(now_utc())
    content = yaml.dump(artifact, default_flow_style=False, allow_unicode=True, sort_keys=False)
    ACTIVE_PATH.write_text(content, encoding="utf-8")


def delete_artifact() -> bool:
    if artifact_exists():
        ACTIVE_PATH.unlink()
        return True
    return False


def create_empty_artifact() -> dict[str, Any]:
    now = to_rfc3339(now_utc())
    return {
        "version": "1",
        "status": "drafting",
        "created_at": now,
        "updated_at": now,
        "intent": {
            "objective": "",
            "constraints": [],
            "assumptions": [],
            "open_questions": [],
        },
        "prompt": "",
        "quality": None,
    }


def validate_artifact(artifact: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    if not isinstance(artifact, dict):
        return ["artifact is not a dictionary"]

    if artifact.get("version") != "1":
        errors.append("missing or invalid version (expected '1')")

    status = artifact.get("status")
    if status not in VALID_STATUSES:
        errors.append(f"invalid status '{status}' (expected: {VALID_STATUSES})")

    if not artifact.get("created_at"):
        errors.append("missing created_at")

    if not artifact.get("updated_at"):
        errors.append("missing updated_at")

    intent = artifact.get("intent")
    if not isinstance(intent, dict):
        errors.append("missing or invalid intent object")
    elif not intent.get("objective") and status == "ready":
        errors.append("ready artifact must have an objective")

    if status == "ready" and not artifact.get("prompt"):
        errors.append("ready artifact must have a prompt")

    return errors


def write_receipt(artifact: dict[str, Any]) -> Path:
    ensure_receipts_dir()

    prompt_text = artifact.get("prompt", "")
    prompt_hash = compute_hash(prompt_text)
    timestamp = to_rfc3339(now_utc()).replace(":", "-")

    receipt = {
        "version": "1",
        "executed_at": to_rfc3339(now_utc()),
        "prompt_hash": prompt_hash,
        "prompt": prompt_text,
        "intent": artifact.get("intent"),
        "quality": artifact.get("quality"),
    }

    filename = f"{timestamp}-{prompt_hash[:8]}.yaml"
    receipt_path = RECEIPTS_DIR / filename

    content = yaml.dump(receipt, default_flow_style=False, allow_unicode=True, sort_keys=False)
    receipt_path.write_text(content, encoding="utf-8")

    return receipt_path


def list_receipts() -> list[Path]:
    if not RECEIPTS_DIR.exists():
        return []
    return sorted(RECEIPTS_DIR.glob("*.yaml"))


COMPILED_PATH = PROMPT_DIR / "PROMPT.md"


def compile_to_markdown(artifact: dict[str, Any]) -> str:
    intent = artifact.get("intent", {})

    lines: list[str] = []
    lines.append("# Prompt")
    lines.append("")

    objective = intent.get("objective", "").strip()
    if objective:
        lines.append("## Objective")
        lines.append("")
        lines.append(objective)
        lines.append("")

    constraints = intent.get("constraints", [])
    if constraints:
        lines.append("## Constraints")
        lines.append("")
        lines.append("The following constraints must be respected:")
        lines.append("")
        for c in constraints:
            lines.append(f"- {c}")
        lines.append("")

    assumptions = intent.get("assumptions", [])
    if assumptions:
        lines.append("## Assumptions")
        lines.append("")
        lines.append("The following assumptions are in effect:")
        lines.append("")
        for a in assumptions:
            lines.append(f"- {a}")
        lines.append("")

    prompt_text = artifact.get("prompt", "").strip()
    if prompt_text:
        lines.append("## Prompt Text")
        lines.append("")
        lines.append(prompt_text)
        lines.append("")

    quality = artifact.get("quality")
    if quality and isinstance(quality, dict):
        grade = quality.get("grade")
        if grade:
            lines.append("## Quality Assessment")
            lines.append("")
            lines.append(f"**Grade**: {grade}")
            reasons = quality.get("reasons", [])
            if reasons:
                lines.append("")
                for r in reasons:
                    lines.append(f"- {r}")
            top_fix = quality.get("top_fix")
            if top_fix:
                lines.append("")
                lines.append(f"**Top fix**: {top_fix}")
            lines.append("")

    return "\n".join(lines)


def write_compiled(content: str) -> Path:
    ensure_prompt_dir()
    COMPILED_PATH.write_text(content, encoding="utf-8")
    return COMPILED_PATH


def compiled_exists() -> bool:
    return COMPILED_PATH.exists()
