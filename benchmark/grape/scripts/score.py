#!/usr/bin/env python3
import json
from pathlib import Path


def _parse_usage(log_path: Path) -> dict:
    usage = {}
    if not log_path.exists():
        return usage
    for line in log_path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = line.strip()
        if not line or not (line.startswith("{") and line.endswith("}")):
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            if "usage" in data and isinstance(data["usage"], dict):
                usage.update(data["usage"])
            for key in ("prompt_tokens", "completion_tokens", "total_tokens", "context_remaining", "context_left"):
                if key in data and isinstance(data[key], int):
                    usage[key] = data[key]
    return usage

runs_dir = Path("benchmark/grape/runs")
results = []
for path in runs_dir.glob("*/results.json"):
    try:
        results.append(json.loads(path.read_text()))
    except Exception:
        continue

if not results:
    print("no results")
    raise SystemExit(0)

# Aggregate by task+mode
summary = {}
for r in results:
    key = (r.get("task"), r.get("mode"))
    entry = summary.setdefault(
        key,
        {
            "runs": 0,
            "durations": [],
            "passes": 0,
            "fails": 0,
            "test_passes": 0,
            "test_fails": 0,
            "clean_passes": 0,
            "clean_fails": 0,
            "files_changed": [],
            "insertions": [],
            "deletions": [],
            "tokens": [],
            "context_left": [],
        },
    )
    entry["runs"] += 1
    if isinstance(r.get("duration_sec"), int):
        entry["durations"].append(r["duration_sec"])
    if r.get("check_status") == "pass":
        entry["passes"] += 1
    elif r.get("check_status") == "fail":
        entry["fails"] += 1
    if r.get("test_status") == "pass":
        entry["test_passes"] += 1
    elif r.get("test_status") == "fail":
        entry["test_fails"] += 1
    if r.get("clean_status") == "pass":
        entry["clean_passes"] += 1
    elif r.get("clean_status") == "fail":
        entry["clean_fails"] += 1
    if isinstance(r.get("files_changed"), int):
        entry["files_changed"].append(r["files_changed"])
    if isinstance(r.get("insertions"), int):
        entry["insertions"].append(r["insertions"])
    if isinstance(r.get("deletions"), int):
        entry["deletions"].append(r["deletions"])

    run_dir = runs_dir / str(r.get("run_id", ""))
    log_name = "grape.out" if r.get("mode") == "grape" else "baseline.out"
    usage = _parse_usage(run_dir / "logs" / log_name)
    total_tokens = usage.get("total_tokens")
    if isinstance(total_tokens, int):
        entry["tokens"].append(total_tokens)
    context_left = usage.get("context_remaining") or usage.get("context_left")
    if isinstance(context_left, int):
        entry["context_left"].append(context_left)

print(
    "task,mode,runs,avg_sec,clean_pass,clean_fail,check_pass,check_fail,test_pass,test_fail,avg_files,avg_insertions,avg_deletions,avg_tokens,avg_context_left"
)
for (task, mode), entry in sorted(summary.items()):
    avg = sum(entry["durations"]) / len(entry["durations"]) if entry["durations"] else 0.0
    avg_tokens = sum(entry["tokens"]) / len(entry["tokens"]) if entry["tokens"] else 0.0
    avg_context = sum(entry["context_left"]) / len(entry["context_left"]) if entry["context_left"] else 0.0
    avg_files = sum(entry["files_changed"]) / len(entry["files_changed"]) if entry["files_changed"] else 0.0
    avg_ins = sum(entry["insertions"]) / len(entry["insertions"]) if entry["insertions"] else 0.0
    avg_del = sum(entry["deletions"]) / len(entry["deletions"]) if entry["deletions"] else 0.0
    print(
        f"{task},{mode},{entry['runs']},{avg:.2f},{entry['clean_passes']},{entry['clean_fails']},{entry['passes']},{entry['fails']},{entry['test_passes']},{entry['test_fails']},{avg_files:.1f},{avg_ins:.1f},{avg_del:.1f},{avg_tokens:.1f},{avg_context:.1f}"
    )
