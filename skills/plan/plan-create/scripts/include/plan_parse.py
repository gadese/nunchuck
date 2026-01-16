"""Parse and manage plan artifacts."""

from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml


PLAN_DIR = Path(".plan")
VALID_STATUSES = ("pending", "in_progress", "complete", "abandoned", "blocked")
ROMAN_NUMERALS = ["i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"]


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def to_rfc3339(dt: datetime) -> str:
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def ensure_plan_dir() -> None:
    PLAN_DIR.mkdir(exist_ok=True)


def list_plans() -> list[int]:
    if not PLAN_DIR.exists():
        return []
    plans: list[int] = []
    for d in PLAN_DIR.iterdir():
        if d.is_dir() and d.name.isdigit():
            plans.append(int(d.name))
    return sorted(plans)


def next_plan_number() -> int:
    plans = list_plans()
    if not plans:
        return 1
    return max(plans) + 1


def plan_path(n: int) -> Path:
    return PLAN_DIR / str(n)


def plan_exists(n: int) -> bool:
    return plan_path(n).exists()


def root_plan_path(n: int) -> Path:
    return plan_path(n) / "plan.md"


def parse_frontmatter(content: str) -> tuple[dict[str, Any], str]:
    if not content.startswith("---"):
        return {}, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}, content

    try:
        fm = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        fm = {}

    body = parts[2].lstrip("\n")
    return fm, body


def read_plan_frontmatter(n: int) -> dict[str, Any] | None:
    path = root_plan_path(n)
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(content)
    return fm


def list_subplans(n: int) -> list[str]:
    ppath = plan_path(n)
    if not ppath.exists():
        return []
    subplans: list[str] = []
    for d in ppath.iterdir():
        if d.is_dir() and len(d.name) == 1 and d.name.isalpha():
            subplans.append(d.name)
    return sorted(subplans)


def list_tasks(n: int, letter: str) -> list[str]:
    subplan_path = plan_path(n) / letter
    if not subplan_path.exists():
        return []
    tasks: list[str] = []
    for f in subplan_path.glob("*.md"):
        name = f.stem.lower()
        if name in ROMAN_NUMERALS:
            tasks.append(name)
    return sorted(tasks, key=lambda x: ROMAN_NUMERALS.index(x) if x in ROMAN_NUMERALS else 99)


def task_path(n: int, letter: str, roman: str) -> Path:
    return plan_path(n) / letter / f"{roman}.md"


def read_task_frontmatter(n: int, letter: str, roman: str) -> dict[str, Any] | None:
    path = task_path(n, letter, roman)
    if not path.exists():
        return None
    content = path.read_text(encoding="utf-8")
    fm, _ = parse_frontmatter(content)
    return fm


def get_plan_status(n: int) -> dict[str, Any]:
    if not plan_exists(n):
        return {"error": f"plan {n} does not exist"}

    root_fm = read_plan_frontmatter(n)
    status: dict[str, Any] = {
        "plan": n,
        "status": root_fm.get("status", "pending") if root_fm else "pending",
        "title": root_fm.get("title", "") if root_fm else "",
        "subplans": [],
    }

    for letter in list_subplans(n):
        subplan: dict[str, Any] = {"letter": letter, "tasks": []}
        for roman in list_tasks(n, letter):
            task_fm = read_task_frontmatter(n, letter, roman)
            task_status = task_fm.get("status", "pending") if task_fm else "pending"
            subplan["tasks"].append({"roman": roman, "status": task_status})
        status["subplans"].append(subplan)

    return status


def init_plan(n: int, title: str = "") -> Path:
    ppath = plan_path(n)
    ppath.mkdir(parents=True, exist_ok=True)

    root = root_plan_path(n)
    now = to_rfc3339(now_utc())
    content = f"""---
status: pending
created_at: {now}
title: {title or f'Plan {n}'}
---

# Plan {n}

## Objective

<!-- Define the goal of this plan -->

## Success Criteria

- [ ] Criterion 1
- [ ] Criterion 2

## Sub-plan Index

- a/ — Sub-plan A
"""
    root.write_text(content, encoding="utf-8")

    (ppath / "a").mkdir(exist_ok=True)
    index_content = f"""---
status: pending
created_at: {now}
---

# Sub-plan A

## Tasks

- i — Task 1
"""
    (ppath / "a" / "index.md").write_text(index_content, encoding="utf-8")

    task_content = f"""---
status: pending
created_at: {now}
---

# Task i

## Focus

<!-- What is the specific goal? -->

## Inputs

<!-- What files/artifacts are needed? -->

## Work

1. Step 1
2. Step 2

## Output

<!-- Results go here after execution -->

## Handoff

<!-- Next step instructions go here after execution -->
"""
    (ppath / "a" / "i.md").write_text(task_content, encoding="utf-8")

    return ppath


def clean_plan(n: int) -> bool:
    ppath = plan_path(n)
    if not ppath.exists():
        return False
    import shutil

    shutil.rmtree(ppath)
    return True


def clean_all_plans() -> int:
    plans = list_plans()
    for n in plans:
        clean_plan(n)
    return len(plans)


def surface_scan(patterns: list[str] | None = None) -> list[str]:
    if patterns is None:
        patterns = ["*.md", "*.py", "*.ts", "*.js", "*.yaml", "*.yml", "*.json"]

    results: list[str] = []
    cwd = Path.cwd()

    for pattern in patterns:
        for f in cwd.rglob(pattern):
            parts = f.parts
            if any(p.startswith(".") and p not in [".plan"] for p in parts):
                continue
            if any(p in ["node_modules", "__pycache__", "venv", ".venv"] for p in parts):
                continue
            results.append(str(f.relative_to(cwd)))

    return sorted(results)
