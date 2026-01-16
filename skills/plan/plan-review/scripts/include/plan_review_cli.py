#!/usr/bin/env python3

import importlib.util
import sys


def cmd_help() -> int:
    print(
        """plan-review - Review a completed plan for gaps and produce an assessment

Commands:
  help
  validate

This skill is primarily procedure-driven. Refer to the documents in metadata.references for the canonical review path.
"""
    )
    return 0


def cmd_validate() -> int:
    if importlib.util.find_spec("yaml") is None:
        print("error: missing dependency: pyyaml", file=sys.stderr)
        return 1

    print("ok: plan-review CLI is runnable")
    return 0


def main() -> int:
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"

    if cmd == "help":
        return cmd_help()
    if cmd == "validate":
        return cmd_validate()

    print(f"error: unknown command '{cmd}'", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
