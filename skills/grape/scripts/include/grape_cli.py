#!/usr/bin/env python3

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path


def repo_root_from_file(file_path: Path) -> Path:
    p = file_path.resolve()
    for parent in [p] + list(p.parents):
        if (parent / ".git").exists():
            return parent
    return Path.cwd().resolve()


REPO_ROOT = repo_root_from_file(Path(__file__))


def cmd_help(_: argparse.Namespace) -> int:
    print(
        """grape - AI-enabled deterministic grep (parameterized by agent judgment)\n\nCommands:\n  help                         Show this help message\n  validate                     Verify the skill is runnable (read-only)\n  scan [opts]                  Run a deterministic surface snapshot (file list + distributions)\n  grep [opts]                  Run a deterministic surface search (matches + context lines)\n  plan [opts]                  Validate/execute a compiled plan receipt (stdin or file)\n\nOptions (scan):\n  --root <path>                default: .\n  --glob <pattern>             repeatable (rg -g)\n  --exclude <pattern>          repeatable (rg -g '!pat')\n  --snapshot-max-files <n>     default: 20000\n  --hidden                     include hidden files\n  --follow                     follow symlinks\n  --no-ignore                  do not respect ignore files\n  --no-ignore-vcs              do not respect VCS ignore files\n  --no-ignore-global           do not respect global ignore files\n\nOptions (grep):\n  --root <path>                default: .\n  --pattern <text>             repeatable (search terms)\n  --glob <pattern>             repeatable (rg -g)\n  --exclude <pattern>          repeatable (rg -g '!pat')\n  --mode <fixed|regex>         default: fixed\n  --case <sensitive|insensitive|smart>  default: smart\n  --context <n>                default: 0\n  --format <auto|human|jsonl>  default: auto\n  --strategy <single|parallel|cascade>  default: single\n  --max-probes <n>             default: 8\n  --max-derived <n>            default: 12\n  --snapshot-max-files <n>     default: 20000\n  --hidden                     include hidden files\n  --follow                     follow symlinks\n  --no-ignore                  do not respect ignore files\n  --no-ignore-vcs              do not respect VCS ignore files\n  --no-ignore-global           do not respect global ignore files\n  --max-lines <n>              default: 500\n\nOptions (plan):\n  --stdin                      read compiled plan JSON from stdin\n  --plan <path>                read compiled plan JSON from a file\n\nUsage:\n  grape grep --root . --pattern "foo" --glob "src/**/*.py"\n"""
    )
    return 0


def cmd_validate(_: argparse.Namespace) -> int:
    errors: list[str] = []

    if shutil.which("rg") is None:
        errors.append("missing command: rg (ripgrep)")

    if errors:
        for e in errors:
            print(f"error: {e}", file=sys.stderr)
        return 1

    print("ok: grape CLI is runnable")
    return 0


def _resolve_root(root: str) -> Path:
    p = Path(root)
    if p.is_absolute():
        return p.resolve()
    return (REPO_ROOT / p).resolve()


