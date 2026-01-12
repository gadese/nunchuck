---
description: Close a task by setting state to closed, recording close_reason and closed_at.
Recomputes intent hash and clears `.tasks/.active` if it pointed to this task.
auto_execution_mode: 1
---

# task-close

This workflow delegates to the agent skill at `skills/task/task-close/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/task/task-close/`
- **References:** `references/`
