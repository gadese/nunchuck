# Full R-P-I Workflow with Plan Review & Reimagine

Complete Research-Plan-Implement cycle with integrated plan review, plan reimagination, code review, and commit message generation.

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

**🧹 CONTEXT CLEARING:** After user approval, clear conversation context. The next phase (Plan) should start fresh with only the research document and Memory Bank as inputs.

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

**🧹 CONTEXT CLEARING:** After user approval, clear conversation context. The next phase (Plan Review) should start fresh with only the plan document as input.

---

### Phase 3: Plan Review
**Skill:** `rpi-plan-review`

**Objective:** Review the implementation plan as a staff engineer, identifying blind spots, edge cases, and opportunities for better practices.

**Process:**
1. Read the plan document from Phase 2
2. Review across all dimensions:
   - Edge cases and boundary conditions
   - Error handling and validation
   - Performance and scalability
   - Security considerations
   - Maintainability and testability
   - Dependencies and external services
3. Annotate the plan in-place with improvements
4. Present review summary with recommendation

**Output:** Annotated plan with improvements, review summary

**⏸️ PAUSE POINT:** Present review summary to user. Wait for explicit approval before proceeding to Phase 4.

**🧹 CONTEXT CLEARING:** After user approval, clear conversation context. The next phase (Plan Reimagine) should start fresh with the reviewed plan document as input.

---

### Phase 4: Plan Reimagine
**Skill:** `rpi-plan-reimagine`

**Objective:** Rewrite the implementation plan from scratch as a V2 architect, optimizing for robustness, readability, and elegant coding patterns.

**Process:**
1. Read all context:
   - Research document from Phase 1
   - Original plan from Phase 2
   - Reviewed plan from Phase 3
   - Relevant code files
2. Identify optimization opportunities:
   - Algorithmic efficiency
   - Data structures
   - Code patterns
   - Simplification
   - Robustness
   - Readability
3. Write new plan (V2) from scratch in `llm_docs/plans/YYYY-MM-DD-HHMM-plan-<topic>-v2.md`
4. Document key optimizations and rationale

**Output:** New optimized plan (V2), comparison with V1

**⏸️ PAUSE POINT:** Present optimization summary to user. Wait for explicit approval of which plan to use (V1 reviewed or V2 optimized) before proceeding to Phase 5.

**🧹 CONTEXT CLEARING:** After user approval, clear conversation context. The next phase (Implement) should start fresh with only the approved plan document and Memory Bank as inputs.

---

### Phase 5: Implement
**Skill:** `rpi-implement`

**Objective:** Execute the approved plan, implementing changes phase by phase with verification.

**Process:**
1. Read Memory Bank files
2. Read approved plan document (V1 reviewed or V2 optimized)
3. Apply clarification protocol if plan is ambiguous
4. Evaluate mismatches between plan and current codebase state
5. Implement changes phase by phase
6. Run verification after each phase (automated checks + manual criteria)
7. Update plan checkboxes as work completes
8. Update Memory Bank with completion status

**Output:** Code changes, updated plan with checkmarks, implementation summary

**⏸️ PAUSE POINT:** Present implementation summary with verification results. Wait for user approval before proceeding to Phase 6.

**🧹 CONTEXT CLEARING:** After user approval, clear conversation context. The next phase (Code Review) should start fresh with only the modified files as input.

---

### Phase 6: Code Review
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

**⏸️ PAUSE POINT:** Present code review summary. Offer to proceed to Phase 7 (commit message generation).

**🧹 CONTEXT CLEARING:** After user approval, clear conversation context. The next phase (Commit Message) should start fresh with only the staged changes as input.

---

### Phase 7: Commit Message (Optional)
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
- **Update after Plan Review:** Add review insights to `activeContext.md`
- **Update after Plan Reimagine:** Add optimization decisions to `activeContext.md`
- **Update after Implement:** Update `progress.md` with completed work
- **Update after Review:** Mark task complete in `activeContext.md`

---

## Context Clearing Protocol

**CRITICAL:** Between each phase, the agent MUST clear conversation context to prevent:
- Carrying over assumptions from previous phases
- Mixing concerns between phases
- Context pollution affecting decision-making

**How to clear context:**
1. Complete the current phase and present results
2. Wait for user approval
3. Explicitly state: "Context cleared. Starting [next phase] with fresh perspective."
4. Only read the specified inputs for the next phase (do not reference prior conversation)

---

## Quick Reference

**Starting the full workflow:**
```
/rpi-full

Task: [describe what you want to build/change]
Files: [relevant files if known]
Constraints: [any requirements or limitations]
```

**Invoking individual phases:**
- `/rpi-research` — Research phase only
- `/rpi-plan` — Plan phase only (provide research doc)
- `/rpi-plan-review` — Plan review phase only (provide plan doc)
- `/rpi-plan-reimagine` — Plan reimagine phase only (provide plan doc)
- `/rpi-implement` — Implement phase only (provide plan doc)
- `/code-review` — Code review (standalone)
- `/commit-message` — Commit message generation (standalone)

---

## Success Criteria

The workflow is complete when:
- [x] Research document created and approved
- [x] Implementation plan created and approved
- [x] Plan reviewed and improvements added
- [x] Plan reimagined and optimized (V2 created)
- [x] User selected which plan to use (V1 reviewed or V2 optimized)
- [x] All plan phases implemented and verified
- [x] Code review passes all checks
- [x] Commit message generated (if requested)
- [x] Memory Bank updated with completion status

---

## Comparison with Default Workflow

**Default Workflow (00_DEFAULT.md):**
- Research → Plan → Implement → Code Review → Commit Message
- 5 phases total
- Faster, suitable for straightforward tasks

**Full Workflow (04_FULL_WORKFLOW.md):**
- Research → Plan → Plan Review → Plan Reimagine → Implement → Code Review → Commit Message
- 7 phases total
- More thorough, includes quality gates and optimization
- Suitable for complex tasks requiring high quality and robustness

**When to use Full Workflow:**
- Complex features with many edge cases
- Performance-critical implementations
- Security-sensitive changes
- Refactoring with optimization opportunities
- When you want maximum quality and robustness

**When to use Default Workflow:**
- Simple features or bug fixes
- Time-sensitive tasks
- When the straightforward approach is sufficient
- Prototyping or exploratory work
