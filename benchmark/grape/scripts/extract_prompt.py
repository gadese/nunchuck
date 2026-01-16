#!/usr/bin/env python3
import re
import sys
from typing import Optional
from pathlib import Path

if len(sys.argv) != 3:
    print("usage: extract_prompt.py <task-file> <section>", file=sys.stderr)
    sys.exit(2)

path = Path(sys.argv[1])
section = sys.argv[2].strip().lower()
text = path.read_text(encoding="utf-8")

section_map = {
    "baseline": "Baseline Prompt",
    "grape": "Grape Prompt",
    "check": "Check Command",
    "check-command": "Check Command",
    "test": "Test Command",
    "test-command": "Test Command",
    "clean": "Clean Command",
    "clean-command": "Clean Command",
    "constraints": "Constraints",
}

def extract_block(label: str) -> Optional[str]:
    pattern = rf"## {re.escape(label)}\n```[a-zA-Z]*\n(.*?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    if not match:
        return None
    return match.group(1).strip()

label = section_map.get(section, section.title())
block = extract_block(label)
if block is None and section in {"baseline", "grape"}:
    # Backward compatibility with older task templates.
    alt_label = "Baseline" if section == "baseline" else "Grape"
    block = extract_block(alt_label)

if section in {"baseline", "grape"}:
    if block is None:
        print(f"error: prompt section not found: {section}", file=sys.stderr)
        sys.exit(2)
    constraints = extract_block("Constraints")
    if constraints:
        block = f"{block}\n\nConstraints:\n{constraints}"
    print(block)
    sys.exit(0)

if block is None:
    print(f"error: prompt section not found: {section}", file=sys.stderr)
    sys.exit(2)

print(block)
