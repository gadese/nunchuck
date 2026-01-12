---
status: complete
---

# Phase 1ciii — Regenerate indexes/adapters

## Focus

Update and regenerate any discovery/index artifacts and IDE adapters so they reflect the reorganized layout and remain deterministic.

## Inputs

- Updated skill tree from `docs/planning/phase-1/c/ii.md`
- Existing index/adapter skills and scripts under `skills/` and `scripts/`

## Work

1. Ensure the index generation scripts correctly discover all skills in the new layout.
2. Ensure adapter generation (Windsurf/Cursor) references the correct skill paths.
3. Regenerate the repo indexes and validate that docs reflect the new structure.

## Output

### Index regeneration

- Updated index generators to keep `skills/INDEX.md` and `skills/.INDEX.md` in sync:
  - `scripts/index/index.sh`
  - `scripts/index/index.ps1`
- Regenerated index:
  - `bash scripts/index/index.sh`

### Adapter regeneration

- Regenerated Windsurf workflows:
  - `bash scripts/adapter/windsurf.sh`
- Regenerated Cursor commands:
  - `bash scripts/adapter/cursor.sh`

### Validation

- `PYTHONPATH=src python3 -m nunchuck validate .` reports `Errors: 0  Warnings: 0`.

## Handoff

Proceed to the **Phase 1 wrap-up** (update the phase root plan status and validate repo end-to-end).
