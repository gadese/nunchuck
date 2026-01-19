#!/usr/bin/env python3
"""Deterministically cut a versioned release from [Unreleased]."""

from __future__ import annotations

import argparse
import sys

from changelog_parse import locate_changelog, parse_changelog, release_changelog, today_iso


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="changelog-release",
        description="Convert [Unreleased] into a versioned release section.",
    )
    parser.add_argument("version", help="Version number (e.g., 1.2.0)")
    parser.add_argument("--date", help="Release date (YYYY-MM-DD, default: today UTC)")
    parser.add_argument("--force", action="store_true", help="Release even if [Unreleased] is empty")
    args = parser.parse_args()

    date = args.date or today_iso()
    path = locate_changelog()
    if path is None:
        print("error: changelog not found", file=sys.stderr)
        return 1

    data = parse_changelog(path)
    if not data["has_unreleased"]:
        print("error: no [Unreleased] section found", file=sys.stderr)
        return 1

    unreleased_count = sum(len(v) for v in data["unreleased_entries"].values())
    if unreleased_count == 0 and not args.force:
        print("warning: [Unreleased] section is empty", file=sys.stderr)
        print("use --force to release anyway", file=sys.stderr)
        return 1

    if not release_changelog(path, args.version, date):
        print("error: release failed", file=sys.stderr)
        return 1

    print(f"released: [{args.version}] - {date}")
    print(f"  entries: {unreleased_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
