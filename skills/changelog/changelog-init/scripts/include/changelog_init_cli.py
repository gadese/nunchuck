#!/usr/bin/env python3
"""Deterministic init for CHANGELOG.md."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from changelog_parse import get_remote_url, get_repo_root


def main() -> int:
    parser = argparse.ArgumentParser(
        prog="changelog-init",
        description="Create a canonical CHANGELOG.md from template.",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing CHANGELOG.md")
    args = parser.parse_args()

    root = get_repo_root() or Path.cwd()
    target = root / "CHANGELOG.md"

    if target.exists() and not args.force:
        print(f"error: {target} already exists", file=sys.stderr)
        print("use --force to overwrite", file=sys.stderr)
        return 1

    skill_root = Path(__file__).resolve().parents[2]
    template = skill_root / "assets" / "templates" / "CHANGELOG.template.md"

    if not template.exists():
        print(f"error: template not found at {template}", file=sys.stderr)
        return 1

    content = template.read_text(encoding="utf-8")

    remote_url = get_remote_url()
    if remote_url:
        content = content.replace("https://github.com/OWNER/REPO", remote_url)

    target.write_text(content, encoding="utf-8")
    print(f"created: {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
