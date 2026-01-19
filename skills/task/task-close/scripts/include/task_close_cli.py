#!/usr/bin/env python3
"""Task Close CLI - Close a task."""

import argparse
import sys

from task_hash import compute_intent_hash
from task_parse import (
    get_task_path,
    parse_task_file,
    read_active_task,
    serialize_task,
    write_active_task,
)
from task_time import now_utc, to_rfc3339


def cmd_close(args: argparse.Namespace) -> int:
    """Close a task."""
    task_id = args.id
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
    fm["close_reason"] = args.reason
    fm["closed_at"] = now
    fm["updated_at"] = now
    
    content = serialize_task(fm, body)
    intent_hash = compute_intent_hash(content)
    fm["intent_hash"] = intent_hash
    
    final_content = serialize_task(fm, body)
    task_path.write_text(final_content, encoding="utf-8")
    
    print(f"closed: {task_id} ({args.reason})")
    
    active_id = read_active_task()
    if active_id == task_id:
        write_active_task(None)
        print("cleared: .tasks/.active")
    
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="task-close", description="Close a task")
    parser.add_argument("id", help="Task ID to close")
    parser.add_argument("--reason", choices=["completed", "abandoned"], required=True)
    
    args = parser.parse_args()
    return cmd_close(args)


if __name__ == "__main__":
    sys.exit(main())
