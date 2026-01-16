#!/usr/bin/env python3

import importlib.util
import sys


def cmd_help() -> int:
    print(
        """plan-exec - Execute plan tasks by performing actual work

Commands:
  help
  validate

This skill is primarily procedure-driven. Refer to the documents in metadata.references for the canonical execution path.
"""
    )
    return 0


def cmd_validate() -> int:
    if importlib.util.find_spec("yaml") is None:
        print("error: missing dependency: pyyaml", file=sys.stderr)
        return 1

    print("ok: plan-exec CLI is runnable")
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
