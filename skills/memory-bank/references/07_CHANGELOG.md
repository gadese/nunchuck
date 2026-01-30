# changeLog Reference

## Purpose

The `changeLog.md` file maintains a chronological record of all Memory Bank updates. It provides an audit trail of what changed, when, and why—enabling historical context and debugging of Memory Bank evolution.

## Entry Format

Each changeLog entry follows this structure:

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

### Field Descriptions

| Field | Description | Example |
|-------|-------------|---------|
| `#[N]` | Sequential entry number | `#42` |
| Timestamp | Date and time of update | `2026-01-28 14:30` |
| Task | Task ID or brief description | `Implement user auth` |
| Files Modified | Memory Bank files that were updated | `activeContext.md, progress.md` |
| Reason | Why the update was necessary | `Completed Phase 2 of auth implementation` |
| Changes | Bullet list of specific changes | `- Updated Current Focus`, `- Marked auth feature complete` |

## Examples

### Example 1: After Completing Work

```markdown
---

#15 - 2026-01-28 14:30
**Task:** User Authentication Implementation
**Files Modified:** activeContext.md, progress.md, systemPatterns.md
**Reason:** Completed Phase 2 of authentication implementation
**Changes:**
- Updated Current Focus to Phase 3
- Marked JWT token generation as complete in progress.md
- Added authentication pattern to systemPatterns.md
```

### Example 2: After Architectural Decision

```markdown
---

#16 - 2026-01-28 16:45
**Task:** Database Selection
**Files Modified:** activeContext.md, techContext.md, systemPatterns.md
**Reason:** Made decision on database technology
**Changes:**
- Documented PostgreSQL selection in techContext.md
- Added data access patterns to systemPatterns.md
- Updated Current Focus to reflect decision made
```

### Example 3: Quick Update

```markdown
---

#17 - 2026-01-28 17:00
**Task:** Session end
**Files Modified:** activeContext.md
**Reason:** End of work session
**Changes:**
- Captured current state for next session
- Added blocker: waiting for API credentials
```

## Archive Procedure

### When to Archive

Archive when `changeLog.md` contains **100 or more entries**.

### Archive Steps

1. **Count entries** in changeLog.md
2. **If >= 100 entries**:
   - Identify the oldest 50 entries
   - Create archive file: `archives/changeLog-YYYY-MM-DD.md`
   - Move oldest 50 entries to archive
   - Update changeLog.md (remove archived entries)
   - Update changeLog-index.md with new archive

### Archive File Format

```markdown
# Change Log Archive - YYYY-MM-DD

Archived entries from changeLog.md.
Date Range: [First entry date] to [Last entry date]
Entries: #X - #Y

---

[Archived entries here, preserving original format and numbering]
```

### changeLog-index.md Format

```markdown
# Change Log Index

Index of archived changeLog entries.

## Archives
- **archives/changeLog-2026-01-15.md** - Entries #1-#50 (2025-12-01 to 2026-01-15) - Initial setup, auth implementation
- **archives/changeLog-2026-02-28.md** - Entries #51-#100 (2026-01-16 to 2026-02-28) - API development, testing
```

## Best Practices

1. **Be concise** - Each entry should be brief but informative
2. **Be specific** - List actual files modified, not "various files"
3. **Include context** - The "Reason" field helps future readers understand why
4. **Maintain numbering** - Never reuse entry numbers, even after archiving
5. **Archive promptly** - Don't let changeLog grow beyond 100 entries
