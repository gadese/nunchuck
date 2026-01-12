---
status: complete
---

# Phase 1diii — Migration guide

## Focus

Create a migration guide describing how to transition from the current repo structure to the new `nunchuck` package structure and how local projects should install/use skills.

## Inputs

- Target layout and CLI behavior from Phase 1a/1b

## Work

1. Document “before/after” structure and common pitfalls.
2. Document recommended install locations in a consuming project.
3. Document how to validate and troubleshoot installs.

## Output

### Migration guide (high-level)

- **Before:** skillset members commonly lived in `skills/<skillset>/<short-name>/` where `<short-name>` did not match `name` in `SKILL.md`.
- **After:** every skill directory containing `SKILL.md` matches its `name` (e.g. `skills/plan/plan-status/`, `skills/task/task-list/`).

Recommended consuming-project install locations:

- Packs install under `<project>/.nunchuck/packs/<pack-name>/`.
- Install state is tracked at `<project>/.nunchuck/state/installs.json`.

Validation / troubleshooting:

- Validate a repo/pack: `PYTHONPATH=src python3 -m nunchuck validate <pack-root>`
- Validate a single skill: `PYTHONPATH=src python3 -m nunchuck validate <skill-dir>`
- If validation fails, fix spec issues first (frontmatter parse, `name`/dir mismatch, missing referenced files).

## Handoff

Proceed to **Phase 1e — Quality gates and cleanup**.
