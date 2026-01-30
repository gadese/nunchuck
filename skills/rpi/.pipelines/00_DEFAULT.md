# Full R-P-I Workflow

Complete Research-Plan-Implement cycle with integrated code review and commit message generation.

## Workflow Phases

### Phase 1: Research
**Skill:** `rpi-research`

**Objective:** Document the current state of the codebase relevant to the task.

**Process:**
1. Read Memory Bank files (`llm_docs/memory/activeContext.md`, `llm_docs/memory/systemPatterns.md`)
2. Apply clarification protocol if scope is ambiguous
3. Perform descriptive codebase analysis
4. Create research document in `llm_docs/research/YYYY-MM-DD-HHMM-research-<topic>.md`

**Output:** Research document with findings, architecture documentation, and references

**⏸️ PAUSE POINT:** Present research findings summary to user. Wait for explicit approval before proceeding to Phase 2.

---

### Phase 2: Plan
**Skill:** `rpi-plan`

**Objective:** Create a detailed, actionable implementation plan based on research findings.

**Process:**
1. Read Memory Bank files
2. Read research document from Phase 1
3. Apply clarification protocol if requirements are ambiguous
4. Present design options and get user confirmation
5. Present plan structure for approval
6. Create detailed plan document in `llm_docs/plans/YYYY-MM-DD-HHMM-plan-<topic>.md`

**Output:** Implementation plan with phases, success criteria, and file references

**⏸️ PAUSE POINT:** Present plan structure and key decisions to user. Wait for explicit approval before proceeding to Phase 3.

---

### Phase 3: Implement
**Skill:** `rpi-implement`

**Objective:** Execute the approved plan, implementing changes phase by phase with verification.

**Process:**
1. Read Memory Bank files
2. Read plan document from Phase 2
3. Apply clarification protocol if plan is ambiguous
4. Evaluate mismatches between plan and current codebase state
5. Implement changes phase by phase
6. Run verification after each phase (automated checks + manual criteria)
7. Update plan checkboxes as work completes
8. Update Memory Bank with completion status

**Output:** Code changes, updated plan with checkmarks, implementation summary

**⏸️ PAUSE POINT:** Present implementation summary with verification results. Wait for user approval before proceeding to Phase 4.

---

### Phase 4: Code Review
**Skill:** `code-review` (standalone skill, not part of rpi skillset)

**Objective:** Review implemented code for quality, adherence to guidelines, and best practices.

**Process:**
1. Identify files modified during implementation (from plan or git diff)
2. Run automated checks (ruff, pytest, type checking)
3. Perform manual review using coding standards
4. Identify areas for improvement in terms of readability and code quality
5. Fix identified issues
6. Verify fixes
7. Update Memory Bank

**Output:** Clean code passing all quality checks, review summary

**⏸️ PAUSE POINT:** Present code review summary. Offer to proceed to Phase 5 (commit message generation).

---

### Phase 5: Commit Message (Optional)
**Skill:** `commit-message` (standalone skill, not part of rpi skillset)

**Objective:** Generate descriptive, conventional commit message based on changes.

**Process:**
1. Analyze staged changes (`git diff --staged`)
2. Identify change type (feat, fix, refactor, docs, test, chore)
3. Generate commit message following conventional format
4. Present to user for confirmation

**Output:** Commit message ready for use

---

## Memory Bank Integration

At each phase, the workflow integrates with Memory Bank:

- **Read at start:** `activeContext.md`, `systemPatterns.md`, `techContext.md`
- **Update after Research:** Add key findings to `activeContext.md`
- **Update after Plan:** Add design decisions to `activeContext.md`
- **Update after Implement:** Update `progress.md` with completed work
- **Update after Review:** Mark task complete in `activeContext.md`

---

## Quick Reference

**Starting the full workflow:**
```
/rpi

Task: [describe what you want to build/change]
Files: [relevant files if known]
Constraints: [any requirements or limitations]
```

**Invoking individual phases:**
- `/rpi-research` — Research phase only
- `/rpi-plan` — Plan phase only (provide research doc)
- `/rpi-implement` — Implement phase only (provide plan doc)
- `/code-review` — Code review (standalone)
- `/commit-message` — Commit message generation (standalone)

---

## Success Criteria

The workflow is complete when:
- [x] Research document created and approved
- [x] Implementation plan created and approved
- [x] All plan phases implemented and verified
- [x] Code review passes all checks
- [x] Commit message generated (if requested)
- [x] Memory Bank updated with completion status
