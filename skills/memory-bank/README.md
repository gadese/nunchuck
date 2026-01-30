# Memory Bank Skill

A global skill for managing workspace-specific Memory Bank files that provide persistent cross-session context for AI agents.

## Overview

The Memory Bank skill manages a structured knowledge base in `llm_docs/memory/` that maintains project context across sessions. It consists of 10 core files that track different aspects of the project:

1. **memory-index.md** - Index of all memory files
2. **projectbrief.md** - Project requirements and definition of done
3. **productContext.md** - Feature rationale and business logic
4. **activeContext.md** - Current session state (most frequently updated)
5. **systemPatterns.md** - Architectural patterns and tech decisions
6. **techContext.md** - Dependencies, APIs, schema, environment
7. **progress.md** - Feature completion checklist
8. **changeLog.md** - Chronological record of Memory Bank updates
9. **changeLog-index.md** - Index of changeLog archives
10. **codeInventory.md** - Inventory of classes, interfaces, and functions

Additionally, the `archives/` directory stores archived changeLog entries.

## When to Use

### Read Memory Bank
- **At the start of every session** - Understand where work left off
- **Before implementation** - Get context on requirements and patterns
- **When user mentions context** - Provide continuity from previous sessions
- **When making architectural decisions** - Ensure consistency with established patterns

### Update Memory Bank
- **After significant work** - Capture completed phases and decisions
- **After feature completion** - Update progress tracking
- **After architectural changes** - Document new patterns
- **At end of work sessions** - Preserve state for next session
- **When context changes significantly** - Keep Memory Bank current

## Usage

### Standalone Invocation

```
/memory-bank
```

This will guide you through updating the Memory Bank based on recent work.

### Integration with R-P-I Workflows

The Memory Bank is automatically integrated with R-P-I workflows:

- **Research Phase** - Read Memory Bank to understand context, update with findings
- **Plan Phase** - Read Memory Bank to inform planning, update with decisions
- **Implement Phase** - Read Memory Bank for implementation details, update with progress
- **Review Phase** - Update Memory Bank with lessons learned and next steps

## Quick Update vs Full Update

### Quick Update (activeContext.md only)

Use when:
- Completing a small task
- Changing focus within the same area
- Adding a quick note or blocker

Process:
1. Read `activeContext.md`
2. Update "Current Focus" and "Recent Work"
3. Update timestamp

### Full Update (multiple files)

Use when:
- Completing a major feature
- Making architectural decisions
- Discovering important patterns
- Changing dependencies or APIs
- Updating requirements

Process:
1. Read all Memory Bank files
2. Identify what changed
3. Update relevant files
4. Verify consistency
5. Provide summary report

## File-Specific Guidelines

### activeContext.md
**Update frequency**: Very high (after every significant action)
**Purpose**: Track current work and immediate next steps
**Keep**: Last 2-3 sessions only

### progress.md
**Update frequency**: High (when features start/complete)
**Purpose**: Track feature completion status
**Keep**: All features (archive completed ones periodically)

### systemPatterns.md
**Update frequency**: Medium (when patterns emerge or change)
**Purpose**: Document architectural decisions and patterns
**Keep**: All current patterns (remove obsolete ones)

### techContext.md
**Update frequency**: Medium (when dependencies or APIs change)
**Purpose**: Track technical dependencies and contracts
**Keep**: All current technical context

### productContext.md
**Update frequency**: Low (when feature rationale is clarified)
**Purpose**: Document why features exist and business logic
**Keep**: All product context

### projectbrief.md
**Update frequency**: Low (when requirements change)
**Purpose**: Define project scope and success criteria
**Keep**: Current requirements only

### memory-index.md
**Update frequency**: Low (when structure changes)
**Purpose**: Index all memory files
**Keep**: Current index only

### changeLog.md
**Update frequency**: Very high (on every Memory Bank update)
**Purpose**: Chronological record of all Memory Bank changes
**Keep**: Last 100 entries (archive older entries)
**Format**: Numbered entries (#1, #2, etc.) with timestamp, task, files modified, reason, and changes

### changeLog-index.md
**Update frequency**: Low (when archives are created)
**Purpose**: Index of archived changeLog entries
**Keep**: All archive references

### codeInventory.md
**Update frequency**: Medium (when adding/removing/renaming code elements)
**Purpose**: Inventory of classes, interfaces, and functions
**Keep**: All current code elements (remove deleted items)
**Include**: Both public and private methods

## Best Practices

1. **Update frequently but not excessively** - After significant work, not every edit
2. **Keep activeContext.md current** - This is the most important file
3. **Be concise** - Memory Bank is for essential context, not detailed logs
4. **Use timestamps** - Always update "Last Updated" fields
5. **Cross-reference** - Link between files when relevant
6. **Remove stale info** - Archive or delete outdated context
7. **Maintain consistency** - Ensure no contradictions across files

## Initialization

If a workspace doesn't have a Memory Bank, this skill will:
1. Create `llm_docs/memory/` directory
2. Initialize all 10 core files with templates
3. Create `archives/` directory for changeLog archives
4. Populate with current project information
5. Inform user that Memory Bank was initialized

## Error Handling

The skill handles common errors:
- **Missing Memory Bank** - Initializes structure
- **Corrupted files** - Creates backups and re-initializes
- **Stale information** - Prompts for update
- **Inconsistent information** - Identifies and resolves conflicts
- **Permission errors** - Reports and suggests fixes

## Global Skill

This is a **global skill** usable across multiple workspaces and projects. Each workspace maintains its own `llm_docs/memory/` directory with workspace-specific content.

## References

See `references/` directory for detailed instructions:
- `00_ROUTER.md` - Routing logic
- `01_SUMMARY.md` - Purpose and structure
- `02_TRIGGERS.md` - When to read/update
- `03_ALWAYS.md` - Required behaviors
- `04_NEVER.md` - Prohibited behaviors
- `05_PROCEDURE.md` - Update procedures
- `06_FAILURES.md` - Error handling
- `07_CHANGELOG.md` - changeLog format and procedures
- `08_INVENTORY.md` - codeInventory format and conventions
