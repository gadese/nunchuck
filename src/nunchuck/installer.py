from __future__ import annotations

from pathlib import Path
from typing import Any

from .packs import compute_dir_hash, copy_tree, load_install_state, read_pack_meta, save_install_state


class InstallError(Exception):
    pass


def install_pack(source: Path, project_root: Path) -> dict[str, Any]:
    source = source.resolve()
    project_root = project_root.resolve()

    meta = read_pack_meta(source)

    dest_root = project_root / ".nunchuck/packs" / meta.name
    dest_root.parent.mkdir(parents=True, exist_ok=True)

    src_hash = compute_dir_hash(source)

    state = load_install_state(project_root)
    packs = state.setdefault("packs", [])

    # if already installed with same hash, no-op
    for p in packs:
        if p.get("name") == meta.name:
            if p.get("hash") == src_hash:
                return {"status": "noop", "name": meta.name, "version": meta.version, "path": str(dest_root)}

    copy_tree(source, dest_root)

    # update state
    packs = [p for p in packs if p.get("name") != meta.name]
    packs.append({"name": meta.name, "version": meta.version, "source": str(source), "path": str(dest_root), "hash": src_hash})
    packs.sort(key=lambda x: x.get("name", ""))
    state["packs"] = packs
    save_install_state(project_root, state)

    return {"status": "installed", "name": meta.name, "version": meta.version, "path": str(dest_root)}


def uninstall_pack(name: str, project_root: Path) -> dict[str, Any]:
    project_root = project_root.resolve()
    dest_root = project_root / ".nunchuck/packs" / name

    state = load_install_state(project_root)
    packs = state.get("packs", [])

    found = next((p for p in packs if p.get("name") == name), None)
    if found is None and not dest_root.exists():
        return {"status": "noop", "name": name}

    if dest_root.exists():
        # delete pack directory
        import shutil

        shutil.rmtree(dest_root)

    state["packs"] = [p for p in packs if p.get("name") != name]
    save_install_state(project_root, state)

    return {"status": "uninstalled", "name": name}
