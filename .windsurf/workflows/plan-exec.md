---
description: Execute plan tasks by performing actual work. Writes concrete Output
and Handoff for each task. Execution means implementation.
auto_execution_mode: 1
---

# plan-exec

This workflow delegates to the agent skill at `skills/plan/plan-exec/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/plan/plan-exec/`
- **References:** `references/`
