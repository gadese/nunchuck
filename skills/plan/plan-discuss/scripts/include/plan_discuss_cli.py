#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys

from plan_discuss_parse import (
    ACTIVE_ARTIFACT_PATH,
    artifact_exists,
    create_empty_artifact,
    load_artifact,
    save_artifact,
    validate_artifact,
)


def cmd_help() -> int:
    print(
        """plan-discuss - Shape and stabilize intent into .plan/active.yaml

Usage:
  plan-discuss [--mark-ready]
  plan-discuss help
  plan-discuss validate

Deterministic behavior:
- Ensures .plan/active.yaml exists (creates it if missing)
- Prints current artifact status and any schema errors
- Optionally marks artifact ready (requires no open questions)
"""
    )
    return 0


def cmd_validate() -> int:
    errors: list[str] = []

    try:
        import yaml  # noqa: F401
    except Exception:
        errors.append("missing dependency: pyyaml")

    try:
        import jsonschema  # noqa: F401
    except Exception:
        errors.append("missing dependency: jsonschema")

    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    print("ok: plan-discuss CLI is runnable")
    return 0


def ensure_artifact_exists() -> None:
    if artifact_exists():
        return
    save_artifact(create_empty_artifact())


def print_status() -> int:
    if not artifact_exists():
        print("status: no active plan intent")
        print(f"path: {ACTIVE_ARTIFACT_PATH} (does not exist)")
        return 0

    artifact = load_artifact() or {}
    errors = validate_artifact(artifact)

    print(f"status: {artifact.get('status', 'unknown')}")
    print(f"path: {ACTIVE_ARTIFACT_PATH}")
    print(f"created: {artifact.get('created_at', 'unknown')}")
    print(f"updated: {artifact.get('updated_at', 'unknown')}")

    intent = artifact.get("intent", {}) if isinstance(artifact, dict) else {}
    title = intent.get("title", "")
    objective = intent.get("objective", "")
    print(f"title: {title or '(empty)'}")
    print(f"objective: {objective[:60]}..." if len(objective) > 60 else f"objective: {objective or '(empty)'}")

    open_q = intent.get("open_questions", []) if isinstance(intent, dict) else []
    if isinstance(open_q, list):
        print(f"open_questions: {len(open_q)}")

    if errors:
        print(f"errors: {len(errors)}")
        for e in errors:
            print(f"  - {e}")

    return 0


def mark_ready() -> int:
    if not artifact_exists():
        print("error: no active plan intent", file=sys.stderr)
        return 1

    artifact = load_artifact() or {}
    if not isinstance(artifact, dict):
        print("error: invalid artifact (not a mapping)", file=sys.stderr)
        return 1

    errors = validate_artifact(artifact)
    if errors:
        print(f"error: artifact has {len(errors)} schema errors", file=sys.stderr)
        for e in errors:
            print(f"  - {e}", file=sys.stderr)
        return 1

    intent = artifact.get("intent", {})
    open_q = intent.get("open_questions", []) if isinstance(intent, dict) else []
    if isinstance(open_q, list) and open_q:
        print(f"error: {len(open_q)} open questions remain", file=sys.stderr)
        for q in open_q:
            print(f"  - {q}", file=sys.stderr)
        return 1

    # Strengthen readiness beyond schema basics: ensure tasks are executable.
    structure = artifact.get("structure", {})
    subplans = structure.get("subplans", []) if isinstance(structure, dict) else []
    task_errors: list[str] = []
    if isinstance(subplans, list):
        for sp in subplans:
            if not isinstance(sp, dict):
                continue
            letter = sp.get("letter", "?")
            tasks = sp.get("tasks", [])
            if not isinstance(tasks, list):
                continue
            for t in tasks:
                if not isinstance(t, dict):
                    continue
                task_id = t.get("task", "?")
                focus = str(t.get("focus", "")).strip()
                work = t.get("work", [])
                crit = t.get("success_criteria", [])
                val = t.get("validation_steps", [])
                if not focus:
                    task_errors.append(f"{letter}/{task_id}: focus is empty")
                if not isinstance(work, list) or not work:
                    task_errors.append(f"{letter}/{task_id}: work is empty")
                if not isinstance(crit, list) or not crit:
                    task_errors.append(f"{letter}/{task_id}: success_criteria is empty")
                if not isinstance(val, list) or not val:
                    task_errors.append(f"{letter}/{task_id}: validation_steps is empty")

    if task_errors:
        print(f"error: {len(task_errors)} task guardrail violations prevent ready", file=sys.stderr)
        for e in task_errors[:50]:
            print(f"  - {e}", file=sys.stderr)
        return 1

    artifact["status"] = "ready"
    save_artifact(artifact)
    print("status: ready")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="plan-discuss", add_help=False)
    parser.add_argument("command", nargs="?", help="help or validate")
    parser.add_argument("--mark-ready", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "help":
        return cmd_help()

    if args.command == "validate":
        return cmd_validate()

    ensure_artifact_exists()

    if args.mark_ready:
        return mark_ready()

    return print_status()


if __name__ == "__main__":
    raise SystemExit(main())
