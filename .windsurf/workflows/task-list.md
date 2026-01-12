---
description: List tasks in `.tasks/` with derived flags (stale, hash mismatch).
Supports filtering by state and staleness. Stable ordering by updated_at.
auto_execution_mode: 1
---

# task-list

This workflow delegates to the agent skill at `skills/task/task-list/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/task/task-list/`
- **References:** `references/`

