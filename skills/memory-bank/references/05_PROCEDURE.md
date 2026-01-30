# Procedure

## Full Update Workflow

Use this procedure for comprehensive Memory Bank updates after significant work.

### Step 1: Read Current Memory Bank State

Read all Memory Bank files to understand the current state:

```
llm_docs/memory/memory-index.md
llm_docs/memory/activeContext.md
llm_docs/memory/progress.md
llm_docs/memory/systemPatterns.md
llm_docs/memory/techContext.md
llm_docs/memory/productContext.md
llm_docs/memory/projectbrief.md
llm_docs/memory/changeLog.md
llm_docs/memory/changeLog-index.md
llm_docs/memory/codeInventory.md
```

If files don't exist, proceed to initialization (see 06_FAILURES.md).

### Step 2: Identify What Changed

Analyze recent work and identify what needs updating:

**Ask yourself:**
- What work was completed since the last update?
- Were any architectural decisions made?
- Did we discover new patterns or constraints?
- Did dependencies or APIs change?
- Did requirements or success criteria change?
- Are there new features to track in progress?

### Step 3: Determine Which Files to Update

Based on what changed, determine which files need updates:

| Change Type | Files to Update |
|-------------|-----------------|
| Any Memory Bank update | `changeLog.md` |
| Completed work, current focus changed | `activeContext.md`, `progress.md` |
| Architectural decision, new pattern | `systemPatterns.md`, `activeContext.md` |
| New dependency, API change | `techContext.md`, `activeContext.md` |
| Feature rationale clarified | `productContext.md` |
| Requirements changed | `projectbrief.md`, `activeContext.md` |
| New memory file added | `memory-index.md` |
| Added/removed/renamed classes, interfaces, functions | `codeInventory.md`, `changeLog.md` |
| changeLog exceeds 100 entries | Archive oldest 50, update `changeLog-index.md` |

### Step 4: Update Files Systematically

For each file that needs updating, follow the file-specific guidelines below.

#### Updating activeContext.md (Most Frequent)

**Structure:**
```markdown
# Active Context

Last Updated: YYYY-MM-DD HH:MM

## Current Focus
[What you're working on RIGHT NOW]

## Recent Work
[What was completed in the last 1-2 sessions]

## Next Steps
[What needs to happen next]

## Open Questions
[Unresolved issues or decisions needed]

## Blockers
[Anything preventing progress]

## Notes
[Any other relevant context]
```

**Update guidelines:**
- Move old "Current Focus" to "Recent Work"
- Add new "Current Focus" at the top
- Keep only last 2-3 sessions in "Recent Work"
- Archive older content (remove or move to separate file)
- Always update the timestamp

#### Updating progress.md

**Update guidelines:**
- Move completed items from "In Progress" to "Completed Features"
- Add completion dates to completed items
- Add new items to "In Progress" or "Planned"
- Update subtask checkboxes
- Add blockers if any

**Structure:**
```markdown
# Progress Tracker

## Completed Features
- [x] Feature A - Completed YYYY-MM-DD
- [x] Feature B - Completed YYYY-MM-DD

## In Progress
- [ ] Feature C - Started YYYY-MM-DD
  - [x] Subtask 1
  - [ ] Subtask 2

## Planned
- [ ] Feature D
- [ ] Feature E

## Blocked
- [ ] Feature F - Blocked by: [reason]
```

#### Updating systemPatterns.md

**Update guidelines:**
- Add new architectural patterns discovered
- Document new design decisions with rationale
- Update code organization if structure changed
- Add new testing patterns if established
- Document new error handling patterns
- Keep patterns organized by category

#### Updating techContext.md

**Update guidelines:**
- Add new dependencies to the list
- Update API contracts if they changed
- Add new data models
- Update environment variables
- Document new external APIs
- Update deployment configuration if changed

#### Updating productContext.md

**Update guidelines:**
- Add new user stories or use cases
- Document feature rationale when clarified
- Update business logic explanations
- Add key decisions with context
- Document why features exist

#### Updating projectbrief.md

**Update guidelines:**
- Update requirements if they changed
- Modify definition of done if criteria changed
- Update success criteria
- Adjust technology stack if needed
- Update objectives if scope changed

#### Updating memory-index.md

**Update guidelines:**
- Update "Last Updated" timestamp
- Add new files if any were created
- Update file descriptions if they changed
- Keep the index concise and accurate

**Structure:**
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

---

## changeLog Procedures

### changeLog Append Procedure

Perform after every Memory Bank update:

