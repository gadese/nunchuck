#!/usr/bin/env python3

from __future__ import annotations

import argparse
import sys

from plan_exec_parse import (
    ACTIVE_DIR,
    archive_active_plan,
    ensure_one_in_progress_task,
    is_terminal,
    sync_derived_state,
    validate_active_plan,
)


def cmd_help() -> int:
    print(
        """plan-exec - Execute a compiled active plan (agent performs real work)

Usage:
  plan-exec
  plan-exec help
  plan-exec validate

Deterministic behavior:
- Validates `.plan/active/` schemas/invariants
- If the plan is terminal (all tasks complete/deferred), archives it to `.plan/archive/<id>/`
- Otherwise prints the current in_progress task path for the agent to execute

Note: This tool does not do the work for you. The agent is responsible for implementation.
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

    print("ok: plan-exec CLI is runnable")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="plan-exec", add_help=False)
    parser.add_argument("command", nargs="?", help="help or validate")
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.command == "help":
        return cmd_help()
    if args.command == "validate":
        return cmd_validate()
    if args.command not in (None, ""):
        print(f"error: unknown command '{args.command}'", file=sys.stderr)
        return 1

    if not ACTIVE_DIR.exists():
        print(f"error: missing active plan directory: {ACTIVE_DIR}", file=sys.stderr)
        print("run plan-create first", file=sys.stderr)
        return 1

    # Keep derived status surfaces in sync deterministically.
    sync_derived_state()

    errors = validate_active_plan()
    if errors:
        print(f"error: active plan validation failed ({len(errors)} issues)", file=sys.stderr)
        for e in errors[:200]:
            print(f"  - {e}", file=sys.stderr)
        return 1

    if is_terminal():
        archived = archive_active_plan()
        print(f"archived: {archived}")
        return 0

    try:
        cur = ensure_one_in_progress_task()
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    if cur is None:
        print("error: no pending task available (unexpected non-terminal)", file=sys.stderr)
        return 1

    path, fm = cur
    print(f"active_task: {path}")
    print(f"title: {fm.get('title', '')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
