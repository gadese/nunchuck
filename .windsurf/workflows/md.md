---
description: Orchestrates markdown document workflows with deterministic operations
auto_execution_mode: 1
---

# md

This workflow delegates to the agent skill at `skills/md/`.

## Instructions

1. Read the skill manifest: `skills/md/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/md/`
- **References:** `references/`

## Skillset

This is an orchestrator skill with member skills.

- **Members:** md-split, md-merge, md-review

To run the full pipeline, invoke this workflow.
To run individual skills, use their specific workflows.

## Keywords

`markdown,split merge,lint review`
