---
description: Orchestrator skill for the `task` skillset. Standardizes task creation and lifec
auto_execution_mode: 1
---

# task

This workflow delegates to the agent skill at `skills/task/`.

## Instructions

1. Read the skill manifest: `skills/task/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - README.md
   - USAGE.md
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/task/`
- **References:** `references/`

## Skillset

This is an orchestrator skill with member skills.

- **Members:** task-create, task-validate, task-review, task-activate, task-invalidate, task-status, task-list, task-next, task-prev
- **Default Pipeline:** task-create -> task-validate -> task-activate

To run the full pipeline, invoke this workflow.
To run individual skills, use their specific workflows.


