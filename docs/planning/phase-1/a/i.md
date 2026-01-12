---
status: complete
---

# Phase 1ai — Inventory current structure

## Focus

Inventory the current repository structure (skills, skillsets, scripts, docs, and shared resources) and identify what needs to change to become an installable `nunchuck` skill-package system.

## Inputs

- `tasks/convert-skills-repo-to-nunchuck/00_TASK.md`
- `docs/schema/skill/*`
- `docs/schema/skillset/*`
- `docs/SKILLS.md`
- `docs/SKILLSETS.md`
- Existing skill directories under `skills/`

## Work

1. Identify the current “authoritative” skill roots and naming conventions (e.g. where `SKILL.md` files live, how `references/` are structured).
2. Identify existing shared resource patterns (e.g. `.resources/` usage under `skills/task/`).
3. List mismatches between current state and the intended packaging goals (installable, isolated skill packages, minimal CLI).

## Output

### Current repo structure (high-level)

- `skills/` — primary skill root (spec-style). Contains skillsets (`doctor/`, `md/`, `plan/`, `prompt/`, `refactor/`, `task/`) and some standalone skills (e.g. `mimic/`).
- `scripts/` — deterministic automation (index generation, IDE adapter generation, install helpers).
- `docs/` — human documentation + schemas + tenets.
- `.windsurf/workflows/` — generated thin workflow adapters (already present).
- `tasks/` — task tracking directories with `00_TASK.md`.

### Skill layout conventions observed

- Skills live under `skills/<skill>/...` with a `SKILL.md` file.
- Progressive disclosure is used: detailed instructions live in `references/` and are listed in `metadata.references`.
- Some skillsets use shared resources under a dot-prefixed shared folder (example: `skills/task/.resources/...`).
- Cross-platform automation exists mainly under `scripts/` (e.g. `scripts/index/index.sh` + `scripts/index/index.ps1`, and adapter scripts for Windsurf/Cursor).

### Existing shared resource patterns

- `skills/task/.resources/` contains:
  - `references/` (skillset-level usage docs)
  - `scripts/` (task lifecycle helper scripts)
  - `assets/` (schemas/templates)
- However, several docs/workflows in the task skillset expect repo-root `.resources/scripts/...` paths.
  - Repo-root `.resources/` did not exist originally; it is a mismatch between docs and actual canonical script location.

### Mismatches / risks vs the target “nunchuck package” goals

- **Missing root index artifact**: `README.md` references `./INDEX.md`, but no top-level `INDEX.md` exists in the repo.
- **Index output path mismatch**: `scripts/index/index.sh` defaults to writing `skills/INDEX.md`, while the current canonical index file appears to be `skills/.INDEX.md`.
- **Adapter/skillset mismatch**: Docs mention an `adapter` skillset and `index` skill under their own skill roots, but the current `skills/` tree does not include an `adapter/` or `index/` skill directory (only `scripts/adapter/*` and `scripts/index/*` exist).
- **Shared resources naming**: skillset-level `.resources/` is used, but the packaging goal will likely require a single, unambiguous convention for shared resources (and a deterministic mapping for install/uninstall).
- **Execution environment drift**: Python scripts exist under skill resources; there is not yet a single standardized runtime/venv story for running them in a consuming project (important for “installable, isolated”).

## Handoff

Proceed to **Phase 1aii — Define target layout**.

Use the inventory above to propose:

- A canonical skill package root layout (what gets installed, where it lives in a consumer project).
- A single convention for shared resources (skillset-level vs repo-level), including how CLI commands discover them.
- A decision on how to reconcile existing drift (missing root `INDEX.md`, `skills/INDEX.md` vs `skills/.INDEX.md`, and adapter/index “skill vs script” status).
