from __future__ import annotations

from pathlib import Path
from typing import Any


class FrontmatterError(Exception):
    pass


def _split_frontmatter(text: str) -> str:
    if not text.startswith("---"):
        raise FrontmatterError("Missing frontmatter start delimiter")

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise FrontmatterError("Missing frontmatter end delimiter")

    return parts[1].strip("\n")


def read_frontmatter(path: Path) -> dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    fm = _split_frontmatter(raw)
    return parse_simple_yaml(fm)


def parse_simple_yaml(raw: str) -> dict[str, Any]:
    """Parse a restricted YAML subset used by this repo's frontmatter.

    Supported:
    - key: value
    - key: (starts nested map)
    - key: > or key: | (folded/literal strings)
    - lists: key: [not supported]; use indented - items
    - nested dict/list via indentation

    This is not a general YAML parser.
    """

    lines = [ln.rstrip("\n") for ln in raw.splitlines()]

    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(0, root)]

    def current_container(indent: int) -> Any:
        while stack and indent < stack[-1][0]:
            stack.pop()
        return stack[-1][1]

    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue

        indent = len(line) - len(line.lstrip(" "))
        container = current_container(indent)
        stripped = line.strip()

        if stripped.startswith("- "):
            if not isinstance(container, list):
                raise FrontmatterError(f"List item found but current container is not a list: {line}")
            item = stripped[2:].strip()
            container.append(_coerce_scalar(item))
            i += 1
            continue

        if ":" not in stripped:
            raise FrontmatterError(f"Invalid line (expected key: value): {line}")

        key, _, value = stripped.partition(":")
        key = key.strip()
        value = value.strip()

        if value in {">", "|"}:
            # capture indented block
            block_indent = None
            block_lines: list[str] = []
            j = i + 1
            while j < len(lines):
                nxt = lines[j]
                if not nxt.strip():
                    block_lines.append("")
                    j += 1
                    continue
                nxt_indent = len(nxt) - len(nxt.lstrip(" "))
                if nxt_indent <= indent:
                    break
                if block_indent is None:
                    block_indent = nxt_indent
                block_lines.append(nxt[block_indent:])
                j += 1
            text_value = "\n".join(block_lines).strip("\n")
            if isinstance(container, dict):
                container[key] = text_value
            else:
                raise FrontmatterError("Cannot set key on non-dict container")
            i = j
            continue

        if value == "":
            # Start nested structure; decide list vs dict by lookahead
            j = i + 1
            next_nonempty = None
            while j < len(lines):
                if lines[j].strip() and not lines[j].lstrip().startswith("#"):
                    next_nonempty = lines[j]
                    break
                j += 1

            new_container: Any = {}
            if next_nonempty is not None:
                nxt_indent = len(next_nonempty) - len(next_nonempty.lstrip(" "))
                if nxt_indent > indent and next_nonempty.strip().startswith("- "):
                    new_container = []

            if isinstance(container, dict):
                container[key] = new_container
            else:
                raise FrontmatterError("Cannot set key on non-dict container")

            stack.append((indent + 1, new_container))
            i += 1
            continue

        if isinstance(container, dict):
            container[key] = _coerce_scalar(value)
        else:
            raise FrontmatterError("Cannot set key on non-dict container")

        i += 1

    return root


def _coerce_scalar(value: str) -> Any:
    v = value.strip().strip('"').strip("'")
    if v == "[]":
        return []
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        if not inner:
            return []
        return [part.strip().strip('"').strip("'") for part in inner.split(",")]
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    if v.isdigit():
        return int(v)
    return v
