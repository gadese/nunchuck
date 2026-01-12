---
status: complete
---

# Phase 1ci — Compliance audit

## Focus

Audit all skills/skillsets for compliance with the Agent Skills spec and this repo’s conventions, then make the minimum required refactors for packaging readiness.

## Inputs

- Validation rules from `docs/planning/phase-1/a/iii.md`
- Skill directories under `skills/`

## Work

1. Enumerate all `SKILL.md` files and confirm name/dir matching, required fields, and minimal body content.
2. Ensure `metadata.references` order matches actual reference files.
3. Fix any obvious resource placement issues (scripts/references/assets).

## Output

### Validation result

Ran:

- `PYTHONPATH=src python3 -m nunchuck validate . --json`

Summary:

- `errors: 0`
- `warnings: 1`
- `skills_scanned: 37`

### Fixes performed

- Renamed/moved member skill directories so the directory containing `SKILL.md` matches `name`.
- Normalized `metadata.references` and `metadata.scripts` entries to be relative to their scoped directories:
  - `skills/mimic/SKILL.md`: removed `references/` prefix from reference entries.
  - `skills/md/md-split/SKILL.md`: removed erroneous `scripts/` prefix from script entries.
- Fixed skillset resource issues:
  - `skills/plan/.resources/references/DEFINTIONS.md` -> `DEFINITIONS.md`
  - `skills/prompt/SKILL.md`: `resources.root` set to `.prompt` (matches on-disk directory)

## Handoff

Proceed to **Phase 1cii — Resource boundaries**.

Focus next on:

- Tightening `.resources/` scoping and ensuring no cross-skill coupling.
- Auditing `assets/` contents for static-only convention.
- Resolving the remaining warning (missing Windows variant for `skills/doctor/doctor-triage/scripts/evidence.sh`).
