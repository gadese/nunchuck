# Full Algo-RPI Workflow

Complete Algorithm Research-Plan-Implement cycle with integrated code review and commit message generation.

## Workflow Phases

### Phase 1: Algorithm Research
**Skill:** `algo-rpi-research`

**Objective:** Formalize the algorithmic problem and explore candidate solution approaches.

**Process:**
1. Read Memory Bank files (`llm_docs/memory/activeContext.md`, `llm_docs/memory/systemPatterns.md`, `llm_docs/memory/techContext.md`)
2. Apply clarification protocol if problem statement is ambiguous
3. Formalize problem: inputs, outputs, constraints, metrics, targets, operating environment, failure modes
4. Perform codebase interface analysis
5. Establish baselines and prior art
6. Explore solution space (3-5 candidate approaches)
7. Propose downselect criteria and validation plan
8. Create research document in `llm_docs/research/YYYY-MM-DD-HHMM-research-algo-<topic>.md`

**Output:** Research document with problem formalization, candidate approaches, and validation plan

**⏸️ PAUSE POINT:** Present candidate approaches ranked by feasibility. Wait for user to select approach before proceeding to Phase 2.

---

### Phase 2: Algorithm Plan
**Skill:** `algo-rpi-plan`

**Objective:** Create a detailed implementation plan with quantitative targets and phased development.

**Process:**
1. Read Memory Bank files
2. Read research document from Phase 1
3. Confirm selected approach from research (if multiple options presented)
4. Sketch algorithm architecture (data preparation, core algorithm, postprocessing, evaluation, packaging)
5. Define interfaces and invariants
6. Present P0-P5 plan structure for approval
7. Create detailed plan document in `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-<topic>.md`

**Standard Algorithm Phases (P0-P5):**
- **P0: Baseline & Harness** — Establish baseline, dataset splits, metrics, benchmark harness
- **P1: Prototype** — Implement minimal viable algorithm, verify correctness
- **P2: Evaluation** — Full evaluation, ablations, significance testing
- **P3: Optimization** — Profile, vectorize, parallelize, meet performance targets
- **P4: Robustness** — Edge cases, determinism, error handling
- **P5: Packaging** — Documentation, examples, reproducibility artifacts

**Output:** Implementation plan with quantitative targets table, P0-P5 phases, success criteria, reproducibility checklist

**⏸️ PAUSE POINT:** Present plan with quantitative targets. Get explicit approval before proceeding to Phase 3.

---

### Phase 3: Algorithm Implement
**Skill:** `algo-rpi-implement`

**Objective:** Execute the approved plan phase by phase, meeting quantitative targets with reproducibility.

**Process:**
1. Read Memory Bank files
2. Read plan document from Phase 2
3. Verify prerequisites (baseline metrics, dataset splits, benchmark harness)
4. Evaluate mismatches between plan and current state
5. Implement phases P0 → P5 sequentially
6. Verify each phase with quantitative measurements
7. Check performance gates at P1, P2, P3, P4 milestones
8. Update plan checkboxes as work completes
9. Update Memory Bank with completion status

**Performance Gates:**
- **After P1 (Prototype):** Algorithm produces correct output, metrics within tolerance on small subset
- **After P2 (Evaluation):** Primary metric meets target on full test set, statistically significant
- **After P3 (Optimization):** Latency and memory meet targets, no accuracy regression
- **After P4 (Robustness):** Edge cases pass, deterministic across runs, graceful failure

**Output:** Algorithm implementation code, benchmark results, updated plan with checkmarks, reproducibility artifacts

**⏸️ PAUSE POINT:** Present implementation summary with final metrics table. Wait for user approval before proceeding to Phase 4.

---

### Phase 4: Code Review
**Skill:** `code-review` (standalone skill, not part of algo-rpi skillset)

**Objective:** Review algorithm implementation for quality, adherence to guidelines, and best practices.

**Process:**
1. Identify files modified during implementation (from plan or git diff)
2. Run automated checks (ruff, pytest, type checking)
3. Perform manual review using coding standards
4. Focus on algorithm-specific concerns:
   - Numerical stability (no NaN/Inf)
   - Vectorized operations (NumPy, OpenCV)
   - Type hints on all functions
   - Reproducibility verification
   - Performance verification
5. Identify areas for improvement in terms of readability and code quality
6. Fix identified issues
7. Verify fixes
8. Update Memory Bank

**Output:** Clean code passing all quality checks, review summary

**⏸️ PAUSE POINT:** Present code review summary. Offer to proceed to Phase 5 (commit message generation).

---

### Phase 5: Commit Message (Optional)
**Skill:** `commit-message` (standalone skill, not part of algo-rpi skillset)

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
- **Update after Research:** Add key findings and candidate approaches to `activeContext.md`
- **Update after Plan:** Add design decisions and quantitative targets to `activeContext.md`
- **Update after Implement:** Update `progress.md` with completed work and final metrics
- **Update after Review:** Mark task complete in `activeContext.md`

---

## Reproducibility Requirements

**MANDATORY** at every phase:

1. **Random Seeds:** Set and document Python, NumPy, PyTorch/TensorFlow seeds
2. **Deterministic Ops:** Use deterministic algorithms where possible, document non-deterministic ops
3. **Version Pinning:** Pin all dependency versions in requirements file
4. **Data Versioning:** Record dataset version or hash
5. **Verification:** Same seed → same results across multiple runs

---

## Quick Reference

**Starting the full workflow:**
```
/algo-rpi

Problem: [describe the algorithmic problem]
Constraints: [latency/memory/accuracy requirements]
Data: [dataset characteristics]
Hardware: [CPU/GPU, memory limits]
Metrics: [target thresholds]
```

**Invoking individual phases:**
- `/algo-rpi-research` — Algorithm research phase only
- `/algo-rpi-plan` — Algorithm plan phase only (provide research doc)
- `/algo-rpi-implement` — Algorithm implement phase only (provide plan doc)
- `/code-review` — Code review (standalone)
- `/commit-message` — Commit message generation (standalone)

---

## Success Criteria

The workflow is complete when:
- [x] Research document created with candidate approaches
- [x] User selected approach from research
- [x] Implementation plan created with quantitative targets
- [x] All P0-P5 phases implemented and verified
- [x] Performance gates passed (P1, P2, P3, P4)
- [x] Code review passes all checks
- [x] Reproducibility verified (seeds, versions, deterministic)
- [x] Commit message generated (if requested)
- [x] Memory Bank updated with completion status

---

## Quantitative Verification

Every phase reports metrics in table format:

| Metric | Target | Achieved | Baseline | Status |
|--------|--------|----------|----------|--------|
| [Primary metric] | [value] | [value] | [value] | ✓/✗ |
| Latency | [ms] | [ms] | [ms] | ✓/✗ |
| Memory | [MB/GB] | [MB/GB] | [MB/GB] | ✓/✗ |

All performance claims must be backed by measurements.
