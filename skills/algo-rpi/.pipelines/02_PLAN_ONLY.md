# Algorithm Plan Phase Only

Execute only the algorithm planning phase based on existing research.

## When to Use

Use this pipeline when you:
- Have completed algorithm research and need to create an implementation plan
- Have existing research documentation with candidate approaches
- Want to define quantitative targets and phased implementation
- Need to plan algorithm development with reproducibility requirements

## Prerequisites

**Required:**
- Research document path from `llm_docs/research/`

**Optional:**
- Selected approach from research (if multiple candidates)
- Additional constraints or requirements
- Hardware environment details

## Process

### Phase 1: Algorithm Plan
**Skill:** `algo-rpi-plan`

**Objective:** Create a detailed implementation plan with quantitative targets and phased development.

**Steps:**

1. **Context Gathering & Initial Analysis**
   - Read Memory Bank files (`activeContext.md`, `systemPatterns.md`, `techContext.md`)
   - Read research document completely
   - Identify recommended approaches and their rationale
   - Note algorithmic trade-offs: accuracy vs speed vs memory
   - Extract interface requirements from Codebase Interface Analysis
   - Understand dataset characteristics and evaluation methodology
   - Read all additional input files fully
   - Gather technical context (source files, datasets, benchmarks, integration points, hardware/runtime assumptions)
   - Verify understanding and cross-reference with actual materials

2. **Synthesize and Clarify**
   
   **CRITICAL:** Present understanding and confirm selected approach:

   Based on the algorithm research, I understand we need to implement [algorithm/approach] to achieve [goal].

   **Problem Definition:**
   - Input: [data type, shape, constraints]
   - Output: [expected output, format]
   - Key metric: [primary metric and target value]

   **Selected Approach (from research):**
   - Algorithm: [name/description]
   - Expected complexity: O([time]) time, O([space]) space
   - Key trade-offs: [accuracy vs speed vs memory considerations]

   **Integration Points:**
   - [Interface with file:line reference]
   - [Data contract with file:line reference]

   **Hardware Constraints:**
   - Target: [CPU/GPU/TPU]
   - Memory budget: [limit]
   - Latency requirement: [target]

   **Questions requiring clarification:** (only if genuinely ambiguous)

   **⏸️ PAUSE:** Wait for user confirmation before proceeding.

3. **Design Convergence**
   
   If research presents multiple viable approaches, present refined options:

   **Option A: [Algorithm Name]**
   - Approach, Complexity, Pros, Cons, Research reference

   **Option B: [Algorithm Name]**
   - Approach, Complexity, Pros, Cons, Research reference

   **Recommendation:** Option [X] because [rationale]

   **⏸️ PAUSE:** Which approach should we proceed with? Wait for user selection.

   Sketch algorithm architecture (textual):
   - Data Preparation, Core Algorithm, Postprocessing, Evaluation, Packaging

   Define interfaces and invariants

4. **Plan Structure Development**
   
   Present P0-P5 phase outline:

   **Proposed Plan Structure**

   **Overview:** [1-2 sentence summary]

   **Development Phases:**
   1. **P0: Baseline & Harness** — Establish baseline, dataset splits, metrics, benchmark harness
   2. **P1: Prototype** — Implement minimal viable algorithm, verify correctness
   3. **P2: Evaluation** — Full evaluation, ablations, significance testing
   4. **P3: Optimization** — Profile, vectorize, parallelize, meet performance targets
   5. **P4: Robustness** — Edge cases, determinism, error handling
   6. **P5: Packaging** — Documentation, examples, reproducibility artifacts

   Does this phasing make sense?

   **⏸️ PAUSE:** Wait for structure approval before writing detailed plan.

5. **Detailed Plan Writing**
   
   Create comprehensive plan document with:
   - Problem statement
   - Quantitative targets table (metric, target, baseline, notes)
   - Selected approach (algorithm, complexity, rationale, trade-offs)
   - Integration points from research
   - Hardware & runtime assumptions
   - Out of scope items
   - P0-P5 implementation phases with deliverables and success criteria
   - Risks & mitigations
   - Reproducibility checklist

6. **Output Document**
   - Location: `llm_docs/plans/`
   - Filename: `YYYY-MM-DD-HHMM-plan-algo-<kebab-topic>.md`
   - No frontmatter, markdown with references only

7. **Update Memory Bank**
   - Add design decisions to `llm_docs/memory/activeContext.md`

**Output:** Implementation plan with quantitative targets, P0-P5 phases, success criteria, reproducibility checklist

**⏸️ PAUSE POINT:** Present plan with quantitative targets. Plan phase complete.

---

## Output Format

The plan document follows this structure:

```markdown
# Algorithm Implementation Plan — [Topic]

**Tags:** [taxonomy tags]

## 1. Problem Statement
Input, Output, Objective

## 2. Quantitative Targets
| Metric | Target | Baseline | Notes |
|--------|--------|----------|-------|
| [Primary metric] | [value] | [current] | [context] |
| Latency | [ms] | [current] | [hardware context] |
| Memory | [MB/GB] | [current] | [constraints] |

## 3. Selected Approach
Algorithm, Complexity, Rationale, Key Trade-offs

## 4. Integration Points
From research with file:line references

## 5. Hardware & Runtime Assumptions
Target hardware, memory budget, batch size, concurrency

## 6. Out of Scope
Explicit exclusions

## 7. Implementation Phases
### P0: Baseline & Harness
Objective, Deliverables, Success Criteria

### P1-P5: [Similar structure]

## 8. Risks & Mitigations
Table of risks, impacts, mitigation strategies

## 9. Reproducibility Checklist
Seeds, versions, dataset hash, hardware config

## 10. References
Research doc, baseline, dataset paths
```

---

## Quick Reference

**Invoking plan only:**
```
/algo-rpi-plan

Research document: llm_docs/research/[filename].md
Problem: [algorithmic task]
Targets: [metric]=X, latency=Yms, memory=ZMB
Hardware: [CPU/GPU/TPU, memory limits]
```

---

## Next Steps

After planning is complete, you can:
1. Review and refine the plan manually
2. Invoke `/algo-rpi-implement` with plan document to execute implementation
3. Share plan for team review before implementation