def _sha256_intent(intent_doc: dict) -> str:
    normalized = json.dumps(intent_doc, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    h = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
    return f"sha256:{h}"


def _emit_jsonl(obj: dict) -> None:
    print(json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


def _is_match_line(line: str) -> bool:
    # Expected rg line format: path:line:content
    parts = line.split(":", 2)
    if len(parts) < 3:
        return False
    _, line_no, _ = parts
    return line_no.isdigit()


def cmd_grep(args: argparse.Namespace) -> int:
    root = args.root
    patterns: list[str] = args.pattern or []
    globs: list[str] = args.glob or []
    excludes: list[str] = args.exclude or []
    mode = args.mode
    case = args.case
    context = args.context
    fmt = args.format
    strategy = args.strategy
    max_probes = args.max_probes
    max_derived = args.max_derived
    snapshot_max_files = args.snapshot_max_files
    hidden = args.hidden
    follow = args.follow
    no_ignore = args.no_ignore
    no_ignore_vcs = args.no_ignore_vcs
    no_ignore_global = args.no_ignore_global
    max_lines = args.max_lines

    if not patterns:
        print("error: at least one --pattern is required", file=sys.stderr)
        return 2

    root_path = _resolve_root(root)

    argv: list[str] = [
        "rg",
        "-n",
        "--color",
        "never",
        "--no-heading",
        "--with-filename",
        "--line-number",
        "--sort",
        "path",
    ]

    if hidden:
        argv.append("--hidden")
    if follow:
        argv.append("--follow")
    if no_ignore:
        argv.append("--no-ignore")
    if no_ignore_vcs:
        argv.append("--no-ignore-vcs")
    if no_ignore_global:
        argv.append("--no-ignore-global")

    if mode == "fixed":
        argv.append("-F")

    if case == "insensitive":
        argv.append("-i")
    elif case == "smart":
        argv.append("-S")

    if context and context > 0:
        argv.extend(["-C", str(context)])

    for g in globs:
        argv.extend(["-g", g])

    for e in excludes:
        argv.extend(["-g", f"!{e}"])

    for p in patterns:
        argv.extend(["-e", p])

    argv.append(str(root_path))

    param_block = {
        "root": root,
        "patterns": patterns,
        "globs": globs,
        "excludes": excludes,
        "mode": mode,
        "case": case,
        "context": context,
        "format": fmt,
        "strategy": strategy,
        "max_probes": max_probes,
        "max_derived": max_derived,
        "snapshot_max_files": snapshot_max_files,
        "policy": {
            "hidden": hidden,
            "follow": follow,
            "ignore": {
                "no_ignore": no_ignore,
                "no_ignore_vcs": no_ignore_vcs,
                "no_ignore_global": no_ignore_global,
            },
        },
        "max_lines": max_lines,
        "tool": "rg",
        "argv": argv,
    }

    if fmt == "jsonl":
        _emit_jsonl({"kind": "param_block", "param_block": param_block})
    else:
        print(json.dumps(param_block, sort_keys=True))

    try:
        r = subprocess.run(argv, check=False, capture_output=True, text=True)
    except OSError as e:
        print(f"error: failed to run rg: {e}", file=sys.stderr)
        return 1

    if r.returncode not in (0, 1):
        if r.stderr:
            print(r.stderr.rstrip("\n"), file=sys.stderr)
        print(f"error: rg exited with status {r.returncode}", file=sys.stderr)
        return 1

    lines = [ln for ln in r.stdout.splitlines() if ln.strip()]
    match_lines = [ln for ln in lines if _is_match_line(ln)]
    files = sorted({ln.split(":", 1)[0] for ln in match_lines})

    truncated = False
    out_lines = lines
    if max_lines is not None and max_lines >= 0 and len(out_lines) > max_lines:
        out_lines = out_lines[:max_lines]
        truncated = True

    if fmt == "jsonl":
        _emit_jsonl({"kind": "summary", "files": len(files), "matches": len(match_lines), "truncated": truncated, "shown_lines": len(out_lines)})
        for ln in out_lines:
            _emit_jsonl({"kind": "rg_line", "line": ln})
    else:
        print(f"files: {len(files)}")
        print(f"matches: {len(match_lines)}")
        if truncated:
            print(f"truncated: true (showing first {len(out_lines)} lines)")

        for ln in out_lines:
            print(ln)

    return 0


def cmd_scan(args: argparse.Namespace) -> int:
    root = args.root
    globs: list[str] = args.glob or []
    excludes: list[str] = args.exclude or []
    snapshot_max_files = args.snapshot_max_files
    hidden = args.hidden
    follow = args.follow
    no_ignore = args.no_ignore
    no_ignore_vcs = args.no_ignore_vcs
    no_ignore_global = args.no_ignore_global

    root_path = _resolve_root(root)

    argv: list[str] = ["rg", "--files", "--sort", "path"]

    if hidden:
        argv.append("--hidden")
    if follow:
        argv.append("--follow")
    if no_ignore:
        argv.append("--no-ignore")
    if no_ignore_vcs:
        argv.append("--no-ignore-vcs")
    if no_ignore_global:
        argv.append("--no-ignore-global")

    for g in globs:
        argv.extend(["-g", g])
    for e in excludes:
        argv.extend(["-g", f"!{e}"])

    argv.append(str(root_path))

    param_block = {
        "root": root,
        "globs": globs,
        "excludes": excludes,
        "snapshot_max_files": snapshot_max_files,
        "policy": {
            "hidden": hidden,
            "follow": follow,
            "ignore": {
                "no_ignore": no_ignore,
                "no_ignore_vcs": no_ignore_vcs,
                "no_ignore_global": no_ignore_global,
            },
        },
        "tool": "rg",
        "argv": argv,
    }

    print(json.dumps(param_block, sort_keys=True))

    try:
        r = subprocess.run(argv, check=False, capture_output=True, text=True)
    except OSError as e:
        print(f"error: failed to run rg: {e}", file=sys.stderr)
        return 1

    if r.returncode not in (0, 1):
        if r.stderr:
            print(r.stderr.rstrip("\n"), file=sys.stderr)
        print(f"error: rg exited with status {r.returncode}", file=sys.stderr)
        return 1

    files = [ln for ln in r.stdout.splitlines() if ln.strip()]

    truncated = False
    shown_files = files
    if snapshot_max_files is not None and snapshot_max_files >= 0 and len(shown_files) > snapshot_max_files:
        shown_files = shown_files[:snapshot_max_files]
        truncated = True

    ext_counts: Counter[str] = Counter()
    for p in shown_files:
        suffix = Path(p).suffix.lower() or "<none>"
        ext_counts[suffix] += 1

    print(f"files: {len(files)}")
    if truncated:
        print(f"truncated: true (showing first {len(shown_files)} files)")

    for ext, count in sorted(ext_counts.items(), key=lambda kv: (-kv[1], kv[0]))[:25]:
        print(f"ext: {ext} {count}")

    for p in shown_files[:200]:
        print(p)

    return 0


def cmd_plan(args: argparse.Namespace) -> int:
    plan_path = args.plan
    use_stdin = args.stdin

    if (plan_path is None and not use_stdin) or (plan_path is not None and use_stdin):
        print("error: specify exactly one of --stdin or --plan", file=sys.stderr)
        return 2

    try:
        if use_stdin:
            raw = sys.stdin.read()
        else:
            raw = Path(plan_path).read_text(encoding="utf-8")
        doc = json.loads(raw)
    except Exception as e:
        print(f"error: failed to read/parse plan json: {e}", file=sys.stderr)
        return 2

    if doc.get("schema") != "grape_compiled_plan_v1":
        print("error: plan schema must be grape_compiled_plan_v1", file=sys.stderr)
        return 2

    intent = doc.get("intent")
    if not isinstance(intent, dict) or intent.get("schema") != "grape_intent_v1":
        print("error: plan.intent must be grape_intent_v1", file=sys.stderr)
        return 2

    expected_hash = _sha256_intent(intent)
    if doc.get("intent_hash") != expected_hash:
        print(f"error: intent_hash mismatch (expected {expected_hash})", file=sys.stderr)
        return 2

    grep_cfg = doc.get("grep")
    if not isinstance(grep_cfg, dict):
        print("error: plan.grep must be an object", file=sys.stderr)
        return 2

    required_grep_fields = [
        "root",
        "pattern",
        "glob",
        "exclude",
        "mode",
        "case",
        "context",
        "format",
        "max_lines",
        "strategy",
        "max_probes",
        "max_derived",
        "snapshot_max_files",
        "policy",
    ]
    missing = [k for k in required_grep_fields if k not in grep_cfg]
    if missing:
        print(f"error: plan.grep missing required fields: {', '.join(missing)}", file=sys.stderr)
        return 2

    if not isinstance(grep_cfg.get("pattern"), list) or not grep_cfg.get("pattern"):
        print("error: plan.grep.pattern must be a non-empty array", file=sys.stderr)
        return 2
    if not isinstance(grep_cfg.get("glob"), list):
        print("error: plan.grep.glob must be an array", file=sys.stderr)
        return 2
    if not isinstance(grep_cfg.get("exclude"), list):
        print("error: plan.grep.exclude must be an array", file=sys.stderr)
        return 2
    if not isinstance(grep_cfg.get("policy"), dict):
        print("error: plan.grep.policy must be an object", file=sys.stderr)
        return 2
    ignore_cfg = (grep_cfg.get("policy") or {}).get("ignore")
    if not isinstance(ignore_cfg, dict):
        print("error: plan.grep.policy.ignore must be an object", file=sys.stderr)
        return 2
    for k in ("no_ignore", "no_ignore_vcs", "no_ignore_global"):
        if k not in ignore_cfg:
            print(f"error: plan.grep.policy.ignore missing required field: {k}", file=sys.stderr)
            return 2

    _emit_jsonl({"kind": "compiled_plan", "plan": doc})

    grep_ns = argparse.Namespace(
        root=grep_cfg.get("root", "."),
        pattern=list(grep_cfg.get("pattern") or []),
        glob=list(grep_cfg.get("glob") or []),
        exclude=list(grep_cfg.get("exclude") or []),
        mode=grep_cfg.get("mode", "fixed"),
        case=grep_cfg.get("case", "smart"),
        context=int(grep_cfg.get("context", 0)),
        format=grep_cfg.get("format", "auto"),
        strategy=grep_cfg.get("strategy", "single"),
        max_probes=int(grep_cfg.get("max_probes", 8)),
        max_derived=int(grep_cfg.get("max_derived", 12)),
        snapshot_max_files=int(grep_cfg.get("snapshot_max_files", 20000)),
        hidden=bool(((grep_cfg.get("policy") or {}).get("hidden", False))),
        follow=bool(((grep_cfg.get("policy") or {}).get("follow", False))),
        no_ignore=bool((((grep_cfg.get("policy") or {}).get("ignore") or {}).get("no_ignore", False))),
        no_ignore_vcs=bool((((grep_cfg.get("policy") or {}).get("ignore") or {}).get("no_ignore_vcs", False))),
        no_ignore_global=bool((((grep_cfg.get("policy") or {}).get("ignore") or {}).get("no_ignore_global", False))),
        max_lines=int(grep_cfg.get("max_lines", 500)),
    )
    return cmd_grep(grep_ns)


def main() -> int:
    parser = argparse.ArgumentParser(prog="grape", add_help=False)
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("help")
    sub.add_parser("validate")

    p_scan = sub.add_parser("scan")
    p_scan.add_argument("--root", default=".")
    p_scan.add_argument("--glob", action="append")
    p_scan.add_argument("--exclude", action="append")
    p_scan.add_argument("--snapshot-max-files", type=int, default=20000)
    p_scan.add_argument("--hidden", action="store_true")
    p_scan.add_argument("--follow", action="store_true")
    p_scan.add_argument("--no-ignore", action="store_true")
    p_scan.add_argument("--no-ignore-vcs", action="store_true")
    p_scan.add_argument("--no-ignore-global", action="store_true")

    p_grep = sub.add_parser("grep")
    p_grep.add_argument("--root", default=".")
    p_grep.add_argument("--pattern", action="append")
    p_grep.add_argument("--glob", action="append")
    p_grep.add_argument("--exclude", action="append")
    p_grep.add_argument("--mode", choices=["fixed", "regex"], default="fixed")
    p_grep.add_argument(
        "--case", choices=["sensitive", "insensitive", "smart"], default="smart"
    )
    p_grep.add_argument("--context", type=int, default=0)
    p_grep.add_argument("--format", choices=["auto", "human", "jsonl"], default="auto")
    p_grep.add_argument(
        "--strategy", choices=["single", "parallel", "cascade"], default="single"
    )
    p_grep.add_argument("--max-probes", type=int, default=8)
    p_grep.add_argument("--max-derived", type=int, default=12)
    p_grep.add_argument("--snapshot-max-files", type=int, default=20000)
    p_grep.add_argument("--hidden", action="store_true")
    p_grep.add_argument("--follow", action="store_true")
    p_grep.add_argument("--no-ignore", action="store_true")
    p_grep.add_argument("--no-ignore-vcs", action="store_true")
    p_grep.add_argument("--no-ignore-global", action="store_true")
    p_grep.add_argument("--max-lines", type=int, default=500)

    p_plan = sub.add_parser("plan")
    p_plan.add_argument("--stdin", action="store_true")
    p_plan.add_argument("--plan")

    args = parser.parse_args()
    cmd = args.command or "help"

    if cmd == "help":
        return cmd_help(args)
    if cmd == "validate":
        return cmd_validate(args)
    if cmd == "scan":
        return cmd_scan(args)
    if cmd == "grep":
        return cmd_grep(args)
    if cmd == "plan":
        return cmd_plan(args)

    print(f"error: unknown command '{cmd}'", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
