---
description: Materialize the current conversation into a new docs/planning/phase-N plan
auto_execution_mode: 1
---

# plan-create

This workflow delegates to the agent skill at `skills/plan/plan-create/`.

## Instructions

1. Read the skill manifest: `skills/plan/plan-create/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - 00_INSTRUCTIONS.md
   - 01_INTENT.md
   - 02_PRECONDITIONS.md
   - 03_SCRIPTS.md
   - 04_PROCEDURE.md
   - 05_TEMPLATES.md
   - 06_EDGE_CASES.md
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/plan/plan-create/`
- **References:** `references/`
- **Scripts:** `scripts/`

## Keywords

`phase,plan planning,sub-plan sub-plans,subtask subtasks,task tasks,sketch draft`
