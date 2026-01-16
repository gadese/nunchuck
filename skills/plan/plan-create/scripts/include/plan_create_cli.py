#!/usr/bin/env python3

import argparse
import importlib.util
import sys

from plan_parse import clean_plan, init_plan, next_plan_number, plan_exists


def cmd_help() -> int:
    print(
        """plan-create - Create a new plan skeleton in .plan/<N>/

Usage:
  plan-create [N] [--title TITLE] [--force]
  plan-create help
  plan-create validate

Creates:
  .plan/<N>/plan.md
  .plan/<N>/a/index.md
  .plan/<N>/a/i.md

If N is omitted, uses the next available plan number.
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

    print("ok: plan-create CLI is runnable")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="plan-create", add_help=False)
    parser.add_argument("command_or_plan", nargs="?", help="help, validate, or plan number")
    parser.add_argument("--title", help="Plan title")
    parser.add_argument("--force", action="store_true", help="Overwrite existing plan")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command_or_plan is None:
        plan_n = next_plan_number()
    elif args.command_or_plan == "help":
        return cmd_help()
    elif args.command_or_plan == "validate":
        return cmd_validate()
    else:
        try:
            plan_n = int(args.command_or_plan)
        except ValueError:
            print(f"error: expected plan number, got '{args.command_or_plan}'", file=sys.stderr)
            return 1

        if plan_n <= 0:
            print("error: plan number must be > 0", file=sys.stderr)
            return 1

    if plan_exists(plan_n) and not args.force:
        print(f"error: plan {plan_n} already exists", file=sys.stderr)
        print("use --force to overwrite", file=sys.stderr)
        return 1

    if plan_exists(plan_n) and args.force:
        clean_plan(plan_n)

    path = init_plan(plan_n, args.title or "")
    print(f"created: {path}")
    print("  plan.md")
    print("  a/index.md")
    print("  a/i.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
