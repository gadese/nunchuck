# Update Memory Bank Workflow

**Invoke with:** `/update-memory-bank`

This workflow systematically updates the Memory Bank files to maintain persistent project context across sessions. It ensures that important decisions, patterns, and progress are captured for future reference.

---

## Overview

The Memory Bank consists of 7 core files that track different aspects of the project:

1. **memory-index.md** - Index of all memory files
2. **projectbrief.md** - Project requirements and definition of done
3. **productContext.md** - Feature rationale and business logic
4. **activeContext.md** - Current session state (most frequently updated)
5. **systemPatterns.md** - Architectural patterns and tech decisions
6. **techContext.md** - Dependencies, APIs, schema, environment
7. **progress.md** - Feature completion checklist

This workflow helps you identify which files need updating and ensures consistency across all Memory Bank files.

---

## When to Use This Workflow

Use this workflow:
- After completing a significant feature or task
- After making architectural decisions
- After discovering important patterns or constraints
- When switching focus to a new area of work
- At the end of a work session
- When context has changed significantly

**DO NOT** use this workflow for minor changes or every small edit. Reserve it for meaningful updates that affect project understanding.

---

## Process

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
```

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
| Completed work, current focus changed | `activeContext.md`, `progress.md` |
| Architectural decision, new pattern | `systemPatterns.md`, `activeContext.md` |
| New dependency, API change | `techContext.md`, `activeContext.md` |
| Feature rationale clarified | `productContext.md` |
| Requirements changed | `projectbrief.md`, `activeContext.md` |
| New memory file added | `memory-index.md` |

### Step 4: Update Files Systematically

For each file that needs updating:

#### Updating `activeContext.md` (Most Frequent)

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

#### Updating `progress.md`

**Update guidelines:**
- Move completed items from "In Progress" to "Completed Features"
- Add completion dates to completed items
- Add new items to "In Progress" or "Planned"
- Update subtask checkboxes
- Add blockers if any

#### Updating `systemPatterns.md`

**Update guidelines:**
- Add new architectural patterns discovered
- Document new design decisions with rationale
- Update code organization if structure changed
- Add new testing patterns if established
- Document new error handling patterns
- Keep patterns organized by category

#### Updating `techContext.md`

**Update guidelines:**
- Add new dependencies to the list
- Update API contracts if they changed
- Add new data models
- Update environment variables
- Document new external APIs
- Update deployment configuration if changed

#### Updating `productContext.md`

**Update guidelines:**
- Add new user stories or use cases
- Document feature rationale when clarified
- Update business logic explanations
- Add key decisions with context
- Document why features exist

#### Updating `projectbrief.md`

**Update guidelines:**
- Update requirements if they changed
- Modify definition of done if criteria changed
- Update success criteria
- Adjust technology stack if needed
- Update objectives if scope changed

#### Updating `memory-index.md`

**Update guidelines:**
- Update "Last Updated" timestamp
- Add new files if any were created
- Update file descriptions if they changed
- Keep the index concise and accurate

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

## Best Practices

1. **Update frequently but not excessively** - After significant work, not every edit
2. **Keep activeContext.md current** - This is the most important file
3. **Be concise** - Memory Bank is for essential context, not detailed logs
4. **Use timestamps** - Always update "Last Updated" fields
5. **Cross-reference** - Link between files when relevant
6. **Remove stale info** - Archive or delete outdated context
7. **Maintain consistency** - Ensure no contradictions across files

---

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
4. Done

### Full Update (multiple files)
Use when:
- Completing a major feature
- Making architectural decisions
- Discovering important patterns
- Changing dependencies or APIs
- Updating requirements

Process:
1. Follow the complete workflow above
2. Update all relevant files
3. Verify consistency
4. Provide summary report

---

## Integration with R-P-I Workflows

The Memory Bank should be updated at key points in R-P-I workflows:

**During Research:**
- Update `activeContext.md` with research findings
- Update `systemPatterns.md` if new patterns discovered

**During Planning:**
- Update `activeContext.md` with design decisions
- Update `systemPatterns.md` with architectural choices

**During Implementation:**
- Update `progress.md` as phases complete
- Update `activeContext.md` with current state

**During Review:**
- Update all relevant files with final state
- Update `progress.md` with completed features
- Update `systemPatterns.md` with lessons learned

---

## Workflow Invocation

To start this workflow:
```
/update-memory-bank
```

The workflow will guide you through:
1. Reading current Memory Bank state
2. Identifying what changed
3. Determining which files to update
4. Updating files systematically
5. Verifying consistency
6. Providing a summary report
