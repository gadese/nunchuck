from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any, Literal, TypedDict

from .frontmatter import FrontmatterError, read_frontmatter
from .packs import PackError, read_pack_meta


Severity = Literal["error", "warning"]


class Issue(TypedDict, total=False):
    severity: Severity
    code: str
    message: str
    file: str
    hint: str


class Result(TypedDict, total=False):
    path: str
    name: str
    kind: str
    issues: list[Issue]


class Report(TypedDict, total=False):
    target: str
    mode: str
    summary: dict[str, int]
    results: list[Result]


_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def validate_target(target: Path) -> tuple[int, Report]:
    if (target / "nunchuck.toml").exists() and (target / "skills").is_dir():
        rep = validate_pack(target)
        return (0 if rep["summary"]["errors"] == 0 else 1), rep

    if target.is_dir() and (target / "SKILL.md").exists():
        rep = validate_skill(target)
        return (0 if rep["summary"]["errors"] == 0 else 1), rep

    return 2, {
        "target": str(target),
        "mode": "unknown",
        "summary": {"errors": 1, "warnings": 0, "skills_scanned": 0},
        "results": [
            {
                "path": str(target),
                "issues": [
                    {
                        "severity": "error",
                        "code": "INVALID_TARGET",
                        "message": "Target is neither a pack root (nunchuck.toml + skills/) nor a skill directory (SKILL.md)",
                    }
                ],
            }
        ],
    }


def validate_pack(pack_root: Path) -> Report:
    results: list[Result] = []
    errors = 0
    warnings = 0

    # pack structure checks
    pack_issues: list[Issue] = []
    try:
        read_pack_meta(pack_root)
    except PackError as e:
        pack_issues.append(_err("PACK_TOML_INVALID", str(e), file=str(pack_root / "nunchuck.toml")))

    if not (pack_root / "skills").is_dir():
        pack_issues.append(_err("PACK_SKILLS_MISSING", "Missing skills/ directory", file=str(pack_root)))

    if pack_issues:
        results.append({"path": str(pack_root), "kind": "pack", "issues": pack_issues})

    skills_root = pack_root / "skills"
    skill_dirs = sorted({p.parent for p in skills_root.rglob("SKILL.md")})
    if not skill_dirs:
        results.append(
            {
                "path": str(skills_root),
                "kind": "pack",
                "issues": [_err("PACK_NO_SKILLS", "No SKILL.md files found under skills/", file=str(skills_root))],
            }
        )

    seen_names: set[str] = set()
    for sd in skill_dirs:
        rep = validate_skill(sd)
        # collapse skill report into pack results list
        for r in rep.get("results", []):
            results.append(r)
        errors += rep["summary"]["errors"]
        warnings += rep["summary"]["warnings"]

        # duplicate names within pack
        for r in rep.get("results", []):
            name = r.get("name")
            if isinstance(name, str) and name:
                if name in seen_names:
                    errors += 1
                    r.setdefault("issues", []).append(
                        _err(
                            "DUPLICATE_SKILL_NAME",
                            f"Duplicate skill name within pack: {name}",
                            file=str(sd / "SKILL.md"),
                        )
                    )
                else:
                    seen_names.add(name)

    # incorporate pack issues into counts
    for iss in pack_issues:
        if iss["severity"] == "error":
            errors += 1
        else:
            warnings += 1

    return {
        "target": str(pack_root),
        "mode": "pack",
        "summary": {"errors": errors, "warnings": warnings, "skills_scanned": len(skill_dirs)},
        "results": results,
    }


