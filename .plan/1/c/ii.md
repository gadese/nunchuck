# Task C.ii: Migrate Cursor adapter generation

## Focus
Convert scripts/adapter/cursor.sh to Python

## Inputs
- scripts/adapter/cursor.sh
- Cursor rules format specification
- Skill metadata structure

## Work
1. Extend AdapterGenerator for Cursor
2. Generate .cursorrules files
3. Handle skill-specific rule formatting
4. Merge multiple skill rules correctly
5. Preserve existing functionality
6. Test with sample skills
