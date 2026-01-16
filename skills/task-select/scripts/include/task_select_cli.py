#!/usr/bin/env python3

import argparse
import importlib.util
import sys

from task_hash import verify_intent_hash
from task_parse import get_task_path, parse_task_file, write_active_task
from task_time import is_stale


def cmd_help() -> int:
    print(
        """task-select - Select a task as active

Usage:
  task-select <id>
  task-select help
  task-select validate

Writes the active task ID to .tasks/.active.
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

    print("ok: task-select CLI is runnable")
    return 0


def cmd_select(task_id: str) -> int:
    task_path = get_task_path(task_id)

    if not task_path.exists():
        print(f"error: task '{task_id}' not found", file=sys.stderr)
        return 1

    fm, _ = parse_task_file(task_path)
    content = task_path.read_text(encoding="utf-8")

    stale, stale_reason = is_stale(
        fm.get("last_reviewed_at"),
        fm.get("updated_at"),
        fm.get("created_at", ""),
        fm.get("staleness_days_threshold", 21),
    )

    hash_ok, _ = verify_intent_hash(content, fm.get("intent_hash"))

    write_active_task(task_id)
    print(f"selected: {task_path}")

    if stale:
        print(f"warning: task is stale ({stale_reason})", file=sys.stderr)
    if not hash_ok:
        print("warning: intent hash mismatch - task may have drifted", file=sys.stderr)

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="task-select", add_help=False)
    parser.add_argument("command_or_id", nargs="?")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command_or_id in (None, "help"):
        return cmd_help()

    if args.command_or_id == "validate":
        return cmd_validate()

    return cmd_select(args.command_or_id)


if __name__ == "__main__":
    sys.exit(main())
