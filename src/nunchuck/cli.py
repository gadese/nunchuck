import argparse
import json
from pathlib import Path

from .installer import install_pack, uninstall_pack
from .packs import discover_packs
from .validation import format_human, format_json, validate_target


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="nunchuck")

    sub = parser.add_subparsers(dest="command", required=True)

    list_p = sub.add_parser("list")
    list_p.add_argument("--root", default=".")
    list_p.add_argument("--json", action="store_true")

    validate_p = sub.add_parser("validate")
    validate_p.add_argument("target")
    validate_p.add_argument("--json", action="store_true")

    install_p = sub.add_parser("install")
    install_p.add_argument("source")
    install_p.add_argument("--project", default=".")

    uninstall_p = sub.add_parser("uninstall")
    uninstall_p.add_argument("name")
    uninstall_p.add_argument("--project", default=".")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "list":
        packs = discover_packs(Path(args.root))
        if args.json:
            payload = [
                {"name": p.name, "version": p.version, "path": str(p.root)}
                for p in packs
            ]
            print(json.dumps(payload, indent=2, sort_keys=True))
        else:
            if not packs:
                print("No packs found.")
            else:
                for p in packs:
                    print(f"{p.name}\t{p.version}\t{p.root}")
        return 0

    if args.command == "validate":
        code, report = validate_target(Path(args.target))
        if args.json:
            print(format_json(report), end="")
        else:
            print(format_human(report), end="")
        return code

    if args.command == "install":
        result = install_pack(Path(args.source), Path(args.project))
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    if args.command == "uninstall":
        result = uninstall_pack(args.name, Path(args.project))
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0

    return 2


def _entry_point():
    """Entry point for the nunchuck CLI."""
    import sys
    sys.exit(main())
