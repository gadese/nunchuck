---
status: complete
---

# Phase 1bii — Core commands

## Focus

Implement the core CLI behavior:

- `nunchuck list`
- `nunchuck validate`
- `nunchuck install`
- `nunchuck uninstall`

with deterministic, idempotent filesystem semantics.

## Inputs

- Output of `docs/planning/phase-1/b/i.md`
- Validation rules from `docs/planning/phase-1/a/iii.md`

## Work

1. Implement skill discovery from a root directory (find `SKILL.md`, parse frontmatter).
2. Implement validation runner and report formatting.
3. Implement install/uninstall operations with collision handling and a reversible manifest.

## Output

### Implemented commands

- `nunchuck list --root <path> [--json]`
  - Discovers packs by finding directories containing `nunchuck.toml` and `skills/`.
- `nunchuck validate <target> [--json]`
  - Validates either a pack root (if `nunchuck.toml` + `skills/` exist) or a single skill directory (if `SKILL.md` exists).
  - Implements the error/warning categories and JSON shape defined in `phase-1/a/iii.md`.
- `nunchuck install <source> --project <path>`
  - Installs a pack into `<project>/.nunchuck/packs/<pack-name>/`.
  - Writes/updates `<project>/.nunchuck/state/installs.json` with a deterministic directory hash.
  - If an identical hash is already installed for that pack name, it no-ops.
- `nunchuck uninstall <name> --project <path>`
  - Removes `<project>/.nunchuck/packs/<name>/` and updates `installs.json`.

### Files added

- `src/nunchuck/frontmatter.py` (restricted YAML frontmatter parser)
- `src/nunchuck/packs.py` (pack discovery + hashing + install state persistence)
- `src/nunchuck/validation.py` (pack/skill validation + human/JSON formatting)
- `src/nunchuck/installer.py` (install/uninstall operations)
- Updated `src/nunchuck/cli.py` to wire subcommands.

## Handoff

Proceed to **Phase 1biii — Smoke tests**.

Add a deterministic smoke test script that:

- Runs `python -m nunchuck list --root .`
- Runs `python -m nunchuck validate <some-target>`
- Installs the current repo as a pack into a temp project dir and then uninstalls it

(If needed for the smoke test, create a minimal `nunchuck.toml` in-repo to treat this repository as a pack.)
