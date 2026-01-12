---
description: Create a new task file in `.tasks/<id>.md` from template. Sets timestamps,
auto_execution_mode: 1
---

# task-create

This workflow delegates to the agent skill at `skills/task/task-create/`.

## Instructions

1. Read the skill manifest: `skills/task/task-create/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - 00_INSTRUCTIONS.md
   - 01_PROCEDURE.md
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/task/task-create/`
- **References:** `references/`

## Keywords

`task,create new,init start`
