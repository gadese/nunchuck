---
description: Orchestrator skill for the `prompt` skillset. Dispatches to member skills in a s
auto_execution_mode: 1
---

# prompt

This workflow delegates to the agent skill at `skills/prompt/`.

## Instructions

1. Read the skill manifest: `skills/prompt/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/prompt/`
- **References:** `references/`

## Skillset

This is an orchestrator skill with member skills.

- **Members:** prompt-forge, prompt-exec
- **Default Pipeline:** prompt-forge -> prompt-exec

To run the full pipeline, invoke this workflow.
To run individual skills, use their specific workflows.


