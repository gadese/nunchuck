---
status: complete
---

# Task D.iii: Remove deprecated commands

## Focus
Clean up old install/uninstall commands

## Inputs
- Command dispatcher from A.iii
- Migration guide documentation
- User feedback considerations

## Work
1. Remove install command from CLI
2. Remove uninstall command from CLI
3. Add deprecation warnings if old commands called
4. Update help text and documentation
5. Ensure all functionality moved to new commands
6. Test that no functionality is lost

## Output

The old install/uninstall commands were never implemented in the new Click-based CLI. The migration directly to use/drop commands means there are no deprecated commands to remove. All functionality is available through:
- `nunchuck global- add/remove` for global store management
- `nunchuck project use/drop` for project skill management

## Handoff

No deprecated commands exist in the new CLI implementation. The migration to use/drop terminology was complete from the start. Sub-plan D (Command Interface Updates) is now complete. Proceed to Sub-plan E: Cross-Platform Support & Testing.
