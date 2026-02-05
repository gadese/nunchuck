#!/usr/bin/env python3

import argparse
import importlib.util
import sys

from plan_parse import ACTIVE_DIR, ACTIVE_INTENT_PATH, compile_active_plan, validate_active_plan


def cmd_help() -> int:
    print(
        """plan-create - Compile .plan/active.yaml into .plan/active/

Usage:
  plan-create [--force]
  plan-create help
  plan-create validate

Creates/overwrites:
  .plan/active/plan.md
  .plan/active/<letter>/index.md
  .plan/active/<letter>/<roman>.md

Precondition:
  .plan/active.yaml exists and is status: ready (use plan-discuss).
"""
    )
    return 0


def cmd_validate() -> int:
    errors: list[str] = []

    if importlib.util.find_spec("yaml") is None:
        errors.append("missing dependency: pyyaml")
    if importlib.util.find_spec("jsonschema") is None:
        errors.append("missing dependency: jsonschema")

    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    # Validate that required schemas are present (schema-first design).
    from plan_parse import ROOT_SCHEMA_PATH, SUBPLAN_SCHEMA_PATH, TASK_SCHEMA_PATH

    missing: list[str] = []
    for p in [ROOT_SCHEMA_PATH, SUBPLAN_SCHEMA_PATH, TASK_SCHEMA_PATH]:
        if not p.exists():
            missing.append(str(p))
    if missing:
        for p in missing:
            print(f"error: missing schema: {p}", file=sys.stderr)
        return 1

    print("ok: plan-create CLI is runnable")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="plan-create", add_help=False)
    parser.add_argument("--force", action="store_true", help="Overwrite existing plan")
    return parser


def main() -> int:
    parser = build_parser()
    args, unknown = parser.parse_known_args()

    if unknown and unknown[0] == "help":
        return cmd_help()
    if unknown and unknown[0] == "validate":
        return cmd_validate()

    if not ACTIVE_INTENT_PATH.exists():
        print(f"error: missing plan intent: {ACTIVE_INTENT_PATH}", file=sys.stderr)
        print("run plan-discuss first", file=sys.stderr)
        return 1

    try:
        out_dir = compile_active_plan(overwrite=args.force)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 1

    errors = validate_active_plan()
    if errors:
        print(f"error: compiled plan failed validation ({len(errors)} issues)", file=sys.stderr)
        for er in errors:
            print(f"  - {er}", file=sys.stderr)
        return 1

    print(f"created: {out_dir}")
    print(f"  {ACTIVE_DIR / 'plan.md'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
