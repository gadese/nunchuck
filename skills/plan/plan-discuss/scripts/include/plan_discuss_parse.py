"""Parse and validate the plan-discuss artifact stored at `.plan/active.yaml`."""

from __future__ import annotations

import json
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
ACTIVE_ARTIFACT_PATH = PLAN_DIR / "active.yaml"

ASSETS_DIR = REPO_ROOT / "skills" / "plan" / "assets"
SKILL_DIR = Path(__file__).resolve().parents[2]
ASSETS_DIR = SKILL_DIR / "assets"
ARTIFACT_SCHEMA_PATH = ASSETS_DIR / "plan-discuss-artifact-schema.json"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def to_rfc3339(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_plan_dir() -> None:
    PLAN_DIR.mkdir(exist_ok=True)


def artifact_exists() -> bool:
    return ACTIVE_ARTIFACT_PATH.exists()


def load_artifact() -> dict[str, Any] | None:
    if not artifact_exists():
        return None
    return yaml.safe_load(ACTIVE_ARTIFACT_PATH.read_text(encoding="utf-8"))


def save_artifact(artifact: dict[str, Any]) -> None:
    ensure_plan_dir()
    artifact["updated_at"] = to_rfc3339(now_utc())
    content = yaml.safe_dump(artifact, sort_keys=False, allow_unicode=True)
    ACTIVE_ARTIFACT_PATH.write_text(content, encoding="utf-8")


def create_empty_artifact() -> dict[str, Any]:
    now = to_rfc3339(now_utc())
    return {
        "version": "1",
        "status": "drafting",
        "created_at": now,
        "updated_at": now,
        "intent": {
            "title": "Plan",
            "objective": "",
            "constraints": [],
            "assumptions": [],
            "open_questions": [],
            "success_criteria": [],
        },
        "structure": {
            "subplans": [
                {
                    "letter": "a",
                    "title": "Sub-plan A",
                    "tasks": [
                        {
                            "task": "i",
                            "title": "Task 1",
                            "focus": "",
                            "inputs": [],
                            "work": [],
                            "success_criteria": [],
                            "validation_steps": [],
                            "risk": "low",
                        }
                    ],
                }
            ]
        },
        "surface": {
            "root": ".",
            "globs": ["**/*.md", "**/*.py", "**/*.ts", "**/*.js", "**/*.yaml", "**/*.yml", "**/*.json"],
            "excludes": ["**/.git/**", "**/.venv/**", "**/node_modules/**", "**/__pycache__/**", "**/.plan/**"],
            "max_files": 200,
        },
    }


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


def validate_artifact(artifact: dict[str, Any]) -> list[str]:
    if not isinstance(artifact, dict):
        return ["artifact is not a dictionary"]
    if not ARTIFACT_SCHEMA_PATH.exists():
        return [f"missing artifact schema: {ARTIFACT_SCHEMA_PATH}"]
    return _schema_errors(_load_json(ARTIFACT_SCHEMA_PATH), artifact)
