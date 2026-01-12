---
description: Execute the forged prompt exactly as written. Requires explicit consent
and a ready artifact. Deletes artifact after successful execution.
auto_execution_mode: 1
---

# prompt-exec

This workflow delegates to the agent skill at `skills/prompt/prompt-exec/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/prompt/prompt-exec/`
- **References:** `references/`
