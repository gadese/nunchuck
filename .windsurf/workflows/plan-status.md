---
description: Display the execution status of a plan by parsing frontmatter metadata.
auto_execution_mode: 1
---

# plan-status

This workflow delegates to the agent skill at `skills/plan/plan-status/`.

## Instructions

1. Read the skill manifest: `skills/plan/plan-status/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - 01_INTENT.md
   - 02_PROCEDURE.md
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/plan/plan-status/`
- **References:** `references/`
- **Scripts:** `scripts/`

## Keywords

`plan,status progress,tracking`
