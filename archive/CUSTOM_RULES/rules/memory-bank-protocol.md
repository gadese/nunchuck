---
trigger: always_on
---

## Memory Bank Protocol

**YOU MUST** read and update the Memory Bank files at the start of every session and whenever context changes significantly.

The Memory Bank is a persistent knowledge base located in `llm_docs/memory/` that maintains project context across sessions. It consists of 7 core files that YOU MUST keep synchronized with the current state of the project.

---

### Core Memory Files

**YOU MUST** check if these files exist at the start of every session:

1. **`memory-index.md`** - Index of all memory files with brief descriptions
2. **`projectbrief.md`** - Project requirements and definition of done
3. **`productContext.md`** - Why features exist, user stories, business logic
4. **`activeContext.md`** - Current session state (updated frequently)
5. **`systemPatterns.md`** - Architectural patterns and tech decisions
6. **`techContext.md`** - Dependencies, APIs, schema, environment
7. **`progress.md`** - Feature completion checklist

---

### When to Read Memory Bank

**YOU MUST** read relevant Memory Bank files in these situations:

1. **At the start of every new session** - Read `memory-index.md` and `activeContext.md`
2. **Before starting implementation** - Read `projectbrief.md`, `systemPatterns.md`, `techContext.md`
3. **When user mentions "context" or "where we left off"** - Read `activeContext.md` and `progress.md`
4. **When making architectural decisions** - Read `systemPatterns.md` and `productContext.md`
5. **When encountering unfamiliar code** - Read `techContext.md` and `systemPatterns.md`

---

### When to Update Memory Bank

**YOU MUST** update Memory Bank files in these situations:

1. **`activeContext.md`** - Update after every significant action:
   - Completing a phase of work
   - Discovering important information
   - Making key decisions
   - Encountering blockers
   - Changing direction

2. **`progress.md`** - Update when:
   - Completing features or tasks
   - Starting new features
   - Marking items as blocked

3. **`systemPatterns.md`** - Update when:
   - Establishing new architectural patterns
   - Making significant design decisions
   - Refactoring major components

4. **`techContext.md`** - Update when:
   - Adding new dependencies
   - Changing API contracts
   - Modifying database schema
   - Updating environment configuration

5. **`productContext.md`** - Update when:
   - Clarifying feature requirements
   - Understanding new business logic
   - Documenting user stories

6. **`projectbrief.md`** - Update when:
   - Project requirements change
   - Definition of done is clarified
   - Success criteria are modified

---

### How to Update Memory Bank

**Use the `/update-memory-bank` workflow** to systematically update Memory Bank files:

```
/update-memory-bank
```

This workflow will:
1. Read current Memory Bank state
2. Identify what needs updating based on recent work
3. Update relevant files with new information
4. Maintain consistency across all files

**For quick updates to `activeContext.md`**, you can directly edit the file:
- Add new "Current Focus" section at the top
- Move previous focus to "Recent Work" section
- Keep file concise (last 2-3 sessions max)

---

### Memory Bank File Structure

#### `memory-index.md`
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
```

#### `activeContext.md`
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
```

#### `progress.md`
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

---

### Best Practices

1. **Keep `activeContext.md` current** - This is the most frequently updated file
2. **Be concise** - Memory Bank is for essential context, not detailed logs
3. **Cross-reference** - Link between files when relevant (e.g., "See systemPatterns.md for architecture")
4. **Date everything** - Always include "Last Updated" timestamps
5. **Remove stale info** - Archive or delete outdated context to keep files focused
6. **Use the workflow** - Prefer `/update-memory-bank` over manual edits for consistency

---

### Integration with R-P-I Workflow

The Memory Bank integrates with the Research-Plan-Implement workflow:

1. **Research Phase** - Read Memory Bank to understand context, update with findings
2. **Plan Phase** - Read Memory Bank to inform planning, update with decisions
3. **Implement Phase** - Read Memory Bank for implementation details, update with progress
4. **Review Phase** - Update Memory Bank with lessons learned and next steps

**YOU MUST NOT** skip reading Memory Bank files at the start of R-P-I workflows. This ensures continuity across sessions and prevents duplicated work or contradictory decisions.
