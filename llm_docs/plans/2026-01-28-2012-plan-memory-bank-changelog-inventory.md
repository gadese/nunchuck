# Plan: Memory Bank changeLog and Code Inventory

**Date:** 2026-01-28
**Research:** `llm_docs/research/2026-01-28-1959-research-memory-bank-changelog-inventory.md`
**Task:** Add changeLog.md and codeInventory.md to the memory-bank skill

---

## Design Decisions (Confirmed)

| Decision | Choice |
|----------|--------|
| Code inventory population | Incremental during work |
| Method granularity | Include private methods |
| Archive retention | Keep all indefinitely |
| Archival trigger | 100 entries |
| Archive batch size | 50 oldest entries |

---

## Implementation Phases

### Phase 1: Core File Templates and Structure
**Goal:** Add templates for new files to initialization and failure handling

**Files to modify:**
- [x] `references/06_FAILURES.md` - Add templates for `changeLog.md`, `codeInventory.md`, and archive structure

**Changes:**
1. Update "Initialize all 7 core files" → "Initialize all 10 core files" (line 11)
2. Update `memory-index.md` template to list all 10 files
3. Add `changeLog.md` initialization template (with explicit entry numbering: #1, #2, etc.)
4. Add `changeLog-index.md` initialization template (index of archives with date ranges and topics)
5. Add `codeInventory.md` initialization template
6. Add `archives/` directory creation to initialization steps
7. Add archive file template
8. Update "Missing Individual Files" section to check for 10 files

**Verification:**
- Templates follow existing format conventions
- All required sections present
- **New projects initialize with complete 10-file structure + archives directory**

---

### Phase 2: Update Memory Bank Structure Documentation
**Goal:** Update file count and descriptions across documentation

**Files to modify:**
- [x] `references/01_SUMMARY.md` - Update from 7 to 10 core files, add descriptions
- [x] `references/04_NEVER.md` - Update "7-file structure" rule to "10-file structure"

**Changes:**
1. Add `changeLog.md` to file list with description
2. Add `changeLog-index.md` to file list with description
3. Add `codeInventory.md` to file list with description
4. Update structure constraints

**Verification:**
- File counts consistent across all references
- Descriptions clear and concise

---

### Phase 3: Add Triggers for New Files
**Goal:** Define when to read/update the new files

**Files to modify:**
- [x] `references/02_TRIGGERS.md` - Add triggers for changeLog and codeInventory

**Changes:**
1. Add "When to Read" triggers for codeInventory (before implementation)
2. Add "When to Update" triggers for changeLog (every Memory Bank update)
3. Add "When to Update" triggers for codeInventory:
   - After adding/removing/renaming classes, interfaces, or public functions
   - Review codeInventory at end of major implementation phases
4. Add "When to Update" triggers for changeLog-index.md (when archives are created)

**Verification:**
- Triggers are specific and actionable
- No conflicts with existing triggers

---

### Phase 4: Add Required Behaviors
**Goal:** Define ALWAYS rules for new files

**Files to modify:**
- [x] `references/03_ALWAYS.md` - Add required behaviors for changeLog and codeInventory

**Changes:**
1. Add rule: "ALWAYS append to changeLog.md on every Memory Bank update"
2. Add rule: "ALWAYS include timestamp, task ID, files modified, reason, and changes"
3. Add rule: "ALWAYS use explicit entry numbering (#1, #2, etc.) in changeLog"
4. Add rule: "ALWAYS archive when changeLog exceeds 100 entries"
5. Add rule: "ALWAYS update changeLog-index.md when creating new archives"
6. Add rule: "ALWAYS update codeInventory.md when adding/removing/renaming classes, interfaces, or public functions"
7. Add rule: "ALWAYS include private methods in codeInventory"
8. Add rule: "ALWAYS review codeInventory at end of major implementation phases"

**Verification:**
- Rules are clear and unambiguous
- Consistent with existing rule format

---

### Phase 5: Add Prohibited Behaviors
**Goal:** Define NEVER rules for new files

**Files to modify:**
- [x] `references/04_NEVER.md` - Add prohibited behaviors for changeLog and codeInventory

**Changes:**
1. Add rule: "NEVER skip changeLog entry when updating Memory Bank"
2. Add rule: "NEVER delete archives"
3. Add rule: "NEVER read changeLog by default at session start"
4. Add rule: "NEVER update codeInventory for implementation-only changes"

**Verification:**
- Rules prevent common mistakes
- No conflicts with ALWAYS rules

---

### Phase 6: Add Procedures
**Goal:** Define step-by-step procedures for new file operations

**Files to modify:**
- [x] `references/05_PROCEDURE.md` - Add procedures for changeLog and codeInventory

**Changes:**
1. Update file list in "Step 1: Read Current Memory Bank State" (lines 11-18) to include changeLog.md, codeInventory.md
2. Update memory-index.md structure example (lines 171-174) to include new files
3. Add "changeLog Append Procedure" section:
   - Count entries
   - Archive if >= 100
   - Append new entry
4. Add "changeLog Archive Procedure" section:
   - Create archive file with timestamp
   - Move oldest 50 entries
   - Update changeLog.md
   - Update changeLog-index.md with new archive (date range, topics covered)
5. Add "codeInventory Update Procedure" section:
   - Read current inventory
   - Add/update class/function entries
   - Update timestamp
6. Update "Full Update Workflow" to include changeLog append
7. Update "Quick Update Procedure" to include changeLog append
8. Add changeLog.md and codeInventory.md to "Determine Which Files to Update" table

**Verification:**
- Procedures are step-by-step and clear
- Archive procedure handles edge cases
- **All file lists in 05_PROCEDURE.md include new files**

---

### Phase 7: Add New Reference Files (Optional Enhancement)
**Goal:** Dedicated reference files for complex new features

**Files to create:**
- [x] `references/07_CHANGELOG.md` - Dedicated changeLog instructions
- [x] `references/08_INVENTORY.md` - Dedicated codeInventory instructions

**Changes:**
1. Create `07_CHANGELOG.md` with:
   - Entry format specification
   - Archive procedure details
   - Examples
2. Create `08_INVENTORY.md` with:
   - Format specification
   - Method signature conventions
   - Examples for different languages

**Verification:**
- Files follow reference file conventions
- Examples are practical and clear

---

### Phase 8: Update Skill Manifest and Documentation
**Goal:** Update SKILL.md and README.md

**Files to modify:**
- [x] `SKILL.md` - Add new reference files to metadata
- [x] `README.md` - Document new files and usage

**Changes:**
1. Add `07_CHANGELOG.md` and `08_INVENTORY.md` to references list in SKILL.md
2. Update README line 7: "consists of 7 core files" → "consists of 10 core files"
3. Update README line 132: "Initialize all 7 core files" → "Initialize all 10 core files"
4. Add `changeLog.md`, `changeLog-index.md`, and `codeInventory.md` to README file list (after progress.md)
5. Add "changeLog.md" section to "File-Specific Guidelines"
6. Add "codeInventory.md" section to "File-Specific Guidelines"
7. Update "Initialization" section to mention archives/ directory

**Verification:**
- SKILL.md references match actual files
- README is complete and accurate
- **All "7" references updated to "10" across README**

---

### Phase 9: Update Router
**Goal:** Update routing to include new reference files

**Files to modify:**
- [x] `references/00_ROUTER.md` - Add new reference files to default route

**Changes:**
1. Add `07_CHANGELOG.md` to reading order
2. Add `08_INVENTORY.md` to reading order

**Verification:**
- Router lists all reference files
- Order is logical

---

## File Change Summary

| File | Action | Priority |
|------|--------|----------|
| `references/06_FAILURES.md` | Add templates | P1 |
| `references/01_SUMMARY.md` | Update structure | P1 |
| `references/02_TRIGGERS.md` | Add triggers | P2 |
| `references/03_ALWAYS.md` | Add rules | P2 |
| `references/04_NEVER.md` | Add rules + update constraint | P2 |
| `references/05_PROCEDURE.md` | Add procedures | P2 |
| `references/07_CHANGELOG.md` | Create new | P3 |
| `references/08_INVENTORY.md` | Create new | P3 |
| `SKILL.md` | Update metadata | P4 |
| `README.md` | Update documentation | P4 |
| `references/00_ROUTER.md` | Update route | P4 |

---

## Success Criteria

- [x] Memory Bank initialization creates 10 files + archives directory
- [x] Every Memory Bank update appends to changeLog.md
- [x] Archives created automatically when entries exceed 100
- [x] codeInventory.md template available
- [x] All reference files updated consistently
- [x] README documents new functionality
- [x] No contradictions across reference files

---

## Risks and Mitigations

| Risk | Mitigation |
|------|------------|
| Inconsistent file counts across docs | Verify all references after changes |
| changeLog becomes verbose | Entry format is concise; archives at 100 |
| codeInventory becomes stale | Clear triggers for when to update |

---

## Implementation Order

1. **P1 - Core:** Templates and structure (Phase 1-2)
2. **P2 - Behavior:** Triggers, rules, procedures (Phase 3-6)
3. **P3 - Enhancement:** New reference files (Phase 7)
4. **P4 - Documentation:** Manifest and README (Phase 8-9)
