---
description: Orchestrates markdown document workflows with deterministic operations
(split, merge, lint) and agent review.
auto_execution_mode: 1
---

# md

This workflow delegates to the agent skill at `skills/md/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/md/`
- **References:** `references/`

