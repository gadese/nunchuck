---
description: Select a task by writing its ID to `.tasks/.active`. Prints the selected
task path and any suspicion flags (stale, hash mismatch) to encourage skepticism.
auto_execution_mode: 1
---

# task-select

This workflow delegates to the agent skill at `skills/task/task-select/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/task/task-select/`
- **References:** `references/`
