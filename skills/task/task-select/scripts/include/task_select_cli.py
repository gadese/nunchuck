#!/usr/bin/env python3
"""Task Select CLI - Select a task as active."""

import argparse
import sys

from task_hash import verify_intent_hash
from task_parse import (
    get_task_path,
    parse_task_file,
    write_active_task,
)
from task_time import is_stale


def cmd_select(args: argparse.Namespace) -> int:
    """Select a task as active."""
    task_id = args.id
    task_path = get_task_path(task_id)
    
    if not task_path.exists():
        print(f"error: task '{task_id}' not found", file=sys.stderr)
        return 1
    
    fm, body = parse_task_file(task_path)
    content = task_path.read_text(encoding="utf-8")
    
    stale, stale_reason = is_stale(
        fm.get("last_reviewed_at"),
        fm.get("updated_at"),
        fm.get("created_at", ""),
        fm.get("staleness_days_threshold", 21),
    )
    
    hash_ok, computed = verify_intent_hash(content, fm.get("intent_hash"))
    
    write_active_task(task_id)
    print(f"selected: {task_path}")
    
    if stale:
        print(f"warning: task is stale ({stale_reason})", file=sys.stderr)
    if not hash_ok:
        print("warning: intent hash mismatch - task may have drifted", file=sys.stderr)
    
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="task-select", description="Select a task as active")
    parser.add_argument("id", help="Task ID to select")
    
    args = parser.parse_args()
    return cmd_select(args)


if __name__ == "__main__":
    sys.exit(main())
