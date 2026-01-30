# Always

## Required Behaviors

### Read Memory Bank at Session Start
- **ALWAYS** read `memory-index.md` and `activeContext.md` at the start of every session
- **ALWAYS** check if Memory Bank files exist before attempting to read them
- **ALWAYS** use Memory Bank context to inform your work

### Update activeContext.md Frequently
- **ALWAYS** update `activeContext.md` after significant actions
- **ALWAYS** move old "Current Focus" to "Recent Work" when updating
- **ALWAYS** keep only the last 2-3 sessions in "Recent Work"
- **ALWAYS** remove or archive older content to keep the file focused

### Maintain Timestamps
- **ALWAYS** update "Last Updated" timestamps when modifying files
- **ALWAYS** use format: `YYYY-MM-DD HH:MM` for timestamps
- **ALWAYS** include completion dates when marking features as done

### Cross-Reference Between Files
- **ALWAYS** link between files when relevant (e.g., "See systemPatterns.md for architecture")
- **ALWAYS** ensure information is consistent across all files
- **ALWAYS** verify cross-references are valid after updates

### Keep Files Concise
- **ALWAYS** focus on essential context, not detailed logs
- **ALWAYS** remove stale information to keep files current
- **ALWAYS** archive outdated content rather than accumulating it

### Verify Consistency
After updating, **ALWAYS** check:
- Timestamps are current
- Cross-references are valid
- No contradictory information exists across files
- All new patterns/decisions are documented
- Progress tracking is accurate

### Use Structured Formats
- **ALWAYS** maintain the defined structure for each file type
- **ALWAYS** use markdown formatting consistently
- **ALWAYS** use checkboxes for progress tracking (`- [ ]` or `- [x]`)

### Preserve Context Across Sessions
- **ALWAYS** ensure enough context is captured for future sessions
- **ALWAYS** document "why" decisions were made, not just "what"
- **ALWAYS** note open questions and blockers clearly

### Maintain changeLog
- **ALWAYS** append to `changeLog.md` on every Memory Bank update
- **ALWAYS** include timestamp, task ID, files modified, reason, and changes in each entry
- **ALWAYS** use explicit entry numbering (#1, #2, etc.) in changeLog
- **ALWAYS** archive when changeLog exceeds 100 entries
- **ALWAYS** update `changeLog-index.md` when creating new archives

### Maintain codeInventory
- **ALWAYS** update `codeInventory.md` when adding/removing/renaming classes, interfaces, or public functions
- **ALWAYS** include private methods in codeInventory
- **ALWAYS** review codeInventory at end of major implementation phases
