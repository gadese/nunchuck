# Task B.iii: Implement skill removal logic

## Focus
Remove skills from global store safely

## Inputs
- Store class from B.i
- Skill metadata index from B.ii
- Project reference tracking

## Work
1. Implement `nunchuck remove <name>` command
2. Check if skill is in use by any projects
3. Prompt user if skill has dependencies
4. Remove skill directory and update index
5. Clean up any orphaned files
6. Test removal with and without dependencies
