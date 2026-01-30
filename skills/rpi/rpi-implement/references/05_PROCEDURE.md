# Procedure

## Implementation Process

Follow these steps in order:

### Step 1: Context Gathering

1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns

2. **Read the plan completely**
   - Identify all phases, success criteria, and file references
   - Note any existing checkmarks indicating prior progress
   - Understand the dependencies between phases

3. **Read all referenced files**
   - Read every file mentioned in the plan fully (no offset/limit)
   - Verify the current state matches what the plan expects
   - Note any discrepancies for the mismatch evaluation

4. **Create internal task tracking**
   - Build a mental model of what needs to be done
   - Identify the logical order of changes within each phase

### Step 2: Mismatch Evaluation

Before implementing, assess any discrepancies between the plan and reality:

**Minor mismatches** (use judgment, proceed with adaptation):
- Line numbers have shifted due to unrelated changes
- Variable/function names differ slightly but intent is clear
- File structure has minor reorganization
- Additional imports or dependencies already present

**Major mismatches** (STOP and ask):
- Files specified in the plan no longer exist
- The architecture has fundamentally changed
- Key functions or classes the plan depends on are missing
- The plan's approach conflicts with recent codebase changes
- Success criteria cannot be verified with available tools

When encountering a major mismatch, present it as:

```
**Mismatch in Phase [N]: [Phase Name]**

| Aspect | Expected (Plan) | Found (Reality) |
|--------|-----------------|-----------------|
| [Item] | [Plan says]     | [Actual state]  |

**Impact**: [Why this matters for implementation]

**Options**:
1. [Possible adaptation]
2. [Alternative approach]
3. [Skip and revisit later]

How should I proceed?
```

### Step 3: Phase-by-Phase Implementation

For each phase in the plan:

1. **Announce the phase**
   ```
   Starting Phase [N]: [Phase Name]
   Objective: [What this phase achieves]
   ```

2. **Implement changes**
   - Follow the implementation steps in order
   - Make minimal, focused edits
   - Preserve existing code style and patterns
   - Add necessary imports at the top of files

3. **Handle edge cases**
   - If something doesn't work as expected, debug before moving on
   - Add logging or assertions if needed to verify behavior
   - Document any deviations from the plan in your progress update

4. **Update the plan document**
   - Check off completed items using `- [x]`
   - Add brief notes if you made adaptations

### Step 4: Phase Verification

After completing each phase, run verification:

1. **Automated checks**
   ```bash
   ruff check .
   ruff format --check .
   pytest [relevant test files]
   ```

2. **Manual verification** (as specified in success criteria)
   - Verify specific behaviors mentioned in the plan
   - Test edge cases explicitly called out

3. **Report results**
   ```
   Phase [N] Complete ✓
   
   Automated:
   - [x] ruff check passes
   - [x] ruff format passes
   - [x] pytest passes ([N] tests)
   
   Manual:
   - [x] [Specific behavior verified]
   
   Notes: [Any observations or minor adaptations made]
   ```

4. **Fix issues before proceeding**
   - Do not move to the next phase with failing tests
   - If a fix requires plan deviation, apply mismatch protocol

### Step 5: Completion & Handoff

When all phases are complete:

1. **Final verification**
   - Run full test suite
   - Verify all success criteria from the plan

2. **Update plan document**
   - Ensure all checkboxes are marked
   - Add completion timestamp and any final notes

3. **Update Memory Bank**
   - Update `llm_docs/memory/activeContext.md` with completion status
   - Update `llm_docs/memory/progress.md` with completed work

4. **Summary report**
   ```
   Implementation Complete ✓
   
   Phases completed: [N/N]
   Files modified: [list]
   Tests added/modified: [list]
   
   Deviations from plan:
   - [Any adaptations made and why]
   
   Verification status:
   - [x] All automated checks pass
   - [x] All manual criteria verified
   
   Ready for review.
   ```

## Resumption Protocol

If the plan has existing checkmarks:

1. **Trust completed work**
   - Assume checked items are done correctly
   - Do not re-implement completed phases

2. **Verify continuity**
   - Read the last completed phase's changes
   - Ensure the codebase is in the expected state
   - If something seems off, verify before proceeding

3. **Resume from first unchecked item**
   - Pick up exactly where work stopped
   - Apply the same verification rigor to remaining phases

## Sub-Task Guidance

**Use sub-tasks for:**
- Targeted debugging when a test fails unexpectedly
- Exploring unfamiliar parts of the codebase not covered by the plan
- Complex refactoring that cascades through many files
- Test generation for edge cases discovered during implementation

**Avoid sub-tasks for:**
- Simple file edits clearly specified in the plan
- Running verification commands (do these directly)
- Reading files already referenced in the plan
- Making decisions that should be escalated to the user
