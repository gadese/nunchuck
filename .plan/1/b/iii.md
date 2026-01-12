---
status: complete
---

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

## Output

- Enhanced `Store.remove_skill()` method:
  - Added `force` parameter to bypass dependency checks
  - Checks current project for skill usage
  - Scans multiple locations for skill references
  - Prompts user before removing if dependencies found
  - Cleans up skill directory and updates index
- Dependency checking implementation:
  - Checks `.nunchuck/skills/<name>` directory
  - Checks `skills/<name>` directory  
  - Checks `.nunchuck-<name>` file
  - Scans config files for skill name references
- Updated CLI integration:
  - `--force` flag bypasses all confirmations
  - Clear error messages for missing skills
  - Proper cancellation when user declines
- Successfully tested:
  - Normal removal with confirmation
  - Dependency detection and warning
  - Force removal bypassing dependencies
  - Index properly updated after removal

## Handoff

Skill removal logic is fully implemented with safety checks and dependency awareness. The system warns users before removing skills that are in use and provides a force option for override. Proceed to Task B.iv to add skill listing functionality with filtering and status display.
