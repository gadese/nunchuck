---
status: complete
---

# Phase 1cii — Resource boundaries

## Focus

Normalize shared resources and per-skill resources so that packaging and installation are clean and deterministic (no accidental cross-skill coupling).

## Inputs

- Output of `docs/planning/phase-1/c/i.md`
- Tenets: `docs/KICKOFF.md`

## Work

1. Ensure shared resources are clearly scoped (e.g., skillset-level `.resources/`) and do not leak across unrelated skills.
2. Ensure assets are static (schemas/templates/data) and avoid markdown in `assets/`.
3. Ensure scripts are self-contained and have clear error messages.

## Output

### Normalizations performed

- Added a Windows PowerShell variant for the doctor triage evidence helper script:
  - `skills/doctor/doctor-triage/scripts/evidence.ps1`

This removes the remaining cross-platform parity warning from `nunchuck validate .`.

## Handoff

Proceed to **Phase 1ciii — Regenerate indexes/adapters**.

Verify that any index/adapters that enumerate skills still discover all `SKILL.md` under the renamed member directories.
