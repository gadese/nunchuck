---
description: Diagnoses software failures by combining deterministic evidence gathering
auto_execution_mode: 1
---

# doctor

This workflow delegates to the agent skill at `skills/doctor/`.

## Instructions

1. Read the skill manifest: `skills/doctor/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - 00_INDEX.md
   - 01_SUMMARY.md
   - 02_TRIGGERS.md
   - 03_ALWAYS.md
   - 04_NEVER.md
   - 05_PROCEDURE.md
   - 06_FAILURES.md
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/doctor/`
- **References:** `references/`
- **Scripts:** `scripts/`

## Keywords

`diagnose,debug investigate,evidence hypothesis,treatment`
