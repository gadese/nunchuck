#!/usr/bin/env python3

import argparse
import json
import sys
from pathlib import Path


def cmd_help() -> int:
    print(
        """md-merge - Merge markdown chunks back into a single document

Usage:
  md-merge <chunks_dir> [--out <file>] [--force] [--dry-run]
  md-merge help
  md-merge validate

Notes:
- Reads chunks from <chunks_dir>.
- Uses .SPLIT.json if present for ordering; otherwise uses file order.
- Converts chunk H1 headings back to H2.
"""
    )
    return 0


def cmd_validate() -> int:
    print("ok: md-merge CLI is runnable")
    return 0


def merge_chunks(dir_path: str, out: str | None, force: bool, dry_run: bool) -> int:
    chunk_dir = Path(dir_path)
    if not chunk_dir.exists():
        print(f"error: directory '{dir_path}' not found", file=sys.stderr)
        return 1

    manifest_path = chunk_dir / ".SPLIT.json"
    if not manifest_path.exists():
        chunks = sorted(chunk_dir.glob("[0-9][0-9]_*.md"))
    else:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        chunks = [chunk_dir / entry["filename"] for entry in manifest.get("files", [])]

    if not chunks:
        print("error: no chunks found to merge", file=sys.stderr)
        return 1

    out_file = out or str(chunk_dir.parent / f"{chunk_dir.name}_merged.md")
    out_path = Path(out_file)

    if out_path.exists() and not force:
        print(f"error: '{out_path}' already exists. Use --force to overwrite.", file=sys.stderr)
        return 1

    if dry_run:
        print(f"would merge {len(chunks)} chunks to {out_path}")
        for c in chunks:
            print(f"  - {c.name}")
        return 0

    merged_parts: list[str] = []
    for chunk in chunks:
        if not chunk.exists():
            print(f"warning: chunk '{chunk}' not found, skipping", file=sys.stderr)
            continue

        text = chunk.read_text(encoding="utf-8")
        lines = text.split("\n")
        converted: list[str] = []
        for line in lines:
            if line.startswith("# ") and not line.startswith("## "):
                converted.append("## " + line[2:])
            else:
                converted.append(line)

        merged_parts.append("\n".join(converted))

    out_path.write_text("\n\n".join(merged_parts), encoding="utf-8")
    print(f"merged {len(chunks)} chunks to {out_path}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="md-merge", add_help=False)
    parser.add_argument("command_or_dir", nargs="?")
    parser.add_argument("--out")
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command_or_dir in (None, "help"):
        return cmd_help()

    if args.command_or_dir == "validate":
        return cmd_validate()

    return merge_chunks(args.command_or_dir, out=args.out, force=args.force, dry_run=args.dry_run)


if __name__ == "__main__":
    sys.exit(main())
