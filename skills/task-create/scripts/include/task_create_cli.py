#!/usr/bin/env python3

import argparse
import importlib.util
import sys
from typing import Any

from task_hash import compute_intent_hash
from task_parse import get_task_path, get_tasks_dir, serialize_task, write_active_task
from task_time import now_utc, to_rfc3339


def cmd_help() -> int:
    print(
        """task-create - Create a new task

Usage:
  task-create <id> [--title TITLE] [--kind KIND] [--risk RISK] [--goal GOAL] [--select]
  task-create help
  task-create validate

Creates a new task at .tasks/<id>.md
"""
    )
    return 0


def cmd_validate() -> int:
    errors: list[str] = []

    if importlib.util.find_spec("yaml") is None:
        errors.append("missing dependency: pyyaml")

    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    print("ok: task-create CLI is runnable")
    return 0


def cmd_create(args: argparse.Namespace) -> int:
    tasks_dir = get_tasks_dir()
    tasks_dir.mkdir(exist_ok=True)

    task_id = args.id
    task_path = get_task_path(task_id)

    if task_path.exists():
        print(f"error: task '{task_id}' already exists", file=sys.stderr)
        return 1

    now = to_rfc3339(now_utc())

    body = f"""## Goal

{args.goal or 'TODO: Define the goal'}

## Acceptance

- [ ] TODO: Define acceptance criteria

## Constraints

- None specified

## Dependencies

- None

## Evidence

<!-- Evidence section is excluded from intent hash -->
"""

    frontmatter: dict[str, Any] = {
        "id": task_id,
        "title": args.title or task_id.replace("-", " ").title(),
        "kind": args.kind,
        "risk": args.risk,
        "state": "draft",
        "created_at": now,
        "updated_at": now,
        "intent_hash_algo": "sha256-v1",
        "intent_hash_scope": "canonical-intent",
        "staleness_days_threshold": 21,
    }

    content = serialize_task(frontmatter, body)
    intent_hash = compute_intent_hash(content)
    frontmatter["intent_hash"] = intent_hash

    final_content = serialize_task(frontmatter, body)
    task_path.write_text(final_content, encoding="utf-8")

    print(f"created: {task_path}")

    if args.select:
        write_active_task(task_id)
        print(f"selected: {task_id}")

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="task-create", add_help=False)

    parser.add_argument("command_or_id", nargs="?", help="'help', 'validate', or task id")
    parser.add_argument("--title", help="Task title")
    parser.add_argument("--kind", choices=["feature", "fix", "refactor", "docs", "chore", "spike"], default="feature")
    parser.add_argument("--risk", choices=["low", "medium", "high"], default="low")
    parser.add_argument("--goal", help="Initial goal text")
    parser.add_argument("--select", action="store_true", help="Auto-select after creation")

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command_or_id in (None, "help"):
        return cmd_help()

    if args.command_or_id == "validate":
        return cmd_validate()

    args.id = args.command_or_id
    return cmd_create(args)


if __name__ == "__main__":
    sys.exit(main())