def validate_skill(skill_dir: Path) -> Report:
    issues: list[Issue] = []

    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        issues.append(_err("SKILL_FILE_MISSING", "Missing SKILL.md", file=str(skill_file)))
        return {
            "target": str(skill_dir),
            "mode": "skill",
            "summary": {"errors": 1, "warnings": 0, "skills_scanned": 0},
            "results": [{"path": str(skill_dir), "kind": "skill", "issues": issues}],
        }

    name = None
    kind = "skill"

    try:
        fm = read_frontmatter(skill_file)
    except FrontmatterError as e:
        issues.append(_err("FRONTMATTER_INVALID", str(e), file=str(skill_file)))
        return {
            "target": str(skill_dir),
            "mode": "skill",
            "summary": {"errors": 1, "warnings": 0, "skills_scanned": 0},
            "results": [{"path": str(skill_dir), "kind": "skill", "issues": issues}],
        }

    name_val = fm.get("name")
    desc_val = fm.get("description")

    if not isinstance(name_val, str) or not name_val:
        issues.append(_err("SKILL_NAME_MISSING", "Missing or invalid 'name'", file=str(skill_file)))
    else:
        name = name_val
        if name != skill_dir.name:
            issues.append(
                _err(
                    "SKILL_NAME_MISMATCH",
                    f"name '{name}' does not match directory '{skill_dir.name}'",
                    file=str(skill_file),
                )
            )
        if not _NAME_RE.match(name):
            issues.append(_err("SKILL_NAME_INVALID", f"Invalid skill name format: {name}", file=str(skill_file)))

    if not isinstance(desc_val, str) or not desc_val.strip():
        issues.append(_err("SKILL_DESCRIPTION_MISSING", "Missing or invalid 'description'", file=str(skill_file)))

    metadata = fm.get("metadata") if isinstance(fm.get("metadata"), dict) else {}

    # references integrity
    refs = metadata.get("references")
    if isinstance(refs, list):
        for ref in refs:
            if not isinstance(ref, str) or not ref:
                issues.append(_warn("REFERENCE_INVALID", f"Invalid reference entry: {ref!r}", file=str(skill_file)))
                continue
            ref_path = (skill_dir / "references" / ref).resolve()
            if not _is_under(ref_path, skill_dir / "references"):
                issues.append(_err("REFERENCE_ESCAPE", f"Reference escapes references/: {ref}", file=str(skill_file)))
                continue
            if not ref_path.exists():
                issues.append(_err("REFERENCE_MISSING", f"Missing reference file: references/{ref}", file=str(skill_file)))

    # scripts integrity
    scripts = metadata.get("scripts")
    if isinstance(scripts, list):
        for script in scripts:
            if not isinstance(script, str) or not script:
                issues.append(_warn("SCRIPT_INVALID", f"Invalid script entry: {script!r}", file=str(skill_file)))
                continue
            script_path = (skill_dir / "scripts" / script).resolve()
            if not _is_under(script_path, skill_dir / "scripts"):
                issues.append(_err("SCRIPT_ESCAPE", f"Script escapes scripts/: {script}", file=str(skill_file)))
                continue
            if not script_path.exists():
                # allow skillset shared resources root (checked below)
                issues.append(_err("SCRIPT_MISSING", f"Missing script file: scripts/{script}", file=str(skill_file)))
            else:
                # cross-platform parity warning
                if script.endswith(".sh") and not (script_path.with_suffix(".ps1")).exists():
                    issues.append(_warn("SCRIPT_PLATFORM_MISSING", f"Missing Windows variant for {script}", file=str(script_path)))
                if script.endswith(".ps1") and not (script_path.with_suffix(".sh")).exists():
                    issues.append(_warn("SCRIPT_PLATFORM_MISSING", f"Missing Unix variant for {script}", file=str(script_path)))

    # keywords
    kws = metadata.get("keywords")
    if isinstance(kws, list):
        for kw in kws:
            if not isinstance(kw, str) or not kw.strip():
                issues.append(_warn("KEYWORD_EMPTY", "Empty keyword entry", file=str(skill_file)))

    # skillset schema
    skillset = metadata.get("skillset")
    if isinstance(skillset, dict):
        kind = "skillset"
        if skillset.get("schema_version") != 1:
            issues.append(_err("SKILLSET_SCHEMA_VERSION", "metadata.skillset.schema_version must be 1", file=str(skill_file)))
        if skillset.get("name") != name:
            issues.append(_err("SKILLSET_NAME_MISMATCH", "metadata.skillset.name must match top-level name", file=str(skill_file)))
        skills = skillset.get("skills")
        if not isinstance(skills, list) or not skills:
            issues.append(_err("SKILLSET_SKILLS_INVALID", "metadata.skillset.skills must be a non-empty list", file=str(skill_file)))
        pipelines = skillset.get("pipelines")
        if not isinstance(pipelines, dict):
            issues.append(_err("SKILLSET_PIPELINES_MISSING", "metadata.skillset.pipelines missing/invalid", file=str(skill_file)))
        else:
            default = pipelines.get("default")
            allowed = pipelines.get("allowed")
            if not isinstance(default, list) or not default:
                issues.append(_err("SKILLSET_PIPELINE_DEFAULT", "pipelines.default must be a non-empty list", file=str(skill_file)))
            if isinstance(default, list) and isinstance(skills, list):
                for s in default:
                    if s not in skills:
                        issues.append(_err("SKILLSET_PIPELINE_UNKNOWN", f"pipelines.default contains unknown skill: {s}", file=str(skill_file)))
            if not isinstance(allowed, list) or not allowed:
                issues.append(_err("SKILLSET_PIPELINE_ALLOWED", "pipelines.allowed must be a non-empty list", file=str(skill_file)))
            if isinstance(allowed, list) and isinstance(skills, list):
                for pipe in allowed:
                    if not isinstance(pipe, list):
                        issues.append(_err("SKILLSET_PIPELINE_ALLOWED_INVALID", "pipelines.allowed entries must be lists", file=str(skill_file)))
                        continue
                    for s in pipe:
                        if s not in skills:
                            issues.append(_err("SKILLSET_PIPELINE_UNKNOWN", f"pipelines.allowed contains unknown skill: {s}", file=str(skill_file)))

        resources = skillset.get("resources")
        if isinstance(resources, dict):
            root = resources.get("root")
            if isinstance(root, str) and root:
                res_root = (skill_dir / root).resolve()
                if not _is_under(res_root, skill_dir):
                    issues.append(_err("RESOURCE_ROOT_ESCAPE", f"resources.root escapes skill dir: {root}", file=str(skill_file)))
                if not res_root.exists():
                    issues.append(_err("RESOURCE_ROOT_MISSING", f"resources.root missing: {root}", file=str(skill_file)))
                else:
                    _validate_resource_list(issues, res_root, "assets", resources.get("assets"), skill_file)
                    _validate_resource_list(issues, res_root, "scripts", resources.get("scripts"), skill_file)
                    _validate_resource_list(issues, res_root, "references", resources.get("references"), skill_file)

    errors = sum(1 for i in issues if i["severity"] == "error")
    warnings = sum(1 for i in issues if i["severity"] == "warning")

    return {
        "target": str(skill_dir),
        "mode": "skill",
        "summary": {"errors": errors, "warnings": warnings, "skills_scanned": 1},
        "results": [{"path": str(skill_dir), "name": name or "", "kind": kind, "issues": issues}],
    }


