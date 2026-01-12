---
description: Agent review for markdown quality, clarity, and structural integrity.
Leverages deterministic lint output as input for subjective assessment.
auto_execution_mode: 1
---

# md-review

This workflow delegates to the agent skill at `skills/md/md-review/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/md/md-review/`
- **References:** `references/`
