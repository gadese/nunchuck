---
description: Splits a Markdown file by H2 headings into numbered documents and generates
an index file.
auto_execution_mode: 1
---

# md-split

This workflow delegates to the agent skill at `skills/md/md-split/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/md/md-split/`
- **References:** `references/`
- **Scripts:** `scripts/`
