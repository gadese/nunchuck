---
status: complete
---

# Phase 1bi — CLI scaffolding

## Focus

Create the `nunchuck` CLI scaffolding (module/package layout and a basic command entrypoint) and decide the configuration conventions for how skills are discovered and installed.

## Inputs

- Output of `docs/planning/phase-1/a/ii.md`
- Existing scripts patterns under `scripts/`

## Work

1. Choose the implementation approach for the CLI (language, packaging, and how it will be run by users).
2. Create the CLI entrypoint and subcommand structure.
3. Define config/flags for:
   - source skill package directory
   - target project install directory
   - output format (human vs `--json`)

## Output

### Implementation approach

- CLI implemented in **Python** (stdlib-only for scaffolding) using `argparse`.
- Packaging via `pyproject.toml` with a console entrypoint `nunchuck = nunchuck.cli:main`.
- Minimum supported Python: `>=3.11` (for `tomllib`).

### Files created

- `pyproject.toml`
- `src/nunchuck/__init__.py`
- `src/nunchuck/__main__.py` (enables `python -m nunchuck`)
- `src/nunchuck/cli.py` (argument parsing + subcommand stubs)

### CLI UX (initial)

- `nunchuck list --root <path> [--json]`
- `nunchuck validate <target> [--json]`
- `nunchuck install <source> --project <path>`
- `nunchuck uninstall <name> --project <path>`

(Behavior is stubbed; implemented in Phase 1bii.)

## Handoff

Proceed to **Phase 1bii — Core commands**.

Implement:

- `list`: discover packs and/or skills from a root (per Phase 1a definitions)
- `validate`: implement the validation categories and JSON schema from `phase-1/a/iii.md`
- `install`/`uninstall`: deterministic pack install into `<project>/.nunchuck/packs/<name>/` with a reversible manifest in `<project>/.nunchuck/state/`
