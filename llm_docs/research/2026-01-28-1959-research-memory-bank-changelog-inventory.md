# Research: Memory Bank changeLog and Code Inventory

**Date:** 2026-01-28
**Task:** Add changeLog.md and code inventory files to the memory-bank skill

---

## 1. Current State

### 1.1 Memory Bank Skill Structure

**Location:** `skills/memory-bank/`

**Files:**
- `SKILL.md` - Skill manifest with metadata and references
- `README.md` - Usage documentation
- `references/` - 7 reference files (00-06)

**Current Core Memory Files (7 files):**
1. `memory-index.md` - Index of all memory files
2. `projectbrief.md` - Project requirements and definition of done
3. `productContext.md` - Feature rationale and business logic
4. `activeContext.md` - Current session state (most frequently updated)
5. `systemPatterns.md` - Architectural patterns and tech decisions
6. `techContext.md` - Dependencies, APIs, schema, environment
7. `progress.md` - Feature completion checklist

### 1.2 Problem Statement

**activeContext.md Update Behavior (from `05_PROCEDURE.md:79-84`):**
```markdown
**Update guidelines:**
- Move old "Current Focus" to "Recent Work"
- Add new "Current Focus" at the top
- Keep only last 2-3 sessions in "Recent Work"
- Archive older content (remove or move to separate file)
```

**Issue:** Historical context is lost when `activeContext.md` is pruned. Information about past work, decisions, and context is discarded with no permanent record.

### 1.3 Current Constraints

From `04_NEVER.md`:
- "NEVER change the 7-file structure of the Memory Bank"
- "NEVER add custom files without documenting them in `memory-index.md`"

These rules need updating to accommodate the new files while maintaining structure integrity.

---

## 2. Requirements Analysis

### 2.1 Feature 1: changeLog.md

**Purpose:** Permanent chronological record of all Memory Bank changes.

**Requirements:**
- Append an entry on every Memory Bank update call
- Each entry includes:
  - Timestamp
  - Summary of content changes
  - Reason for the update
  - Task identifier (if available)
- Archive entries older than 100 changes to separate files
- Archived files available for agent reading but not read by default

**Entry Format (proposed):**
```markdown
### [YYYY-MM-DD HH:MM] - Entry #N

**Task:** [task identifier or "N/A"]
**Files Modified:** [list of files]
**Reason:** [why the update was made]
**Changes:**
- [summary of change 1]
- [summary of change 2]
```

**Archival Behavior:**
- When entries exceed 100, move oldest entries to `changeLog-archive-YYYYMMDD.md`
- Archive files stored in `llm_docs/memory/archives/`
- Archives not read by default but available on request

### 2.2 Feature 2: Code Inventory Files

**Purpose:** Repertoire of existing code structures (classes, interfaces, functions) with brief overviews and method signatures.

**Requirements:**
- Not overly descriptive
- Documents what exists
- Includes:
  - Class names with brief purpose
  - Method signatures for each class
  - Interface definitions
  - Standalone functions
- Updated when code structure changes significantly

**Proposed Files:**
- `codeInventory.md` - Single file inventory OR
- `codeInventory/` - Directory with per-module inventories (for larger projects)

**Entry Format (proposed):**
```markdown
## module_name

### ClassName
Brief description of the class purpose.

**Methods:**
- `method_name(param1: Type, param2: Type) -> ReturnType` - Brief description
- `other_method() -> None` - Brief description

### function_name
`function_name(param: Type) -> ReturnType`
Brief description.
```

---

## 3. Integration Points

### 3.1 Files Requiring Modification

| File | Change Type | Description |
|------|-------------|-------------|
| `SKILL.md` | Metadata | Add new reference file(s) |
| `README.md` | Documentation | Document new files and usage |
| `references/01_SUMMARY.md` | Structure | Update file count and add descriptions |
| `references/02_TRIGGERS.md` | Triggers | Add triggers for when to update changeLog/inventory |
| `references/03_ALWAYS.md` | Rules | Add rules for changeLog entries |
| `references/04_NEVER.md` | Rules | Update "7-file structure" rule, add new prohibitions |
| `references/05_PROCEDURE.md` | Procedure | Add changeLog append procedure, inventory update procedure |
| `references/06_FAILURES.md` | Templates | Add templates for new files, archive handling |

### 3.2 New Reference Files (Optional)

