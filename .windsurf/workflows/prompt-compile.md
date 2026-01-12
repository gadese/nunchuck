---
description: Compile the YAML artifact into PROMPT.md with deterministic structure.
A final agent pass polishes for fluidity, conciseness, and correctness.
auto_execution_mode: 1
---

# prompt-compile

This workflow delegates to the agent skill at `skills/prompt/prompt-compile/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/prompt/prompt-compile/`
- **References:** `references/`
