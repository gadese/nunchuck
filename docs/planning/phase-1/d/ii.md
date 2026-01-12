---
status: complete
---

# Phase 1dii — Workflow alignment

## Focus

Update workflow/adapters so they invoke the correct skills and scripts after the reorganization.

## Inputs

- Output of `docs/planning/phase-1/c/iii.md`
- `.windsurf/workflows/*`

## Work

1. Ensure Windsurf workflows reference valid skill paths.
2. Ensure any assumptions about `.resources/` or `scripts/` paths remain correct after migration.
3. Regenerate workflows if needed using adapter skills.

## Output

### Workflow regeneration

- Regenerated Windsurf workflows via `bash scripts/adapter/windsurf.sh`.
- `.gitignore` updated to ignore `.windsurf/*` but *unignore* `.windsurf/workflows/**` so generated workflow adapters can be committed.

### Path verification

- Workflows were regenerated after the directory renames (e.g. `skills/plan/plan-status/`) so they now reference valid skill paths.

## Handoff

Proceed to **Phase 1diii — Migration guide**.
