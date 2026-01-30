# Algorithm Full-Cycle Workflow

**Invoke with:** `/algo-full-cycle`

This workflow orchestrates the complete cycle of researching, planning, implementing, and reviewing algorithm implementations. Each phase invokes a dedicated rule that contains the full protocol.

---

## Overview

The Algorithm Full-Cycle workflow consists of 4 phases, each calling a dedicated rule:

| Phase | Rule to Invoke | Output |
|-------|---------------|--------|
| 1. Research | `@algo-research` | `llm_docs/research/YYYY-MM-DD-HHMM-research-algo-<topic>.md` |
| 2. Plan | `@algo-plan` | `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-<topic>.md` |
| 3. Implement | `@algo-implement` | Code changes + metrics + updated plan |
| 4. Review | `@review` | Cleaned code + reproducibility verification |

**YOU MUST** complete each phase and get user confirmation before proceeding to the next.

---

## Prerequisites

Before starting this workflow:

1. **Read Memory Bank** - Check `llm_docs/memory/activeContext.md` and `llm_docs/memory/memory-index.md`
2. **Understand the problem** - Have a clear problem statement with constraints
3. **Identify metrics** - Know what success looks like quantitatively
4. **Prepare data** - Ensure datasets are available or know where to get them

---

## Phase 1: Algorithm Research

**Invoke:** `@algo-research`

**Objective:** Formalize the algorithmic problem and explore candidate solution approaches.

**Process:**
1. Apply the `@algo-research` rule protocol
2. Follow all steps (Memory Bank → Clarify → Formalize → Baselines → Candidates → Validation Plan)
3. Create research document in `llm_docs/research/`

**Key Outputs:**
- Problem formalization (inputs, outputs, constraints, metrics)
- 3-5 candidate approaches with complexity analysis
- Validation plan with dataset splits

**Pause Point:**
Present candidate approaches ranked by feasibility. Wait for user to select approach.

---

## Phase 2: Algorithm Plan

**Invoke:** `@algo-plan`

**Objective:** Create a detailed implementation plan with quantitative targets and phased development.

**Process:**
1. Provide the research document path from Phase 1
2. Provide the selected approach from user
3. Apply the `@algo-plan` rule protocol
4. Follow all steps (Context → Design Convergence → Structure → Detailed Plan)
5. Create plan document in `llm_docs/plans/`

**Standard Algorithm Phases (P0-P5):**
- **P0:** Baseline & Harness
- **P1:** Prototype
- **P2:** Evaluation
- **P3:** Optimization
- **P4:** Robustness
- **P5:** Packaging

**Key Outputs:**
- Quantitative targets table (metric, target, baseline)
- Phased implementation with success criteria
- Reproducibility checklist

**Pause Point:**
Present plan with quantitative targets. Get explicit approval.

---

## Phase 3: Algorithm Implement

**Invoke:** `@algo-implement`

**Objective:** Execute the approved plan phase by phase, meeting quantitative targets with reproducibility.

**Process:**
1. Provide the plan document path from Phase 2
2. Apply the `@algo-implement` rule protocol
3. Implement phases P0 → P5 sequentially
4. Verify each phase with quantitative measurements
5. Update plan checkboxes and metrics as work completes

**Performance Gates:**
- **After P1:** Correct output, metrics within tolerance
- **After P2:** Primary metric meets target
- **After P3:** Latency and memory meet targets
- **After P4:** Edge cases pass, deterministic

**Key Outputs:**
- Algorithm implementation code
- Benchmark results and comparison tables
- Reproducibility artifacts (seeds, versions, configs)

**Pause Point:**
Present implementation summary with final metrics table.

---

## Phase 4: Review

**Invoke:** `@review`

**Objective:** Review the algorithm implementation for quality, reproducibility, and documentation.

**Process:**
1. Provide the plan document path and list of modified files
2. Apply the `@review` rule protocol
3. Focus on algorithm-specific concerns:
   - Numerical stability (no NaN/Inf)
   - Vectorized operations
   - Reproducibility checklist
   - Performance verification

---

## Final Steps

After completing all 4 phases:

1. **Update Memory Bank:**
   - `llm_docs/memory/activeContext.md` - Current state
   - `llm_docs/memory/progress.md` - Completed work
   - `llm_docs/memory/systemPatterns.md` - New patterns (if any)

2. **Final Metrics Summary:**
   ```
   Algorithm Full-Cycle Workflow Complete ✓
   
   Research: [document path]
   Plan: [document path]
   Implementation: [P0-P5 complete]
   Review: [quality checks passed]
   
   Final Metrics:
   | Metric | Target | Achieved | vs Baseline |
   |--------|--------|----------|-------------|
   | [metric] | [value] | [value] | +X% / -X% |
   
   Reproducibility: Seeds documented, versions pinned.
   Memory Bank updated.
   
   Ready for production use.
   ```

---

## Quick Reference

### Starting the workflow:
```
/algo-full-cycle

Problem: [describe the algorithmic problem]
Constraints: [latency/memory/accuracy requirements]
Data: [dataset characteristics]
Hardware: [CPU/GPU, memory limits]
```

### Invoking individual phases:
- `@algo-research` - Start algorithm research phase
- `@algo-plan` - Start planning phase (provide research doc + selected approach)
- `@algo-implement` - Start implementation (provide plan doc)
- `@review` - Start review (provide plan doc + files)

### Extended thinking triggers:
Use "think hard", "think harder", or "ultrathink" for:
- Complex algorithmic problems
- Trade-off analysis between approaches
- Debugging numerical stability issues
- Performance optimization

---

## Reproducibility Requirements

**YOU MUST** ensure reproducibility at every phase:

1. **Random Seeds:** Set Python, NumPy, PyTorch/TensorFlow seeds
2. **Deterministic Ops:** Use deterministic algorithms where possible
3. **Version Pinning:** Pin all dependency versions
4. **Data Versioning:** Record dataset version or hash

---

## Rules

Each phase follows its dedicated rule. See individual rules for full protocols:

- **`@algo-research`** - Problem formalization and solution space exploration
- **`@algo-plan`** - Algorithm architecture and quantitative planning
- **`@algo-implement`** - Plan execution with benchmarking
- **`@review`** - Quality assurance and cleanup (shared with generic workflow)
