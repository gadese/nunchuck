---
status: complete
---

# Phase 1biii — Smoke tests

## Focus

Add a small set of deterministic smoke tests and runnable checks to ensure the CLI works for common flows (list, validate, install, uninstall).

## Inputs

- Implemented CLI from `docs/planning/phase-1/b/ii.md`
- A representative set of skills/skillsets in this repo

## Work

1. Add a smoke test script (or minimal test harness) that runs the CLI against a temp directory.
2. Verify install/uninstall are idempotent.
3. Document the smoke test command(s).

## Output

### Smoke test script

- Added: `scripts/nunchuck/smoke_test.sh`

### How to run

```bash
bash scripts/nunchuck/smoke_test.sh
```

Notes:

- The smoke test sets `PYTHONPATH=src` and runs:
  - `python3 -m nunchuck list --root <repo>`
  - `python3 -m nunchuck validate <repo>` (non-zero is currently expected until skills are migrated)
  - `python3 -m nunchuck install <repo> --project <tmpdir>`
  - `python3 -m nunchuck uninstall nunchuck --project <tmpdir>`

### Pack metadata

- Added: `nunchuck.toml` at repo root so the repository can be treated as a pack for install/uninstall testing.

## Handoff

Proceed to **Phase 1c — Migrate/refactor existing skills to the new layout**, starting with `docs/planning/phase-1/c/i.md`.

Use `nunchuck validate .` output as the authoritative list of spec/convention failures to fix.
