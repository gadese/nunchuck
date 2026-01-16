"""Parse task files with YAML frontmatter."""

import re
from pathlib import Path
from typing import Any

import yaml


FRONTMATTER_PATTERN = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_task_file(path: Path) -> tuple[dict[str, Any], str]:
    content = path.read_text(encoding="utf-8")
    return parse_task_content(content)


def parse_task_content(content: str) -> tuple[dict[str, Any], str]:
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return {}, content

    frontmatter_str = match.group(1)
    body = content[match.end() :]

    try:
        frontmatter = yaml.safe_load(frontmatter_str) or {}
    except yaml.YAMLError:
        frontmatter = {}

    return frontmatter, body


def serialize_task(frontmatter: dict[str, Any], body: str) -> str:
    fm_str = yaml.dump(
        frontmatter,
        default_flow_style=False,
        allow_unicode=True,
        sort_keys=False,
    )
    return f"---\n{fm_str}---\n\n{body.lstrip()}"


def get_tasks_dir() -> Path:
    return Path(".tasks")


def get_active_file() -> Path:
    return get_tasks_dir() / ".active"


def get_task_path(task_id: str) -> Path:
    return get_tasks_dir() / f"{task_id}.md"


def list_task_files() -> list[Path]:
    tasks_dir = get_tasks_dir()
    if not tasks_dir.exists():
        return []
    return sorted(tasks_dir.glob("*.md"))


def read_active_task() -> str | None:
    active_file = get_active_file()
    if not active_file.exists():
        return None
    content = active_file.read_text(encoding="utf-8").strip()
    return content if content else None


def write_active_task(task_id: str | None) -> None:
    active_file = get_active_file()
    if task_id is None:
        if active_file.exists():
            active_file.unlink()
    else:
        active_file.write_text(task_id + "\n", encoding="utf-8")
