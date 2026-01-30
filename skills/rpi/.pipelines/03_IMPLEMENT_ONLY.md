# Implement Phase Only

Execute only the implementation phase based on existing plan.

## When to Use

Use this pipeline when you:
- Have an approved implementation plan ready to execute
- Need to resume interrupted implementation work
- Want to implement a specific plan without research/planning overhead
- Are continuing work from a previous session

## Prerequisites

**Required:**
- Plan document path from `llm_docs/plans/`

**Optional:**
- Clarification on scope, environment, priorities, or verification steps

## Process

### Phase 1: Implement
**Skill:** `rpi-implement`

**Objective:** Execute the approved plan, implementing changes phase by phase with verification.

**Steps:**

1. **Context Gathering**
   - Read Memory Bank files (`activeContext.md`, `systemPatterns.md`)
   - Read plan document completely
   - Check for existing checkmarks (`- [x]`) to identify completed work
   - Read all files referenced in the plan
   - Create internal task tracking

2. **Clarification (if needed)**
   - Apply clarification protocol if plan is ambiguous
   - Ask about scope confirmation, environment setup, priorities, verification
   - Wait for user answers before proceeding
   - Exception: If plan is complete and unambiguous, proceed directly

3. **Mismatch Evaluation**
   - Assess discrepancies between plan and current codebase
   - Minor mismatches: Use judgment and adapt (line shifts, naming differences)
   - Major mismatches: STOP and present to user with options
   - Get confirmation before proceeding if major mismatch found

4. **Phase-by-Phase Implementation**
   For each phase in the plan:
   - Announce the phase and objective
   - Implement changes following plan steps
   - Make minimal, focused edits
   - Preserve existing code style
   - Handle edge cases and debug issues
   - Update plan document checkboxes (`- [x]`)

5. **Phase Verification**
   After each phase:
   - Run automated checks (ruff, pytest, type checking)
   - Perform manual verification per success criteria
   - Report results concisely
   - Fix issues before proceeding to next phase

6. **Completion & Handoff**
   When all phases complete:
   - Run full test suite
   - Verify all success criteria
   - Update plan with completion timestamp
   - Update Memory Bank (`activeContext.md`, `progress.md`)
   - Present summary report

**Output:** Code changes, updated plan with checkmarks, implementation summary

**⏸️ PAUSE POINT:** Present implementation summary with verification results. Implementation phase complete.

---

## Resuming Interrupted Work

If the plan has existing checkmarks:
1. **Trust completed work** — Assume checked items are done correctly
2. **Verify continuity** — Read last completed phase's changes
3. **Resume from first unchecked item** — Pick up exactly where work stopped

---

## Verification Requirements

**Automated checks (run after each phase):**
- `ruff check .` — Linting
- `ruff format --check .` — Formatting
- `pytest [relevant test files]` — Tests

**Manual verification:**
- Verify specific behaviors mentioned in plan
- Test edge cases explicitly called out
- Confirm success criteria met

---

## Quality Guidelines

- Follow existing codebase patterns and conventions
- Respect workspace rules (code principles, style guides)
- Write code for clarity and maintainability
- Use type hints consistently
- Keep changes minimal and focused
- Prefer `ruff` for formatting

---

## Quick Reference

**Invoking implement only:**
```
/rpi-implement

Plan document: llm_docs/plans/[filename].md
Scope: [any last-minute scope changes]
Environment: [setup steps or dependencies]
Priority: [which phases are highest priority]
```

---

## Next Steps

After implementation is complete, you can:
1. Invoke `/code-review` to review implemented code
2. Invoke `/commit-message` to generate commit message
3. Manually test and verify the implementation
4. Deploy or merge changes
