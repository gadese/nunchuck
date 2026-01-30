# Algorithm Implement Phase Only

Execute only the algorithm implementation phase based on existing plan.

## When to Use

Use this pipeline when you:
- Have an approved algorithm implementation plan ready to execute
- Need to resume interrupted algorithm implementation work
- Want to implement with quantitative verification at each phase
- Are continuing algorithm work from a previous session

## Prerequisites

**Required:**
- Plan document path from `llm_docs/plans/`

**Recommended:**
- Baseline harness and dataset splits prepared
- Quantitative targets confirmed
- Hardware environment ready
- Dependencies installed

## Process

### Phase 1: Algorithm Implement
**Skill:** `algo-rpi-implement`

**Objective:** Execute the approved plan phase by phase, meeting quantitative targets with reproducibility.

**Steps:**

1. **Context Gathering**
   - Read Memory Bank files (`activeContext.md`, `systemPatterns.md`)
   - Read plan document completely
   - Identify all phases, quantitative targets, success criteria, dependencies
   - Check for existing checkmarks (`- [x]`) to identify completed work
   - Extract Quantitative Targets table for reference
   - Read all referenced materials (algorithm plan, research, code, datasets, baselines, benchmark harness)
   - Verify prerequisites (baseline metrics documented, dataset splits reproducible, benchmark harness functional)

2. **Mismatch Evaluation**
   
   Before implementing, assess discrepancies between plan and reality:

   **Minor mismatches** (proceed with adaptation):
   - Line numbers shifted, variable names differ slightly, dataset path moved, baseline metrics differ <5%

   **Major mismatches** (STOP and ask):
   - Quantitative targets missing, dataset unavailable, baseline harness broken, hardware mismatch, dependencies incompatible, existing implementation conflicts

   Present major mismatches with impact analysis and options.

3. **Phase-by-Phase Implementation (P0 → P5)**
   
   For each phase:

   **Announce the phase:**
   ```
   Starting Phase [PN]: [Phase Name]
   Objective: [What this phase achieves]
   Target metrics: [Relevant targets]
   ```

   **Implement deliverables:**
   - Follow implementation steps in order
   - Keep changes incremental and testable
   - Prefer clear, typed functions with single responsibility
   - Use vectorized operations (NumPy) where applicable
   - Prefer OpenCV (`cv2`) for imaging operations
   - Ensure reproducibility: fixed seeds, deterministic ops

   **Handle algorithm-specific concerns:**
   - Validate numerical stability
   - Check for edge cases in data
   - Verify input/output shapes and types
   - Add assertions for invariants

   **Update plan document:**
   - Check off completed items using `- [x]`
   - Add brief notes on any adaptations

4. **Phase Verification**
   
   After completing each phase:

   **Code quality checks:**
   ```bash
   ruff check .
   ruff format --check .
   pytest [relevant test files]
   ```

   **Algorithm-specific verification:**
   - Run benchmark harness and record metrics
   - Compare results against baseline
   - Verify reproducibility (same seed → same results)
   - Check memory usage and latency against targets

   **Report results with measurements:**
   ```
   Phase [PN] Complete ✓
   
   Code Quality:
   - [x] ruff check passes
   - [x] ruff format passes
   - [x] pytest passes ([N] tests)
   
   Quantitative Results:
   | Metric | Target | Achieved | Baseline | Status |
   |--------|--------|----------|----------|--------|
   | [metric] | [value] | [value] | [value] | ✓/✗ |
   
   Reproducibility:
   - [x] Seed [X] produces identical results across [N] runs
   
   Notes: [Observations]
   ```

   **Fix issues before proceeding:**
   - Do not move to next phase with failing tests
   - Do not proceed if metrics significantly below target

5. **Performance & Accuracy Gates**
   
   At key milestones, verify quantitative targets:

   **After P1 (Prototype):**
   - Algorithm produces correct output on test cases
   - Metrics within specified tolerance of target on small subset

   **After P2 (Evaluation):**
   - Primary metric meets or exceeds target on full test set
   - Results are statistically significant (if applicable)
   - Ablation studies documented (if applicable)

   **After P3 (Optimization):**
   - Latency meets target
   - Memory usage meets target
   - No regression in accuracy metrics

   **After P4 (Robustness):**
   - Edge case tests pass
   - Deterministic across multiple runs with same seed
   - Graceful failure on invalid inputs

   **Gate Failure Protocol:**
   If a gate is not met:
   1. Document the gap (target vs achieved)
   2. Analyze root cause
   3. Present options to user (adjust target, additional work, accept limitation)

6. **Completion & Handoff**
   
   When all phases complete:

   **Final verification:**
   - Run full test suite
   - Run complete benchmark suite
   - Verify all quantitative targets met
   - Confirm reproducibility checklist

   **Update plan document:**
   - Ensure all checkboxes marked
   - Add final metrics to Quantitative Targets table
   - Add completion timestamp

   **Update Memory Bank:**
   - Update `activeContext.md` with completion status
   - Update `progress.md` with completed work

   **Summary report:**
   ```
   Algorithm Implementation Complete ✓
   
   Phases completed: [N/N]
   
   Final Metrics:
   | Metric | Target | Achieved | vs Baseline |
   |--------|--------|----------|-------------|
   | [metric] | [value] | [value] | +X% / -X% |
   
   Files modified: [list]
   Tests added: [list]
   
   Reproducibility:
   - [x] Seeds documented: [seed values]
   - [x] Versions pinned in [requirements file]
   - [x] Hardware config documented
   
   Deviations from plan: [Any adaptations and rationale]
   
   Ready for review.
   ```

**Output:** Algorithm implementation code, benchmark results, updated plan with checkmarks, reproducibility artifacts

**⏸️ PAUSE POINT:** Present implementation summary with final metrics table. Implementation phase complete.

---

## Reproducibility Requirements

**MANDATORY for every phase:**

1. **Random seeds:** Document and set all seeds (Python, NumPy, PyTorch/TensorFlow)
2. **Deterministic ops:** Use deterministic algorithms, document non-deterministic ops
3. **Version pinning:** Pin all dependency versions in requirements file
4. **Data versioning:** Record dataset version or hash
5. **Verification:** Same seed → same results across multiple runs

---

## Resuming Interrupted Work

If the plan has existing checkmarks:
1. **Trust completed work** — Assume checked phases are done correctly
2. **Verify continuity** — Check baseline harness works, dataset splits unchanged, last phase metrics reproducible
3. **Resume from first unchecked phase** — Pick up exactly where work stopped

---

## Quick Reference

**Invoking implement only:**
```
/algo-rpi-implement

Plan document: llm_docs/plans/[filename].md
Targets: [confirm or update]
Environment: [hardware ready, dependencies installed]
Dataset: [splits prepared, baseline harness functional]
```

---

## Next Steps

After implementation is complete, you can:
1. Invoke `/code-review` to review implemented code
2. Invoke `/commit-message` to generate commit message
3. Manually test and verify the implementation
4. Deploy or integrate the algorithm
