# Failures

## Error Handling and Recovery

### Missing Memory Bank (Initialize)

**Symptom**: `llm_docs/memory/` directory doesn't exist or is empty

**Recovery**:
1. Create `llm_docs/memory/` directory
2. Initialize all 10 core files with templates
3. Create `archives/` directory for changeLog archives
4. Populate with current project information
5. Inform user that Memory Bank was initialized

**Initialization Templates**:

#### memory-index.md
```markdown
# Memory Bank Index

Last Updated: YYYY-MM-DD

## Files
- **projectbrief.md** - Project requirements and definition of done
- **productContext.md** - Feature rationale and business logic
- **activeContext.md** - Current session state
- **systemPatterns.md** - Architectural patterns
- **techContext.md** - Technical dependencies and APIs
- **progress.md** - Feature completion checklist
- **changeLog.md** - Chronological record of Memory Bank updates
- **changeLog-index.md** - Index of changeLog archives
- **codeInventory.md** - Inventory of classes, interfaces, and functions

## Directories
- **archives/** - Archived changeLog entries
```

#### projectbrief.md
```markdown
# Project Brief

Last Updated: YYYY-MM-DD

## Overview
[Project description]

## Objectives
[What this project aims to achieve]

## Requirements
[Key requirements]

## Definition of Done
[Success criteria]

## Technology Stack
[Technologies used]
```

#### productContext.md
```markdown
# Product Context

Last Updated: YYYY-MM-DD

## User Stories
[Key user stories]

## Feature Rationale
[Why features exist]

## Business Logic
[Important business rules]
```

#### activeContext.md
```markdown
# Active Context

Last Updated: YYYY-MM-DD HH:MM

## Current Focus
[What you're working on RIGHT NOW]

## Recent Work
[What was completed recently]

## Next Steps
[What needs to happen next]

## Open Questions
[Unresolved issues]

## Blockers
[Anything preventing progress]
```

#### systemPatterns.md
```markdown
# System Patterns

Last Updated: YYYY-MM-DD

## Architecture
[Architectural patterns]

## Code Organization
[How code is structured]

## Design Decisions
[Key design decisions and rationale]

## Testing Patterns
[Testing approaches]
```

#### techContext.md
```markdown
# Technical Context

Last Updated: YYYY-MM-DD

## Dependencies
[External dependencies]

## APIs
[API contracts and endpoints]

## Data Models
[Key data structures]

## Environment
[Environment variables and configuration]
```

#### progress.md
```markdown
# Progress Tracker

## Completed Features
[None yet]

## In Progress
[Current work]

## Planned
[Future work]

## Blocked
[Blocked items]
```

#### changeLog.md
```markdown
# Change Log

Chronological record of Memory Bank updates.

---

#1 - YYYY-MM-DD HH:MM
**Task:** [Task ID or description]
**Files Modified:** [List of Memory Bank files updated]
**Reason:** [Why this update was made]
**Changes:**
- [Change 1]
- [Change 2]
```

#### changeLog-index.md
```markdown
# Change Log Index

Index of archived changeLog entries.

## Archives
[No archives yet]

<!-- Archive format:
- **archives/changeLog-YYYY-MM-DD.md** - Entries #X-#Y (YYYY-MM-DD to YYYY-MM-DD) - [Topics covered]
-->
```

#### codeInventory.md
```markdown
# Code Inventory

Last Updated: YYYY-MM-DD

Inventory of classes, interfaces, and functions in the codebase.

## Classes
[None documented yet]

<!-- Format:
### ClassName
- **File:** `path/to/file.ext`
- **Purpose:** [Brief description]
- **Methods:**
  - `publicMethod(params)` - [Description]
  - `_privateMethod(params)` - [Description]
-->

## Interfaces
[None documented yet]

## Functions
[None documented yet]

<!-- Format:
### functionName
- **File:** `path/to/file.ext`
- **Signature:** `functionName(params) -> ReturnType`
- **Purpose:** [Brief description]
-->
```

#### Archive File Template (archives/changeLog-YYYY-MM-DD.md)
```markdown
# Change Log Archive - YYYY-MM-DD

Archived entries from changeLog.md.
Date Range: YYYY-MM-DD to YYYY-MM-DD
Entries: #X - #Y

---

[Archived entries here]
```

---

### Corrupted Files

**Symptom**: Memory Bank files exist but contain invalid or corrupted data

**Recovery**:
1. Attempt to read the file
2. If parsing fails, create a backup: `[filename].corrupted.bak`
3. Re-initialize the file with template
4. Inform user about corruption and backup location
5. Ask user if they want to manually recover content from backup

**Example**:
```
Warning: activeContext.md appears corrupted.
- Backup created: activeContext.md.corrupted.bak
- File re-initialized with template
- Please review backup if recovery is needed
```

---

### Stale Information

**Symptom**: Memory Bank files haven't been updated in a long time (timestamps > 1 week old)

**Recovery**:
1. Inform user that Memory Bank appears stale
2. Ask user if they want to update it now or proceed with current information
3. If updating, run full update workflow
4. If proceeding, note the staleness in your working context

**Example**:
```
Notice: Memory Bank last updated 2 weeks ago.
Information may be stale. Would you like me to:
1. Update Memory Bank now (recommended)
2. Proceed with current information
```

---

### Inconsistent Information

**Symptom**: Contradictory information across different Memory Bank files

**Recovery**:
1. Identify the inconsistencies
2. Present them to the user
3. Ask user which information is correct
4. Update files to resolve inconsistencies
5. Verify consistency after updates

**Example**:
```
Inconsistency detected:
- systemPatterns.md says: "Using REST API"
- techContext.md says: "Using GraphQL API"

Which is correct?
```

---

### Missing Individual Files

**Symptom**: Some Memory Bank files exist, but not all 10 core files

**Recovery**:
1. Identify which files are missing
2. Create missing files using templates
3. Inform user which files were created
4. Suggest running full update to populate them

**Example**:
```
Memory Bank incomplete. Created missing files:
- techContext.md
- productContext.md

Recommend running full update to populate these files.
```

---

### Permission Errors

**Symptom**: Cannot read or write Memory Bank files due to permissions

**Recovery**:
1. Report the permission error to user
2. Suggest checking file/directory permissions
3. Provide command to fix permissions if appropriate
4. Wait for user to resolve before proceeding

**Example**:
```
Error: Cannot write to llm_docs/memory/activeContext.md
Permission denied.

Please check file permissions:
chmod 644 llm_docs/memory/*.md
```

---

### Workspace Without llm_docs Directory

**Symptom**: Workspace doesn't have `llm_docs/` directory structure

**Recovery**:
1. Ask user if they want to create Memory Bank structure
2. If yes, create `llm_docs/memory/` and initialize
3. If no, inform user that Memory Bank is not available for this workspace

**Example**:
```
This workspace doesn't have a Memory Bank structure.
Would you like me to create llm_docs/memory/ and initialize it?
```

---

## General Error Handling Principles

1. **Always create backups** before overwriting potentially corrupted files
2. **Always inform the user** about errors and recovery actions taken
3. **Always ask for confirmation** before making destructive changes
4. **Always provide context** about what went wrong and why
5. **Always offer options** when multiple recovery paths exist
