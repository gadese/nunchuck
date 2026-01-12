---
status: complete
---

# Task A.iv: Add help and validation commands

## Focus
Implement help system and skill validation

## Inputs
- Existing validation.py logic
- Agent Skills specification
- Command dispatcher from A.iii

## Work
1. Migrate validation logic to new CLI structure
2. Implement `nunchuck validate` with detailed error reporting
3. Create help system for each command group
4. Add skill metadata validation
5. Implement `nunchuck --help` hierarchy
6. Test validation with sample skills

## Output

- Enhanced validation command with:
  - Path existence validation
  - Dry-run support
  - Verbose mode for detailed error reporting
  - Proper JSON and human-readable output formats
- Added help command with hierarchical support:
  - `nunchuck help` shows main help
  - `nunchuck help <group>` shows group help
  - `nunchuck help <group> <subcommand>` shows subcommand help
- Successfully tested:
  - Validation catches skill errors (missing pipelines metadata)
  - Help system works for all command groups
  - JSON output format works correctly
  - Human-readable output with verbose details

## Handoff

Help system and validation are fully integrated into the CLI. All commands have proper validation, error handling, and help text. The validation command provides detailed feedback for skill compliance with the Agent Skills specification. Sub-plan A (Core CLI Infrastructure) is now complete. Proceed to Sub-plan B: Global Skill Store Implementation.
