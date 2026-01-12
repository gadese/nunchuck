---
status: complete
---

# Task C.i: Migrate Windsurf adapter generation

## Focus
Convert scripts/adapter/windsurf.sh to Python

## Inputs
- scripts/adapter/windsurf.sh
- Windsurf workflow format specification
- Skill metadata structure

## Work
1. Create AdapterGenerator class for Windsurf
2. Parse skill SKILL.md files for workflow info
3. Generate .windsurf/workflows/*.md files
4. Handle workflow templates and variables
5. Preserve existing functionality
6. Test with sample skills

## Output

- Created `src/nunchuck/adapter.py` with AdapterGenerator class:
  - Parses skill SKILL.md files for metadata
  - Generates Windsurf workflows with proper frontmatter
  - Generates Cursor rules for IDE integration
  - Handles skillset-specific information (members, pipelines)
  - Skips meta-skills (index, adapter, etc.)
- Updated CLI integration:
  - `adapter generate --windsurf` command works
  - `adapter generate --cursor` command works
  - `adapter generate --clean` removes adapters
  - Auto-detection of IDE based on directory presence
- Successfully tested:
  - Generated 28 Windsurf workflows
  - Generated 28 Cursor rules
  - Workflows include proper metadata and instructions
  - Skillset information preserved (members, pipelines)
  - Scripts directory detection works

## Handoff

Windsurf adapter generation is fully migrated from shell script to Python. The AdapterGenerator class provides a clean, extensible way to generate IDE adapters from skills. Proceed to Task C.ii to migrate Cursor adapter generation.
