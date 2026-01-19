#!/usr/bin/env python3
"""Show commits since the latest git tag as a suggestion surface."""

from __future__ import annotations

from changelog_parse import get_commits_since_tag, get_latest_tag


def main() -> int:
    tag = get_latest_tag()
    commits = get_commits_since_tag(tag)

    if tag:
        print(f"commits since {tag}:")
    else:
        print("recent commits (no tags found):")

    if not commits:
        print("  (none)")
        return 0

    for commit in commits[:20]:
        print(f"  - {commit}")

    if len(commits) > 20:
        print(f"  ... and {len(commits) - 20} more")

    print("\nCurate entries before adding them to CHANGELOG.md.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
