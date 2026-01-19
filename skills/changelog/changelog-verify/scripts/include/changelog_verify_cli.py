#!/usr/bin/env python3
"""Deterministically verify changelog structure."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from changelog_parse import locate_changelog, parse_changelog


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="changelog-verify",
        description="Validate structure and hygiene of a Keep a Changelog file.",
    )
    parser.add_argument("path", nargs="?", help="Optional path to changelog (default: auto-locate)")
    args = parser.parse_args()

    path = Path(args.path) if args.path else locate_changelog()
    if path is None or not path.exists():
        print("error: changelog not found", file=sys.stderr)
        return 1

    data = parse_changelog(path)
    issues: list[str] = []

    if not data["has_header"]:
        issues.append("missing '# Changelog' header")

    if not data["has_kac_reference"]:
        issues.append("missing Keep a Changelog reference")

    if not data["has_unreleased"]:
        issues.append("missing [Unreleased] section")

    if not data["versions_descending"]:
        issues.append("versions not in descending order")

    issues.extend(data.get("issues", []))

    if issues:
        print(f"found {len(issues)} issues:")
        for issue in issues:
            print(f"  - {issue}")
        return 1

    print(f"ok: {path}")
    print(f"  versions: {len(data['versions'])}")
    print(f"  unreleased entries: {sum(len(v) for v in data['unreleased_entries'].values())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