Consider adding:
- `07_CHANGELOG.md` - Dedicated instructions for changeLog management
- `08_INVENTORY.md` - Dedicated instructions for code inventory management

### 3.3 Memory Bank File Structure (Updated)

**From 7 to 9+ core files:**
1. `memory-index.md` - Index of all memory files
2. `projectbrief.md` - Project requirements and definition of done
3. `productContext.md` - Feature rationale and business logic
4. `activeContext.md` - Current session state
5. `systemPatterns.md` - Architectural patterns and tech decisions
6. `techContext.md` - Dependencies, APIs, schema, environment
7. `progress.md` - Feature completion checklist
8. **`changeLog.md`** - Chronological record of all changes (NEW)
9. **`codeInventory.md`** - Code structure inventory (NEW)

**Additional directories:**
- `archives/` - For archived changeLog files

---

## 4. Behavioral Changes

### 4.1 changeLog Append Procedure

**On every Memory Bank update:**
1. Read current `changeLog.md`
2. Count existing entries
3. If entries >= 100:
   - Archive oldest 50 entries to `archives/changeLog-archive-YYYYMMDD.md`
   - Remove archived entries from `changeLog.md`
4. Append new entry with:
   - Current timestamp
   - Task ID (from context or "N/A")
   - Files modified
   - Reason for update
   - Change summary
5. Save `changeLog.md`

### 4.2 Code Inventory Update Triggers

Update `codeInventory.md` when:
- New classes, interfaces, or functions are added
- Method signatures change significantly
- Code is refactored to change structure
- At end of significant implementation phases

**NOT updated for:**
- Internal implementation changes
- Bug fixes that don't change signatures
- Documentation changes

### 4.3 Reading Behavior Changes

**Default Read (session start):**
- `memory-index.md`, `activeContext.md` (unchanged)
- `changeLog.md` - NOT read by default (too verbose)
- `codeInventory.md` - Read on implementation work

**On-demand Read:**
- `changeLog.md` - When historical context needed
- `archives/` - When deeper history needed

---

## 5. Design Decisions

### 5.1 Single changeLog.md vs Dated Files

**Decision:** Single `changeLog.md` with archival

**Rationale:**
- Simpler to append to one file
- Archival at 100 entries keeps active file manageable
- Archives available when needed

### 5.2 Single codeInventory.md vs Directory

**Decision:** Single `codeInventory.md` initially

**Rationale:**
- Simpler for most projects
- Can split into directory structure later if needed
- Most agent workspaces are medium-sized codebases

### 5.3 Entry Count vs Date-based Archival

**Decision:** Entry count (100 entries)

**Rationale:**
- User-specified requirement
- More predictable file sizes
- Easier to implement and verify

---

## 6. File Templates

### 6.1 changeLog.md Template

```markdown
# Change Log

This file maintains a chronological record of all Memory Bank updates.

---

## Entries

<!-- Newest entries at the top -->
```

### 6.2 codeInventory.md Template

```markdown
# Code Inventory

Last Updated: YYYY-MM-DD

This file catalogs the codebase structure: classes, interfaces, and functions with their signatures.

---

## Overview

[Brief project structure overview]

---

## Modules

<!-- Organized by module/directory -->
```

### 6.3 Archive File Template

```markdown
# Change Log Archive

Archived: YYYY-MM-DD
Entries: #N to #M

---

## Entries

[Archived entries]
```

---

## 7. Open Questions

1. **Code inventory automation:** Should the agent attempt to auto-generate the initial inventory by scanning the codebase, or should it be populated manually over time?

2. **Inventory granularity:** Should private methods be included, or only public APIs?

3. **Archive retention:** Should there be a maximum number of archive files, or keep all indefinitely?

---

## 8. References

- `@/Users/gabriel.descoteaux/Documents/Projects/nunchuck/skills/memory-bank/SKILL.md`
- `@/Users/gabriel.descoteaux/Documents/Projects/nunchuck/skills/memory-bank/README.md`
- `@/Users/gabriel.descoteaux/Documents/Projects/nunchuck/skills/memory-bank/references/05_PROCEDURE.md:79-84` (current pruning behavior)
- `@/Users/gabriel.descoteaux/Documents/Projects/nunchuck/skills/memory-bank/references/04_NEVER.md:25-28` (7-file structure rule)
