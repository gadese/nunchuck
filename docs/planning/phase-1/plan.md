---
status: complete
---

# Phase 1 — Convert skills repository into nunchuck

## Purpose

Consolidate and productize this skills repository into `nunchuck`: an installable, isolated skill-package system with a small CLI.

## Context

The current repository contains a large set of agent skills and skillsets with shared conventions (thin `SKILL.md`, progressive disclosure via `references/`, deterministic scripts, and shared `.resources/` folders). The goal is to reorganize and harden these conventions into a distributable “skill package” model where:

- Each skill is independently usable and spec-compliant.
- Skillsets orchestrate without coupling member skills.
- Installation into a local project is deterministic and reversible via a minimal `nunchuck` CLI.

## Objectives

* [x] Establish the target on-disk package structure and validation rules for skills/skillsets
* [x] Implement a minimal `nunchuck` CLI for listing/installing/validating/uninstalling skills
* [x] Refactor/migrate existing skills to the new package structure and conventions
* [x] Update documentation, adapters, and workflows to match the new structure
* [x] Add deterministic validation as a first-class quality gate

## Constraints

- Follow the Agent Skills spec (`SKILL.md` is YAML frontmatter + optional markdown body; keep it minimal).
- Each skill must remain independently usable (skillset membership is optional grouping).
- Prefer deterministic truth from disk state (generate indexes/validation; avoid handwritten drift).
- Keep a clean separation:
  - deterministic logic in `scripts/`
  - static templates/schemas in `assets/`
  - subjective guidance in `references/`
- Cross-platform scripting where relevant (`.sh` + `.ps1`).

## Success Criteria

- `nunchuck` CLI exists and can:
  - list installed/available skills
  - validate skill directories for spec compliance and repo conventions
  - install/uninstall skills into a local project deterministically
- Repo is reorganized into a canonical structure suitable for packaging.
- Existing skills/skillsets are migrated with:
  - thin `SKILL.md`
  - ordered `metadata.references`
  - declared scripts/assets (where used)
  - shared resources kept in a clearly scoped `.resources/` directory
- Documentation and adapter/workflow generators reflect the new structure.

## Sub-plan Index

* a — Target package layout and validation rules
* b — Implement `nunchuck` CLI (MVP)
* c — Migrate/refactor existing skills to the new layout
* d — Update docs + adapters/workflows for the new structure
* e — Quality gates (deterministic validation) and final cleanup

## Plan Summary

- Canonical skill index: `skills/INDEX.md` (also mirrored to `skills/.INDEX.md`)
  - regenerate: `bash scripts/index/index.sh`
- Adapter generation:
  - Windsurf: `bash scripts/adapter/windsurf.sh` (outputs `.windsurf/workflows/*.md`)
  - Cursor: `bash scripts/adapter/cursor.sh` (outputs `.cursor/commands/*.md`)
- Validation:
  - `PYTHONPATH=src python3 -m nunchuck validate .`
  - CI-friendly entrypoints: `scripts/nunchuck/validate.sh` and `scripts/nunchuck/validate.ps1`
- Smoke test:
  - `bash scripts/nunchuck/smoke_test.sh` (list → validate → install → uninstall)
