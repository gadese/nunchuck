---
status: complete
---

# Phase 1eii — Idempotence checks

## Focus

Ensure core workflows (index generation, validation, install/uninstall) are idempotent and safe to rerun, minimizing repo drift.

## Inputs

- Implemented scripts/CLI from Phase 1b and Phase 1e

## Work

1. Run install/uninstall repeatedly and confirm no unexpected changes.
2. Run index regeneration repeatedly and confirm stable output.
3. Capture any nondeterminism and fix it.

## Output

### Checks performed

- Validation (twice):
  - `bash scripts/nunchuck/validate.sh` (ran twice; stable output; exit code 0)
- Index generation (twice):
  - `bash scripts/index/index.sh` (ran twice; stable output)
- Install/uninstall flow (twice):
  - `bash scripts/nunchuck/smoke_test.sh` (ran twice; deterministic behavior)

## Handoff

Proceed to **Phase 1eiii — Final sweep**.
