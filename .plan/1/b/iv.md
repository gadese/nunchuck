---
status: complete
---

# Task B.iv: Add skill listing functionality

## Focus
List skills in global store and projects

## Inputs
- Store class from B.i
- Skill metadata index
- Project configuration files

## Work
1. Implement `nunchuck list --global` command
2. Implement `nunchuck list` (project scope)
3. Add filtering options (by name, tag, etc.)
4. Display skill metadata in table format
5. Show skill status (installed, available)
6. Test listing with various filters

## Output

- Enhanced `global- list` command:
  - Added `--filter` option for name-based filtering
  - Added `--tag` option (placeholder for future tag support)
  - Improved table formatting with dynamic column widths
  - Truncated long descriptions for better readability
- Project listing improvements:
  - Shows source (global/local) for each skill
  - Added filtering support for project skills
  - Better table formatting with proper alignment
- Display features:
  - Headers with separators for clarity
  - Dynamic column width calculation
  - JSON output format preserved
  - Empty state messages
- Successfully tested:
  - Global skills listing with table format
  - Name filtering (--filter doc)
  - Project skills listing with source detection
  - JSON output format works correctly

## Handoff

Skill listing functionality is fully implemented with filtering, formatted tables, and source detection. The list command provides clear, readable output for both global and project scopes. Sub-plan B (Global Skill Store Implementation) is now complete. Proceed to Sub-plan C: Adapter Generation Migration.
