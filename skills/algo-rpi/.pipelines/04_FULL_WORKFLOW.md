# Full Algo-RPI Workflow with AI Expert Review

Complete Algorithm Research-Plan-Implement cycle with AI expert review phases, code review, and commit message generation.

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

### Phase 3: AI Expert Plan Review
**Skill:** `algo-rpi-plan-review`

**Objective:** Review the implementation plan as an AI/ML expert for theoretical soundness, practical implications, and algorithm alternatives.

**Process:**
1. Read Memory Bank files
2. Read the plan document from Phase 2
3. Read the research document (if available)
4. Apply expert review checklist across six dimensions:
   - Algorithm selection (is this the right algorithm?)
   - Theoretical soundness (convergence, complexity, statistical validity)
   - Numerical stability (precision, overflow, gradient issues)
   - Practical deployment (latency, memory, monitoring, maintenance)
   - Evaluation rigor (baselines, metrics, statistical testing)
   - Reproducibility (seeds, versions, determinism)
5. Annotate/modify plan in-place with expert insights
6. Flag critical issues that would block implementation
7. Suggest algorithm alternatives when genuinely beneficial
8. Update the plan document with review annotations

**Output:** Modified plan with expert review annotations, identified issues, and recommendations

**⏸️ PAUSE POINT:** Present review summary with critical/important/suggestion issues. Offer to proceed to Phase 4 (reimagine) or skip to Phase 5 (implement).

---

### Phase 4: AI Expert Plan Reimagine
**Skill:** `algo-rpi-plan-reimagine`

**Objective:** Reimagine the implementation plan from scratch, optimizing for algorithm efficiency, ML best practices, and production-readiness.

**Process:**
1. Read Memory Bank files
2. Read all context (research, original plan, reviewed plan)
3. Ask: "Knowing everything I know now, what's the elegant solution?"
4. Explore algorithm space systematically (different families, complexities, trade-offs)
5. Select optimal approach balancing all constraints
6. Design for production-readiness (latency, memory, monitoring, graceful degradation)
7. Write new plan (v2) with comprehensive rationale
8. Include comparison section explaining differences and improvements
9. Create v2 plan document in `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-<topic>-v2.md`

**Optimization Goals:**
- **Algorithm efficiency:** Time/space complexity, vectorization, parallelization
- **ML best practices:** Proper evaluation, avoiding leakage, statistical rigor
- **Production-readiness:** Latency, memory, monitoring, graceful degradation
- **Theoretical elegance:** Simpler solutions, principled approaches
- **Industry standards:** What would a senior ML engineer at a top tech company do?

**Output:** Reimagined plan (v2) with optimized algorithm design, comprehensive rationale, and comparison to original

**⏸️ PAUSE POINT:** Present v2 plan with comparison to original. Get user confirmation on which plan to implement (original reviewed or v2 reimagined).

---

### Phase 5: Algorithm Implement
**Skill:** `algo-rpi-implement`

**Objective:** Execute the approved plan phase by phase, meeting quantitative targets with reproducibility.

**Process:**
1. Read Memory Bank files
2. Read plan document (reviewed or v2, as selected by user)
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

**⏸️ PAUSE POINT:** Present implementation summary with final metrics table. Wait for user approval before proceeding to Phase 6.

---

### Phase 6: Code Review
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

**⏸️ PAUSE POINT:** Present code review summary. Offer to proceed to Phase 7 (commit message generation).

---

### Phase 7: Commit Message (Optional)
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
- **Update after Review:** Add expert insights and identified issues to `activeContext.md`
- **Update after Reimagine:** Add v2 design decisions and rationale to `activeContext.md`
- **Update after Implement:** Update `progress.md` with completed work and final metrics
- **Update after Code Review:** Mark task complete in `activeContext.md`

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

**Starting the full workflow with AI expert review:**
```
/algo-rpi-full

Problem: [describe the algorithmic problem]
Constraints: [latency/memory/accuracy requirements]
Data: [dataset characteristics]
Hardware: [CPU/GPU, memory limits]
Metrics: [target thresholds]
```

**Invoking individual phases:**
- `/algo-rpi-research` — Algorithm research phase only
- `/algo-rpi-plan` — Algorithm plan phase only (provide research doc)
- `/algo-rpi-plan-review` — AI expert plan review only (provide plan doc)
- `/algo-rpi-plan-reimagine` — AI expert plan reimagine only (provide plan doc)
- `/algo-rpi-implement` — Algorithm implement phase only (provide plan doc)
- `/code-review` — Code review (standalone)
- `/commit-message` — Commit message generation (standalone)

**Standard workflow (without expert review):**
```
/algo-rpi
```
This uses the default pipeline (00_DEFAULT.md) without the review and reimagine phases.

---

## Success Criteria

The workflow is complete when:
- [x] Research document created with candidate approaches
- [x] User selected approach from research
- [x] Implementation plan created with quantitative targets
- [x] AI expert review completed with annotations
- [x] AI expert reimagination completed (v2 plan created)
- [x] User selected plan for implementation (reviewed or v2)
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

---

## When to Use This Workflow

Use the **full workflow with AI expert review** (`/algo-rpi-full`) when:
- Algorithm choice is critical and needs expert validation
- Performance targets are aggressive and need optimization
- Production deployment requires high confidence in design
- You want a second opinion on the algorithm approach
- You're willing to invest time in thorough review and optimization

Use the **standard workflow** (`/algo-rpi`) when:
- Algorithm choice is straightforward
- Time constraints don't allow for extensive review
- The problem is well-understood and low-risk
- You're confident in the initial plan

Use **individual skills** when:
- You only need one phase (e.g., just planning, just review)
- You're iterating on a specific part of the workflow
- You want to customize the workflow order
