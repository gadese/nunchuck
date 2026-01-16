#!/usr/bin/env python3

import argparse
import importlib.util
import sys

from task_hash import verify_intent_hash
from task_parse import list_task_files, parse_task_file, read_active_task
from task_time import is_stale


def cmd_help() -> int:
    print(
        """task-list - List tasks with derived flags

Usage:
  task-list [--state STATE] [--stale]
  task-list help
  task-list validate

Reads tasks from .tasks/<id>.md and prints derived flags (active, stale, hash-mismatch).
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

    print("ok: task-list CLI is runnable")
    return 0


def cmd_list(args: argparse.Namespace) -> int:
    task_files = list_task_files()

    if not task_files:
        print("no tasks found in .tasks/")
        return 0

    active_id = read_active_task()
    tasks: list[dict[str, object]] = []

    for path in task_files:
        fm, _ = parse_task_file(path)
        if not fm.get("id"):
            continue

        if args.state and fm.get("state") != args.state:
            continue

        stale, stale_reason = is_stale(
            fm.get("last_reviewed_at"),
            fm.get("updated_at"),
            fm.get("created_at", ""),
            fm.get("staleness_days_threshold", 21),
        )

        if args.stale and not stale:
            continue

        content = path.read_text(encoding="utf-8")
        hash_ok, _ = verify_intent_hash(content, fm.get("intent_hash"))

        tasks.append(
            {
                "id": fm["id"],
                "title": fm.get("title", ""),
                "state": fm.get("state", "?"),
                "kind": fm.get("kind", "?"),
                "risk": fm.get("risk", "?"),
                "updated_at": fm.get("updated_at", ""),
                "is_active": fm["id"] == active_id,
                "is_stale": stale,
                "stale_reason": stale_reason,
                "hash_mismatch": not hash_ok,
            }
        )

    tasks.sort(key=lambda t: str(t.get("updated_at", "")), reverse=True)

    for t in tasks:
        flags: list[str] = []
        if t["is_active"]:
            flags.append("*")
        if t["is_stale"]:
            flags.append(f"stale:{t['stale_reason']}")
        if t["hash_mismatch"]:
            flags.append("hash-mismatch")

        flag_str = f" [{', '.join(flags)}]" if flags else ""
        print(
            f"{t['id']} | {t['state']} | {t['kind']} | {t['risk']} | {t['title']}{flag_str}"
        )

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="task-list", add_help=False)
    parser.add_argument("command", nargs="?", help="help, validate, or empty for list")
    parser.add_argument("--state", choices=["draft", "open", "closed", "invalid"])
    parser.add_argument("--stale", action="store_true", help="Show only stale tasks")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command in (None, ""):
        return cmd_list(args)

    if args.command == "help":
        return cmd_help()

    if args.command == "validate":
        return cmd_validate()

    print(f"error: unknown command '{args.command}'", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
