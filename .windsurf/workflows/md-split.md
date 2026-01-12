---
description: Splits a Markdown file by H2 headings into numbered documents and generates
auto_execution_mode: 1
---

# md-split

This workflow delegates to the agent skill at `skills/md/md-split/`.

## Instructions

1. Read the skill manifest: `skills/md/md-split/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - 00_INDEX.md
   - 01_SUMMARY.md
   - 02_TRIGGERS.md
   - 03_ALWAYS.md
   - 04_NEVER.md
   - 05_PROCEDURE.md
   - 06_FAILURES.md
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/md/md-split/`
- **References:** `references/`
- **Scripts:** `scripts/`

## Keywords

`markdown,split chunking`
