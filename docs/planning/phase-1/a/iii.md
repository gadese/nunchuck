---
status: complete
---

# Phase 1aiii — Define validation rules

## Focus

Define what deterministic validation means for this repo and what `nunchuck validate` must check (spec compliance, repo conventions, and installation readiness).

## Inputs

- Output of `docs/planning/phase-1/a/ii.md`
- `docs/schema/skill/*`
- `docs/schema/skillset/*`

## Work

1. Define validation categories (spec compliance, naming rules, required files, referenced file existence, script executability, etc.).
2. Decide which checks are errors vs warnings.
3. Define the machine-readable output shape (`--json`) and human summary format.

## Output

## Validation scope

`nunchuck validate` operates at two levels:

- **Pack-level**: validates a pack root (presence + structure + install readiness).
- **Skill-level**: validates an individual skill/skillset directory (spec + conventions).

In all cases, validation should be deterministic from disk state and should not rely on network access.

## Categories and checks

### A) Pack-level structure (errors)

- `nunchuck.toml` exists at the pack root.
- `skills/` exists at the pack root.
- At least one `skills/**/SKILL.md` exists.

### B) Skill spec compliance (errors)

For each discovered skill directory `<skill-dir>` containing `SKILL.md`:

- Frontmatter exists and parses.
- `name` exists.
- `description` exists.
- `name` matches the parent directory name.
- `name` matches allowed pattern (lowercase, digits, hyphen; no leading/trailing hyphen; no `--`).

### C) Repo/pack conventions (errors unless noted)

- If `metadata.references` exists:
  - Every referenced file exists under `<skill-dir>/references/<ref>`.
- If `metadata.scripts` exists:
  - Every listed script exists under `<skill-dir>/scripts/<script>` OR under the declared shared resources root (see skillset section below).
- If `metadata.keywords` exists:
  - Each keyword is non-empty (warning if empty strings present).

### D) Skillset schema validation (errors)

If `metadata.skillset` exists:

- `metadata.skillset.schema_version == 1`.
- `metadata.skillset.name` matches the top-level `name`.
- `metadata.skillset.skills` is a non-empty list.
- `metadata.skillset.pipelines.default` is a list of skill names.
- Every skill listed in `pipelines.default` is present in `skills`.
- Every pipeline listed in `pipelines.allowed` only includes skills that are in `skills`.

Resources:

- If `metadata.skillset.resources.root` exists:
  - The directory exists under the skillset directory (e.g. `<skillset-dir>/.resources/`).
  - Each listed `assets`/`scripts`/`references` entry exists under `<root>/assets|scripts|references`.

### E) Cross-platform scripts (warnings)

When a script name is listed in metadata and appears to be platform-specific:

- If `foo.sh` exists but `foo.ps1` does not (or vice versa), emit a warning.
- If a script file exists but is not executable on unix, emit a warning (do not chmod during validate).

### F) Installation readiness (warnings unless fatal)

- Detect “dangling references” that point outside the skill directory or declared resources root (error).
- Detect duplicate `name` across skills within the same pack (error).
- Detect markdown files under `assets/` (warning; per best practices, assets should be static).

## Errors vs warnings policy

- **Error**: anything that breaks spec compliance, breaks referenced-file integrity, or makes install/uninstall unsafe.
- **Warning**: best-practice deviations that do not prevent correct use (cross-platform parity, non-executable scripts, assets containing markdown).

## Output formats

### Human-readable (default)

- One-line summary per pack/skill.
- Final totals:
  - number of packs scanned
  - number of skills scanned
  - number of errors
  - number of warnings
- Exit code semantics:
  - `0`: no errors
  - `1`: errors present
  - `2`: invalid invocation (bad args)

### JSON (`--json`)

JSON should be a deterministic object:

- `target`: string (path)
- `mode`: `pack` or `skill`
- `summary`:
  - `errors`: integer
  - `warnings`: integer
  - `skills_scanned`: integer
- `results`: array of entries:
  - `path`
  - `name` (if applicable)
  - `kind`: `skill` or `skillset`
  - `issues`: array
    - `severity`: `error` | `warning`
    - `code`: stable string (e.g. `SKILL_NAME_MISMATCH`)
    - `message`: human string
    - `file`: optional path
    - `hint`: optional remediation hint

## Handoff

Proceed to **Phase 1b — Implement `nunchuck` CLI (MVP)** starting with `docs/planning/phase-1/b/i.md`.

The CLI should implement `validate` using the categories and formats above, and it should treat the pack root (`nunchuck.toml` + `skills/`) as the primary unit of installation.
