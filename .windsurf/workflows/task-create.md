---
description: Create a new task directory with 00_TASK.md from template.
auto_execution_mode: 1
---

# task-create

This workflow delegates to the agent skill at `skills/task/task-create/`.

## Instructions

1. Read the skill manifest: `skills/task/task-create/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - 00_INSTRUCTIONS.md
   - 01_INTENT.md
   - 02_PROCEDURE.md
   - 03_OUTPUTS.md
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/task/task-create/`
- **References:** `references/`
- **Scripts:** `scripts/`

## Keywords

`task,create new,initialize init,start begin`
