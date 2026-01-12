---
description: Load a mimic persona into the active slot (assets/persona/spec.yaml).
auto_execution_mode: 1
---

# mimic-load

This workflow delegates to the agent skill at `skills/mimic/.skills/mimic-load/`.

## Instructions

1. Read the skill manifest: `skills/mimic/.skills/mimic-load/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - 00_INSTRUCTIONS.md
   - 01_INTENT.md
   - 02_PRECONDITIONS.md
   - 03_PROCEDURE.md
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/mimic/.skills/mimic-load/`
- **References:** `references/`
- **Scripts:** `scripts/`

## Keywords

`mimic,persona load,slot activate`
