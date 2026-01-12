---
description: Orchestrator skill for the `prompt` skillset. Separates intent formation from
execution to protect humans from premature or misaligned action.
auto_execution_mode: 1
---

# prompt

This workflow delegates to the agent skill at `skills/prompt/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/prompt/`
- **References:** `references/`
