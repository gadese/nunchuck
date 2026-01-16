#!/usr/bin/env python3

import argparse
import importlib.util
import sys

from plan_parse import get_plan_status, list_plans, plan_exists


def cmd_help() -> int:
    print(
        """plan-status - Show plan status from .plan/<N>/

Usage:
  plan-status [N]
  plan-status help
  plan-status validate

If N is omitted, defaults to the latest plan.
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

    print("ok: plan-status CLI is runnable")
    return 0


def print_status(n: int) -> int:
    if not plan_exists(n):
        print(f"error: plan {n} does not exist", file=sys.stderr)
        return 1

    status = get_plan_status(n)

    print(f"plan: {n}")
    print(f"status: {status.get('status', 'pending')}")
    print(f"title: {status.get('title', '')}")
    print()

    subplans = status.get("subplans", [])
    if subplans:
        print("subplans:")
        for sp in subplans:
            letter = sp["letter"]
            tasks = sp["tasks"]
            complete = sum(1 for t in tasks if t["status"] == "complete")
            total = len(tasks)
            print(f"  {letter}/ — {complete}/{total} tasks complete")
            for t in tasks:
                roman = t["roman"]
                st = t["status"]
                marker = "✓" if st == "complete" else "○" if st == "pending" else "→"
                print(f"    {marker} {roman} [{st}]")

    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="plan-status", add_help=False)
    parser.add_argument("command_or_plan", nargs="?")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command_or_plan in (None, ""):
        plans = list_plans()
        if not plans:
            print("no plans found")
            return 1
        return print_status(max(plans))

    if args.command_or_plan == "help":
        return cmd_help()

    if args.command_or_plan == "validate":
        return cmd_validate()

    try:
        n = int(args.command_or_plan)
    except ValueError:
        print(f"error: expected plan number, got '{args.command_or_plan}'", file=sys.stderr)
        return 1

    return print_status(n)


if __name__ == "__main__":
    sys.exit(main())
