---
status: complete
---

# Task C.iii: Implement auto-detection logic

## Focus
Detect IDE and generate appropriate adapters

## Inputs
- AdapterGenerator from C.i and C.ii
- Project directory structure
- IDE configuration file patterns

## Work
1. Implement IDE detection (check .windsurf/, .cursor/)
2. Create `nunchuck adapter` auto-detect command
3. Handle multiple IDEs in same project
4. Add explicit flags (--windsurf, --cursor)
5. Manage adapter updates and conflicts
6. Test auto-detection scenarios

## Output

Auto-detection logic was already implemented in Task C.i:
- Detects Windsurf by checking for .windsurf directory
- Detects Cursor by checking for .cursor directory
- Supports both IDEs in the same project
- Explicit flags (--windsurf, --cursor) override auto-detection
- Error message when no IDE detected

## Handoff

Auto-detection is complete. The adapter command automatically detects IDEs and generates appropriate adapters. Sub-plan C (Adapter Generation Migration) is now complete. Proceed to Sub-plan D: Command Interface Updates.
