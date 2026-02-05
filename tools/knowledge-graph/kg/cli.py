"""Argument parsing, dispatch, and exit codes."""

import argparse
import json
import os
import sys

from kg.core import analyze, build_graph
from kg.render import render_html, render_json, render_text
from kg.validate import validate


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="kg",
        description="Knowledge Graph analysis tool for brainstorming",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    analyze_parser = subparsers.add_parser("analyze", help="Analyze a knowledge graph")
    analyze_parser.add_argument("input", help="Path to input JSON file")
    analyze_parser.add_argument(
        "--format",
        choices=["text", "json"],
        default="text",
        dest="output_format",
        help="Output format (default: text)",
    )
    analyze_parser.add_argument(
        "--visualize",
        metavar="PATH",
        help="Generate interactive HTML visualization at PATH",
    )
    analyze_parser.add_argument(
        "--seed", type=int, default=42, help="Random seed (default: 42)"
    )
    analyze_parser.add_argument(
        "--resolution",
        type=float,
        default=1.0,
        help="Louvain resolution parameter (default: 1.0)",
    )
    analyze_parser.add_argument(
        "--gap-threshold",
        type=float,
        default=0.05,
        help="Gap detection threshold (default: 0.05)",
    )

    validate_parser = subparsers.add_parser(
        "validate", help="Validate input JSON without analyzing"
    )
    validate_parser.add_argument("input", help="Path to input JSON file")

    return parser.parse_args(argv)


def _load_json(path: str) -> dict:
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File not found: {path}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(2)


def _cmd_validate(args: argparse.Namespace) -> int:
    data = _load_json(args.input)
    errors = validate(data)
    if errors:
        print("Validation errors:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 2
    print("Input is valid.")
    return 0


def _cmd_analyze(args: argparse.Namespace) -> int:
    data = _load_json(args.input)

    errors = validate(data)
    if errors:
        print("Validation errors:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 2

    try:
        report = analyze(
            data,
            resolution=args.resolution,
            seed=args.seed,
            gap_threshold=args.gap_threshold,
        )
    except Exception as e:
        print(f"Error during analysis: {e}", file=sys.stderr)
        return 1

    if args.output_format == "json":
        print(render_json(report))
    else:
        print(render_text(report))

    if args.visualize:
        if ".." in args.visualize.split(os.sep):
            print(
                "Error: --visualize path must not contain directory traversal",
                file=sys.stderr,
            )
            return 2
        viz_path = os.path.realpath(args.visualize)
        try:
            G = build_graph(data)
            render_html(report, G, viz_path)
            print(f"Visualization saved to: {viz_path}", file=sys.stderr)
        except Exception as e:
            print(f"Warning: Visualization failed: {e}", file=sys.stderr)

    return 0


def main(argv: list[str] | None = None) -> int:
    """CLI entry point. Returns exit code."""
    args = _parse_args(argv)

    if args.command == "validate":
        return _cmd_validate(args)
    elif args.command == "analyze":
        return _cmd_analyze(args)

    return 1
