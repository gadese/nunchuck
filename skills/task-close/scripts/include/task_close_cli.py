#!/usr/bin/env python3

import argparse
import importlib.util
import sys

from task_hash import compute_intent_hash
from task_parse import get_task_path, parse_task_file, read_active_task, serialize_task, write_active_task
from task_time import now_utc, to_rfc3339


def cmd_help() -> int:
    print(
        """task-close - Close a task

Usage:
  task-close <id> --reason {completed|abandoned}
  task-close help
  task-close validate

Updates .tasks/<id>.md frontmatter:
- sets state=closed
- sets close_reason
- sets closed_at and updated_at
- recomputes intent_hash
If the closed task is currently active, clears .tasks/.active.
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

    print("ok: task-close CLI is runnable")
    return 0


def cmd_close(task_id: str, reason: str) -> int:
    task_path = get_task_path(task_id)

    if not task_path.exists():
        print(f"error: task '{task_id}' not found", file=sys.stderr)
        return 1

    fm, body = parse_task_file(task_path)

    if fm.get("state") == "closed":
        print(f"error: task '{task_id}' is already closed", file=sys.stderr)
        return 1

    now = to_rfc3339(now_utc())

    fm["state"] = "closed"
    fm["close_reason"] = reason
    fm["closed_at"] = now
    fm["updated_at"] = now

    content = serialize_task(fm, body)
    intent_hash = compute_intent_hash(content)
    fm["intent_hash"] = intent_hash

    final_content = serialize_task(fm, body)
    task_path.write_text(final_content, encoding="utf-8")

    print(f"closed: {task_id} ({reason})")

    active_id = read_active_task()
    if active_id == task_id:
        write_active_task(None)
        print("cleared: .tasks/.active")

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="task-close", add_help=False)
    parser.add_argument("command_or_id", nargs="?")
    parser.add_argument("--reason", choices=["completed", "abandoned"])
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command_or_id in (None, "help"):
        return cmd_help()

    if args.command_or_id == "validate":
        return cmd_validate()

    if args.reason is None:
        print("error: --reason is required", file=sys.stderr)
        return 1

    return cmd_close(args.command_or_id, args.reason)


if __name__ == "__main__":
    sys.exit(main())