def format_human(report: Report) -> str:
    lines: list[str] = []
    lines.append(f"Target: {report.get('target')}")
    lines.append(f"Mode: {report.get('mode')}")
    summary = report.get("summary", {})
    lines.append(f"Errors: {summary.get('errors', 0)}  Warnings: {summary.get('warnings', 0)}  Skills: {summary.get('skills_scanned', 0)}")
    lines.append("")

    for res in report.get("results", []):
        issues = res.get("issues", [])
        if not issues:
            continue
        name = res.get("name")
        header = res.get("path")
        if name:
            header = f"{name} ({header})"
        lines.append(header)
        for iss in issues:
            sev = iss.get("severity")
            code = iss.get("code")
            msg = iss.get("message")
            file = iss.get("file")
            loc = f" [{file}]" if file else ""
            lines.append(f"  - {sev}:{code}{loc} {msg}")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def format_json(report: Report) -> str:
    return json.dumps(report, indent=2, sort_keys=True) + "\n"


def _validate_resource_list(issues: list[Issue], root: Path, kind: str, items: Any, skill_file: Path) -> None:
    if items is None:
        return
    if not isinstance(items, list):
        issues.append(_err("RESOURCE_LIST_INVALID", f"resources.{kind} must be a list", file=str(skill_file)))
        return

    base = (root / kind).resolve()
    for it in items:
        if not isinstance(it, str) or not it:
            issues.append(_warn("RESOURCE_ENTRY_INVALID", f"Invalid resources.{kind} entry: {it!r}", file=str(skill_file)))
            continue
        p = (base / it).resolve()
        if not _is_under(p, base):
            issues.append(_err("RESOURCE_ESCAPE", f"resources.{kind} entry escapes {kind}/: {it}", file=str(skill_file)))
            continue
        if not p.exists():
            issues.append(_err("RESOURCE_MISSING", f"Missing resources.{kind} file: {it}", file=str(skill_file)))


def _is_under(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root.resolve())
        return True
    except Exception:
        return False


def _err(code: str, message: str, file: str | None = None, hint: str | None = None) -> Issue:
    out: Issue = {"severity": "error", "code": code, "message": message}
    if file:
        out["file"] = file
    if hint:
        out["hint"] = hint
    return out


def _warn(code: str, message: str, file: str | None = None, hint: str | None = None) -> Issue:
    out: Issue = {"severity": "warning", "code": code, "message": message}
    if file:
        out["file"] = file
    if hint:
        out["hint"] = hint
    return out
