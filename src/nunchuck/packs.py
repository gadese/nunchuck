from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import tomllib
except ImportError:
    import tomli as tomllib


class PackError(Exception):
    pass


@dataclass(frozen=True)
class PackMeta:
    name: str
    version: str
    root: Path


def read_pack_meta(pack_root: Path) -> PackMeta:
    cfg = pack_root / "nunchuck.toml"
    if not cfg.exists():
        raise PackError(f"Missing nunchuck.toml: {cfg}")

    data = tomllib.loads(cfg.read_text(encoding="utf-8"))
    pack = data.get("pack")
    if not isinstance(pack, dict):
        raise PackError("Missing [pack] table in nunchuck.toml")

    name = pack.get("name")
    version = pack.get("version")

    if not isinstance(name, str) or not name:
        raise PackError("pack.name must be a non-empty string")
    if not isinstance(version, str) or not version:
        raise PackError("pack.version must be a non-empty string")

    return PackMeta(name=name, version=version, root=pack_root)


def discover_packs(root: Path) -> list[PackMeta]:
    packs: list[PackMeta] = []

    # If root itself is a pack
    if (root / "nunchuck.toml").exists() and (root / "skills").is_dir():
        try:
            packs.append(read_pack_meta(root))
        except Exception:
            # ignore for discovery
            pass

    if not root.exists():
        return packs

    for p in sorted(root.rglob("nunchuck.toml")):
        pack_root = p.parent
        if not (pack_root / "skills").is_dir():
            continue
        # skip nested packs already included by parent walk
        if any(pack_root == m.root for m in packs):
            continue
        try:
            packs.append(read_pack_meta(pack_root))
        except Exception:
            continue

    # stable order
    packs.sort(key=lambda m: (m.name, m.version, str(m.root)))
    return packs


def compute_dir_hash(root: Path) -> str:
    """Deterministic content hash for a directory (paths + bytes)."""
    h = hashlib.sha256()

    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        if rel.startswith(".git/"):
            continue
        if "__pycache__" in rel:
            continue
        h.update(rel.encode("utf-8"))
        h.update(b"\0")
        h.update(path.read_bytes())
        h.update(b"\0")

    return h.hexdigest()


def copy_tree(src: Path, dst: Path) -> None:
    if dst.exists():
        shutil.rmtree(dst)

    def ignore(dirpath: str, names: list[str]) -> set[str]:
        ignored: set[str] = set()
        if ".git" in names:
            ignored.add(".git")
        if "__pycache__" in names:
            ignored.add("__pycache__")
        return ignored

    shutil.copytree(src, dst, copy_function=shutil.copy2, ignore=ignore)


def load_install_state(project_root: Path) -> dict[str, Any]:
    state = project_root / ".nunchuck/state/installs.json"
    if not state.exists():
        return {"packs": []}

    return json.loads(state.read_text(encoding="utf-8"))


def save_install_state(project_root: Path, data: dict[str, Any]) -> None:
    state_dir = project_root / ".nunchuck/state"
    state_dir.mkdir(parents=True, exist_ok=True)
    state = state_dir / "installs.json"
    state.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
