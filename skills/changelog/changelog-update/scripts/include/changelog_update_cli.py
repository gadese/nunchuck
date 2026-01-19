#!/usr/bin/env python3
"""Deterministically add an entry to [Unreleased]."""

from __future__ import annotations

import argparse
import sys

from changelog_parse import (
    CANONICAL_CATEGORIES,
    add_entry_to_changelog,
    has_duplicate_entry,
    locate_changelog,
    parse_changelog,
)


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="changelog-update",
        description="Add a curated entry to the [Unreleased] section.",
    )
    parser.add_argument("category", help="One of: Added, Changed, Deprecated, Removed, Fixed, Security")
    parser.add_argument("entry", help="Entry text (quote it)")
    args = parser.parse_args()

    category = args.category.capitalize()
    if category not in CANONICAL_CATEGORIES:
        print(f"error: invalid category '{category}'", file=sys.stderr)
        print(f"valid categories: {', '.join(CANONICAL_CATEGORIES)}", file=sys.stderr)
        return 1

    path = locate_changelog()
    if path is None:
        print("error: changelog not found", file=sys.stderr)
        print("run changelog-init first", file=sys.stderr)
        return 1

    data = parse_changelog(path)
    if has_duplicate_entry(data, args.entry, category):
        print("warning: duplicate entry detected, skipping", file=sys.stderr)
        return 0

    if add_entry_to_changelog(path, category, args.entry):
        print(f"added to [{category}]: {args.entry}")
        return 0

    print(f"error: could not add entry (missing {category} section?)", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
