# Plan Phase Only

Execute only the planning phase based on existing research.

## When to Use

Use this pipeline when you:
- Have completed research and need to create an implementation plan
- Have existing research documentation to work from
- Want to explore design options before committing to implementation
- Need to update or revise an existing plan

## Prerequisites

**Required:**
- Research document path from `llm_docs/research/`

**Optional:**
- Additional file paths to consider
- Specific constraints or requirements

## Process

### Phase 1: Plan
**Skill:** `rpi-plan`

**Objective:** Create a detailed, actionable implementation plan based on research findings.

**Steps:**

1. **Context Gathering & Initial Analysis**
   - Read Memory Bank files (`activeContext.md`, `systemPatterns.md`, `techContext.md`)
   - Read research document completely
   - Read all additional input files fully
   - Explore codebase guided by research findings
   - Verify understanding and cross-reference with actual code
   - Synthesize and clarify ambiguities

2. **Clarification (if needed)**
   - Present understanding of current state with file references
   - Ask questions requiring human judgment or clarification
   - Wait for user answers before proceeding

3. **Research & Discovery**
   - Handle any corrections by verifying with actual files
   - Propose 2-3 viable design options with pros/cons
   - Provide recommendation with rationale
   - Wait for user to select approach

4. **Plan Structure Development**
   - Present phased outline for approval
   - Show what each phase accomplishes
   - Wait for structure approval before detailed planning

5. **Detailed Plan Writing**
   - Create comprehensive implementation plan
   - Include phases with success criteria
   - Add file references (path:line-range format)
   - Document risks and mitigations
   - Define out-of-scope items

6. **Output Document**
   - Location: `llm_docs/plans/`
   - Filename: `YYYY-MM-DD-HHMM-plan-<kebab-topic>.md`
   - No frontmatter, markdown with references only

7. **Update Memory Bank**
   - Add design decisions to `llm_docs/memory/activeContext.md`

**Output:** Implementation plan with phases, success criteria, and file references

**⏸️ PAUSE POINT:** Present plan structure and key decisions to user. Plan phase complete.

---

## Output Format

The plan document follows this structure:

```markdown
# Implementation Plan — [Topic]

**Tags:** [taxonomy tags]

## 1. Overview
Brief description of what we're implementing and why

## 2. Current State Summary
What exists now with file:line references

## 3. Desired End State
Statement of desired outcome and verification

## 4. Key Discoveries
Important findings with file:line references

## 5. Design Decision
Chosen approach, rationale, alternatives considered

## 6. Out of Scope
Explicit items NOT being done

## 7. Implementation Phases
### Phase 1: [Name]
**Complexity:** S/M/L
**Objective:** [What this achieves]
**Changes by Component:** [file:line references]
**Implementation Steps:** [Clear actions]
**Success Criteria:** [Automated and manual checks]
**Dependencies:** [If any]

[Additional phases...]

## 8. Risks & Mitigations
Table of risks, impacts, and mitigation strategies

## 9. References
Research doc and similar implementations
```

---

## Quick Reference

**Invoking plan only:**
```
/rpi-plan

Research document: llm_docs/research/[filename].md
Task description: [what you're building]
Constraints: [any requirements or limitations]
```

---

## Next Steps

After planning is complete, you can:
1. Review and refine the plan manually
2. Invoke `/rpi-implement` with plan document to execute implementation
3. Share plan for team review before implementation
