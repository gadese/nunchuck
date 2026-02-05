#!/usr/bin/env python3
"""Task List CLI - List tasks with derived flags."""

import argparse
import sys

from task_hash import verify_intent_hash
from task_parse import (
    list_task_files,
    parse_task_file,
    read_active_task,
)
from task_time import is_stale


def cmd_list(args: argparse.Namespace) -> int:
    """List tasks with derived flags."""
    task_files = list_task_files()
    
    if not task_files:
        print("no tasks found in .tasks/")
        return 0
    
    active_id = read_active_task()
    tasks = []
    
    for path in task_files:
        fm, body = parse_task_file(path)
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
        
        tasks.append({
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
        })
    
    tasks.sort(key=lambda t: t["updated_at"], reverse=True)
    
    for t in tasks:
        flags = []
        if t["is_active"]:
            flags.append("*")
        if t["is_stale"]:
            flags.append(f"stale:{t['stale_reason']}")
        if t["hash_mismatch"]:
            flags.append("hash-mismatch")
        
        flag_str = f" [{', '.join(flags)}]" if flags else ""
        print(f"{t['id']} | {t['state']} | {t['kind']} | {t['risk']} | {t['title']}{flag_str}")
    
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="task-list", description="List tasks with derived flags")
    parser.add_argument("--state", choices=["draft", "open", "closed", "invalid"])
    parser.add_argument("--stale", action="store_true", help="Show only stale tasks")
    
    args = parser.parse_args()
    return cmd_list(args)


if __name__ == "__main__":
    sys.exit(main())
