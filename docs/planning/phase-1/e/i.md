---
status: complete
---

# Phase 1ei — Validation gate

## Focus

Add a deterministic validation entrypoint (script and/or CLI command) that can be run in CI or locally to verify skill package correctness.

## Inputs

- Validation rules from `docs/planning/phase-1/a/iii.md`
- CLI validate implementation from `docs/planning/phase-1/b/ii.md`

## Work

1. Add a canonical validation entrypoint suitable for CI.
2. Define exit code semantics and error reporting.
3. Ensure validation runs against the reorganized skill tree.

## Output

### Canonical validation entrypoints

- Unix: `bash scripts/nunchuck/validate.sh`
- Windows: `powershell -File scripts/nunchuck/validate.ps1`

These run `nunchuck validate` against the repo root (treated as a pack).

### Exit code semantics

- `0`: no validation errors
- `1`: validation errors present
- `2`: invalid invocation

## Handoff

Proceed to **Phase 1eii — Idempotence checks**.
