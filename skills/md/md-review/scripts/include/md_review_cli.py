#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path


def iter_markdown_files(target: Path) -> list[Path]:
    if target.is_dir():
        return sorted([p for p in target.glob("*.md") if p.is_file()])
    return [target]


def lint_file(path: Path) -> list[tuple[int, str]]:
    issues: list[tuple[int, str]] = []
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")

    blank_run = 0
    for i, line in enumerate(lines, 1):
        if line.rstrip() != line:
            issues.append((i, "trailing whitespace"))

        if line.strip() == "":
            blank_run += 1
            if blank_run >= 3:
                issues.append((i, "multiple consecutive blank lines"))
        else:
            blank_run = 0

        if line.startswith("#") and line != "#":
            if not (
                line.startswith("# ")
                or line.startswith("## ")
                or line.startswith("### ")
                or line.startswith("#### ")
                or line.startswith("##### ")
                or line.startswith("###### ")
            ):
                issues.append((i, "heading missing space after #"))

    return issues


def cmd_help() -> int:
    print(
        """md-review - Agent review for markdown quality and structure

Usage:
  md-review <file|dir>
  md-review help
  md-review validate

Behavior:
- Runs deterministic lint checks on the target (read-only)
- Prints lint findings for use by the agent during review
"""
    )
    return 0


def cmd_validate() -> int:
    print("ok: md-review CLI is runnable")
    return 0


def cmd_run(target_str: str) -> int:
    target = Path(target_str)
    if not target.exists():
        print(f"error: '{target_str}' not found", file=sys.stderr)
        return 1

    files = iter_markdown_files(target)
    if not files:
        print("no markdown files found")
        return 0

    total_issues = 0
    for f in files:
        issues = lint_file(f)
        if issues:
            for line_no, msg in issues[:50]:
                print(f"{f}:{line_no} — {msg}")
            if len(issues) > 50:
                print(f"{f} — ... and {len(issues) - 50} more")
            total_issues += len(issues)

    if total_issues > 0:
        print(f"found {total_issues} issues")
        return 1

    print(f"lint passed: {len(files)} files checked")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(prog="md-review", add_help=False)
    parser.add_argument("command_or_target", nargs="?")
    args = parser.parse_args()

    if args.command_or_target in (None, "help"):
        return cmd_help()

    if args.command_or_target == "validate":
        return cmd_validate()

    return cmd_run(args.command_or_target)


if __name__ == "__main__":
    sys.exit(main())
