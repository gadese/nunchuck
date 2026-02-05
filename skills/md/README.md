# md — Markdown Lifecycle Skills

The `md` directory contains a small set of standalone skills for managing markdown documents through a deterministic lifecycle.

> **Make state explicit.
> Make control flow visible.
> Make irreversible actions deliberate.**

## Purpose

Markdown documents tend to oscillate between two bad states:

- too large to review safely
- split into fragments that are hard to reassemble

These skills exist to make markdown structure explicit, repeatable, and auditable.

## The skills (and how they relate)

This is one system composed of three standalone skills:

- `md-split`
  - makes structure explicit by splitting a source file on `##` headings
  - writes a directory of chunk files plus derived index/manifest artifacts
- `md-review`
  - read-only quality gate
  - runs deterministic lint checks and prints findings for an agent to use during review
- `md-merge`
  - collapses explicit structure back into a single file deterministically
  - uses `.SPLIT.json` ordering when present

## Mental model

Think of `md` as a build pipeline for documents, but with explicit artifacts:

```text
SOURCE.md
  ↓
md-split   (structure becomes explicit; files are created)
  ↓
md-review  (quality gate; read-only)
  ↓
md-merge   (structure collapses deterministically; merged file is created)
  ↓
FINAL.md
```

At no point should an agent:

- invent structure
- infer ordering
- silently mutate content

## Lifecycle, artifacts, and constraints

### Authoritative vs derived artifacts

- **Authoritative inputs**
  - `SOURCE.md` (input to `md-split`)
  - `<chunks_dir>/NN_*.md` (inputs to `md-merge`)
- **Derived views / state**
  - `<chunks_dir>/.SPLIT.json` (ordering + provenance; written by `md-split` when enabled)
  - `<chunks_dir>/.INDEX.md` (index view; written by `md-split`)
  - `*_merged.md` (or `--out` target) written by `md-merge`

### Which skills mutate state

- `md-split` writes chunk files and may overwrite with `--force` (destructive).
- `md-merge` writes a merged file and may overwrite with `--force` (destructive).
- `md-review` is read-only.

### Invariants

- Structure is produced by scripts, not agents.
- Ordering is numeric and explicit (`NN_...`).
- Round-tripping (`split → merge`) should preserve content, modulo deterministic heading promotion/demotion.

## How to run

Each skill is independently invokable via its `scripts/skill.sh` (or `scripts/skill.ps1`) entrypoint.

- `md-split`: `skills/md/md-split/scripts/skill.sh --in <source.md> [--out <dir>] ...`
- `md-review`: `skills/md/md-review/scripts/skill.sh <file|dir>`
- `md-merge`: `skills/md/md-merge/scripts/skill.sh <chunks_dir> [--out <file>] ...`
