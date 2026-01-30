# Research-Plan-Implement-Review Workflow

**Invoke with:** `/research-plan-implement`

This workflow orchestrates the complete cycle of researching, planning, implementing, and reviewing code changes. Each phase invokes a dedicated rule that contains the full protocol.

---

## Overview

The R-P-I-Review workflow consists of 4 phases, each calling a dedicated rule:

| Phase | Rule to Invoke | Output |
|-------|---------------|--------|
| 1. Research | `@research` | `llm_docs/research/YYYY-MM-DD-HHMM-research-<topic>.md` |
| 2. Plan | `@plan` | `llm_docs/plans/YYYY-MM-DD-HHMM-plan-<topic>.md` |
| 3. Implement | `@implement` | Code changes + updated plan checkboxes |
| 4. Review | `@review` | Cleaned code + quality verification |

**YOU MUST** complete each phase and get user confirmation before proceeding to the next.

---

## Prerequisites

Before starting this workflow:

1. **Read Memory Bank** - Check `llm_docs/memory/activeContext.md` and `llm_docs/memory/memory-index.md`
2. **Understand the task** - Ensure you have a clear understanding of what needs to be done
3. **Identify scope** - Know which files/components are involved

---

## Phase 1: Research

**Invoke:** `@research`

**Objective:** Document the current state of the codebase relevant to the task.

**Process:**
1. Apply the `@research` rule protocol
2. Follow all steps in the research rule (Memory Bank → Clarify → Read → Analyze → Synthesize)
3. Create research document in `llm_docs/research/`

**Pause Point:**
Present findings summary to user. Wait for confirmation before Phase 2.

---

## Phase 2: Plan

**Invoke:** `@plan`

**Objective:** Create a detailed, actionable implementation plan based on research findings.

**Process:**
1. Provide the research document path from Phase 1
2. Apply the `@plan` rule protocol
3. Follow all steps (Context → Design Options → Structure → Detailed Plan)
4. Create plan document in `llm_docs/plans/`

**Pause Point:**
Present plan to user. Get explicit approval before Phase 3.

---

## Phase 3: Implement

**Invoke:** `@implement`

**Objective:** Execute the approved plan, implementing changes phase by phase with verification.

**Process:**
1. Provide the plan document path from Phase 2
2. Apply the `@implement` rule protocol
3. Follow all steps (Context → Mismatch Evaluation → Implementation → Verification)
4. Update plan checkboxes as work completes

**Pause Point:**
Present implementation summary. Proceed to Phase 4.

---

## Phase 4: Review

**Invoke:** `@review`

**Objective:** Review the implementation for quality, clean up issues, and ensure best practices.

**Process:**
1. Provide the plan document path and list of modified files
2. Apply the `@review` rule protocol
3. Run automated checks, manual review, cleanup
4. Update Memory Bank with completion status

---

## Final Steps

After completing all 4 phases:

1. **Update Memory Bank:**
   - `llm_docs/memory/activeContext.md` - Current state
   - `llm_docs/memory/progress.md` - Completed work

2. **Summary Report:**
   ```
   R-P-I-Review Workflow Complete ✓
   
   Research: [document path]
   Plan: [document path]
   Implementation: [N/N phases complete]
   Review: [quality checks passed]
   
   Files modified: [list]
   Memory Bank updated.
   
   Ready for use.
   ```

---

## Quick Reference

### Starting the workflow:
```
/research-plan-implement

Task: [describe what you want to build/change]
Files: [relevant files if known]
Constraints: [any requirements or limitations]
```

### Invoking individual phases:
- `@research` - Start research phase
- `@plan` - Start planning phase (provide research doc)
- `@implement` - Start implementation (provide plan doc)
- `@review` - Start review (provide plan doc + files)

### Extended thinking triggers:
Use "think hard", "think harder", or "ultrathink" for complex decisions.

---

## Rules

Each phase follows its dedicated rule. See individual rules for full protocols:

- **`@research`** - Descriptive codebase analysis
- **`@plan`** - Technical planning with design options
- **`@implement`** - Plan execution with verification
- **`@review`** - Quality assurance and cleanup
