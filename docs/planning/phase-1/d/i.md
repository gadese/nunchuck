---
status: complete
---

# Phase 1di — Docs update

## Focus

Update user-facing documentation to reflect `nunchuck` identity, the canonical skill package layout, and CLI workflows.

## Inputs

- Implemented CLI from Phase 1b
- Target layout from Phase 1a
- Existing docs under `docs/` and `README.md`

## Work

1. Update README and Quickstart with the new “installable skill packages” framing.
2. Add CLI examples for list/validate/install/uninstall.
3. Ensure documentation aligns with spec and does not drift from deterministic behavior.

## Output

Completed updates:

- Added repo-root `INDEX.md` that points to `skills/INDEX.md`.
- Updated `README.md` to reference:
  - `skills/<skillset>/...` paths
  - `skills/INDEX.md` as the canonical index
  - `docs/references/AGENT_SKILLS_SPEC.md` as the spec reference
- Updated `docs/SKILLS.md` and `docs/SKILLSETS.md` to align with the current `skills/` layout and script-driven adapters.
- Updated `docs/QUICKSTART.md` with a `nunchuck validate` quick check.

## Handoff

Proceed to **Phase 1e — Quality gates and cleanup**.
