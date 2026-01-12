---
description: Orchestrator skill for the `task` skillset. Manages bounded work units with
single-file tasks stored in `.tasks/`, skepticism-aware hashing, and staleness detection.
auto_execution_mode: 1
---

# task

This workflow delegates to the agent skill at `skills/task/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/task/`
- **References:** `references/`
