---
description: Merges markdown chunks back into a single document, reversing the split
operation with integrity checks.
auto_execution_mode: 1
---

# md-merge

This workflow delegates to the agent skill at `skills/md/md-merge/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/md/md-merge/`
- **References:** `references/`
