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
