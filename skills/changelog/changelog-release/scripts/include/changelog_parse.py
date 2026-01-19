"""Parse and manage changelog files."""

from __future__ import annotations

import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


CANONICAL_CATEGORIES = ["Added", "Changed", "Deprecated", "Removed", "Fixed", "Security"]
DATE_PATTERN = re.compile(r"^\\d{4}-\\d{2}-\\d{2}$")
VERSION_PATTERN = re.compile(r"^\\d+\\.\\d+\\.\\d+$")
VERSION_HEADING_PATTERN = re.compile(
    r"^## \\[(\\d+\\.\\d+\\.\\d+|Unreleased)\\](?:\\s*-\\s*(\\d{4}-\\d{2}-\\d{2}))?"
)
CATEGORY_PATTERN = re.compile(r"^### (Added|Changed|Deprecated|Removed|Fixed|Security)")
ENTRY_PATTERN = re.compile(r"^- (.+)$")
LINK_REF_PATTERN = re.compile(r"^\\[([^\\]]+)\\]:\\s*(.+)$")
PR_KEY_PATTERN = re.compile(r"#(\\d+)")
ISSUE_KEY_PATTERN = re.compile(r"([A-Z]+-\\d+)")


def get_repo_root() -> Path | None:
    """Get git repository root."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--show-toplevel"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return Path(result.stdout.strip())
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def locate_changelog() -> Path | None:
    """
    Find changelog using deterministic rules:
    1. Repo root CHANGELOG.md
    2. docs/CHANGELOG.md
    3. None
    """
    root = get_repo_root() or Path.cwd()

    candidates = [
        root / "CHANGELOG.md",
        root / "docs" / "CHANGELOG.md",
    ]

    for path in candidates:
        if path.exists():
            return path

    return None


def get_remote_url() -> str | None:
    """Get git remote URL for link references."""
    try:
        result = subprocess.run(
            ["git", "remote", "get-url", "origin"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            url = result.stdout.strip()
            if url.startswith("git@"):
                url = url.replace(":", "/").replace("git@", "https://")
            if url.endswith(".git"):
                url = url[:-4]
            return url
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def get_latest_tag() -> str | None:
    """Get most recent git tag."""
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return None


def get_commits_since_tag(tag: str | None = None) -> list[str]:
    """Get commit subjects since last tag."""
    cmd = ["git", "log", "--no-merges", "--pretty=format:%s"]
    if tag:
        cmd.append(f"{tag}..HEAD")
    else:
        cmd.append("-20")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            return [line for line in result.stdout.strip().split("\\n") if line]
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass
    return []


def today_iso() -> str:
    """Get today's date in ISO format."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def parse_changelog(path: Path) -> dict[str, Any]:
    """Parse changelog into structured data."""
    content = path.read_text(encoding="utf-8")
    lines = content.split("\\n")

    result: dict[str, Any] = {
        "path": str(path),
        "has_header": False,
        "has_kac_reference": False,
        "has_unreleased": False,
        "versions": [],
        "unreleased_entries": {},
        "link_refs": {},
        "issues": [],
    }

    current_version: str | None = None
    current_category: str | None = None

    for i, line in enumerate(lines):
        line_num = i + 1

        if line.startswith("# Changelog"):
            result["has_header"] = True

        if "keep a changelog" in line.lower():
            result["has_kac_reference"] = True

        version_match = VERSION_HEADING_PATTERN.match(line)
        if version_match:
            version = version_match.group(1)
            date = version_match.group(2)

            if version == "Unreleased":
                result["has_unreleased"] = True
                current_version = "Unreleased"
            else:
                result["versions"].append({"version": version, "date": date, "line": line_num})
                current_version = version
            current_category = None
            continue

        category_match = CATEGORY_PATTERN.match(line)
        if category_match:
            current_category = category_match.group(1)
            continue

        entry_match = ENTRY_PATTERN.match(line)
        if entry_match and current_version and current_category:
            entry = entry_match.group(1)
            if current_version == "Unreleased":
                result["unreleased_entries"].setdefault(current_category, []).append(entry)

        link_match = LINK_REF_PATTERN.match(line)
        if link_match:
            result["link_refs"][link_match.group(1)] = link_match.group(2)

    if len(result["versions"]) >= 2:
        versions_ok = True
        for i in range(len(result["versions"]) - 1):
            v1 = result["versions"][i]["version"]
            v2 = result["versions"][i + 1]["version"]
            if v1 < v2:
                versions_ok = False
                result["issues"].append(
                    f"Version {v1} appears before {v2} (should be descending)"
                )
        result["versions_descending"] = versions_ok
    else:
        result["versions_descending"] = True

    return result


def extract_entry_keys(entry: str) -> set[str]:
    """Extract PR/issue keys from an entry."""
    keys = set()
    for match in PR_KEY_PATTERN.finditer(entry):
        keys.add(f"#{match.group(1)}")
    for match in ISSUE_KEY_PATTERN.finditer(entry):
        keys.add(match.group(1))
    return keys


def has_duplicate_entry(changelog_data: dict[str, Any], new_entry: str, category: str) -> bool:
    """Check if entry already exists (by exact match or key match)."""
    existing = changelog_data.get("unreleased_entries", {}).get(category, [])

    if new_entry in existing:
        return True

    new_keys = extract_entry_keys(new_entry)
    if new_keys:
        for entry in existing:
            existing_keys = extract_entry_keys(entry)
            if new_keys & existing_keys:
                return True

    return False


def add_entry_to_changelog(path: Path, category: str, entry: str) -> bool:
    """Add an entry under the specified category in [Unreleased]."""
    content = path.read_text(encoding="utf-8")
    lines = content.split("\\n")

    in_unreleased = False
    insert_line: int | None = None

    for i, line in enumerate(lines):
        if line.startswith("## [Unreleased]"):
            in_unreleased = True
            continue
        if in_unreleased and line.startswith("## ["):
            break
        if in_unreleased and line == f"### {category}":
            insert_line = i + 1
            while insert_line < len(lines) and (
                lines[insert_line].startswith("- ") or lines[insert_line].strip() == ""
            ):
                if lines[insert_line].startswith("### ") or lines[insert_line].startswith("## "):
                    break
                insert_line += 1
            break

    if insert_line is None:
        return False

    lines.insert(insert_line, f"- {entry}")
    path.write_text("\\n".join(lines), encoding="utf-8")
    return True


def release_changelog(path: Path, version: str, date: str | None = None) -> bool:
    """Transform [Unreleased] into a versioned release."""
    if date is None:
        date = today_iso()

    content = path.read_text(encoding="utf-8")

    new_unreleased = """## [Unreleased]

### Added

### Changed

### Deprecated

### Removed

### Fixed

### Security

"""

    unreleased_pattern = re.compile(r"## \\[Unreleased\\]")
    if not unreleased_pattern.search(content):
        return False

    content = unreleased_pattern.sub(
        f"{new_unreleased}## [{version}] - {date}",
        content,
        count=1,
    )

    remote_url = get_remote_url()
    if remote_url:
        content = re.sub(
            r"\\[Unreleased\\]:\\s*.+",
            f"[Unreleased]: {remote_url}/compare/v{version}...HEAD",
            content,
        )
        if f"[{version}]:" not in content:
            prev_tag = get_latest_tag()
            if prev_tag:
                new_link = f"[{version}]: {remote_url}/compare/{prev_tag}...v{version}\\n"
            else:
                new_link = f"[{version}]: {remote_url}/releases/tag/v{version}\\n"
            content = content.rstrip() + "\\n" + new_link

    path.write_text(content, encoding="utf-8")
    return True