1. **Read changeLog.md** to get current entry count
2. **Check entry count**:
   - If >= 100 entries, run Archive Procedure first
3. **Append new entry** with next sequential number:
   ```markdown
   ---
   
   #[N] - YYYY-MM-DD HH:MM
   **Task:** [Task ID or description]
   **Files Modified:** [List of Memory Bank files updated]
   **Reason:** [Why this update was made]
   **Changes:**
   - [Change 1]
   - [Change 2]
   ```

### changeLog Archive Procedure

Perform when changeLog.md has >= 100 entries:

1. **Identify oldest 50 entries** (entries #1-#50, or the oldest 50 by number)
2. **Create archive file**: `archives/changeLog-YYYY-MM-DD.md`
   - Use today's date in filename
   - Include header with date range and entry numbers
3. **Move oldest 50 entries** to archive file
4. **Update changeLog.md**:
   - Remove archived entries
   - Remaining entries keep their original numbers
5. **Update changeLog-index.md**:
   - Add new archive to the list with:
     - Archive filename
     - Entry number range (#X-#Y)
     - Date range
     - Brief topics covered

**Archive file format:**
```markdown
# Change Log Archive - YYYY-MM-DD

Archived entries from changeLog.md.
Date Range: [First entry date] to [Last entry date]
Entries: #X - #Y

---

[Archived entries here, preserving original format]
```

---

## codeInventory Procedures

### codeInventory Update Procedure

Perform when adding, removing, or renaming classes, interfaces, or functions:

1. **Read codeInventory.md** to understand current state
2. **Identify changes**:
   - New classes/interfaces/functions to add
   - Removed items to delete
   - Renamed items to update
3. **Update entries** following the format:

   **For classes:**
   ```markdown
   ### ClassName
   - **File:** `path/to/file.ext`
   - **Purpose:** [Brief description]
   - **Methods:**
     - `publicMethod(params)` - [Description]
     - `_privateMethod(params)` - [Description]
   ```

   **For interfaces:**
   ```markdown
   ### InterfaceName
   - **File:** `path/to/file.ext`
   - **Purpose:** [Brief description]
   - **Methods:**
     - `methodSignature(params) -> ReturnType`
   ```

   **For standalone functions:**
   ```markdown
   ### functionName
   - **File:** `path/to/file.ext`
   - **Signature:** `functionName(params) -> ReturnType`
   - **Purpose:** [Brief description]
   ```

4. **Update timestamp** at top of file
5. **Verify organization** - keep entries grouped by category (Classes, Interfaces, Functions)

### Step 5: Verify Consistency

After updating files, verify consistency:

**Check:**
- [ ] Timestamps are current
- [ ] Cross-references between files are valid
- [ ] No contradictory information across files
- [ ] All new patterns/decisions are documented
- [ ] Progress tracking is accurate
- [ ] activeContext.md reflects current state

### Step 6: Summary Report

Present a summary of what was updated:

```
Memory Bank Updated ✓

Files updated:
- activeContext.md - [brief description of changes]
- progress.md - [brief description of changes]
- systemPatterns.md - [brief description of changes]
- [other files]

Key updates:
- [Important change 1]
- [Important change 2]
- [Important change 3]

Memory Bank is now current as of [timestamp].
```

---

## Quick Update Procedure

Use this for minor updates to `activeContext.md` only.

### When to Use Quick Update

- Completing a small task
- Changing focus within the same area
- Adding a quick note or blocker
- No architectural or technical changes

### Quick Update Process

1. Read `activeContext.md`
2. Update "Current Focus" and "Recent Work"
3. Update timestamp
4. Append entry to `changeLog.md`
5. Done

---

## Integration with R-P-I Workflows

The Memory Bank should be updated at key points in R-P-I workflows:

### During Research
- Update `activeContext.md` with research findings
- Update `systemPatterns.md` if new patterns discovered

### During Planning
- Update `activeContext.md` with design decisions
- Update `systemPatterns.md` with architectural choices

### During Implementation
- Update `progress.md` as phases complete
- Update `activeContext.md` with current state

### During Review
- Update all relevant files with final state
- Update `progress.md` with completed features
- Update `systemPatterns.md` with lessons learned

---

## Best Practices

1. **Update frequently but not excessively** - After significant work, not every edit
2. **Keep activeContext.md current** - This is the most important file
3. **Be concise** - Memory Bank is for essential context, not detailed logs
4. **Use timestamps** - Always update "Last Updated" fields
5. **Cross-reference** - Link between files when relevant
6. **Remove stale info** - Archive or delete outdated context
7. **Maintain consistency** - Ensure no contradictions across files
