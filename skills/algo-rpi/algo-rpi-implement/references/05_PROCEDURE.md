# Procedure

## Implementation Process

Follow these steps in order:

### Step 1: Context Gathering

1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns

2. **Read the plan completely**
   - Identify all phases, quantitative targets, and success criteria
   - Note any existing checkmarks indicating prior progress
   - Understand the dependencies between phases
   - Extract the Quantitative Targets table for reference

3. **Read all referenced materials**
   - Algorithm plan and research documents
   - Existing code files referenced in the plan
   - Dataset schemas and baseline implementations
   - Benchmark harness if it exists

4. **Verify prerequisites**
   - Confirm baseline metrics are documented
   - Confirm dataset splits are reproducible
   - Confirm benchmark harness is functional
   - Note any discrepancies for mismatch evaluation

### Step 2: Mismatch Evaluation

Before implementing, assess discrepancies between the plan and reality:

**Minor mismatches** (use judgment, proceed with adaptation):
- Line numbers have shifted due to unrelated changes
- Variable/function names differ slightly but intent is clear
- Dataset path has moved but data is identical
- Baseline metrics differ slightly from plan (within 5%)

**Major mismatches** (STOP and ask):
- Quantitative targets are missing or unclear
- Dataset is unavailable or has different characteristics
- Baseline harness doesn't exist or produces errors
- Hardware assumptions don't match available environment
- Key dependencies are missing or incompatible
- Existing implementation conflicts with plan approach

When encountering a major mismatch, present it as:

**Mismatch in Phase [PN]: [Phase Name]**

| Aspect | Expected (Plan) | Found (Reality) |
|--------|-----------------|-----------------|
| [Item] | [Plan says]     | [Actual state]  |

**Impact on Quantitative Targets:**
- [How this affects ability to meet targets]

**Options:**
1. [Possible adaptation]
2. [Alternative approach]
3. [Prerequisite work needed first]

How should I proceed?

### Step 3: Phase-by-Phase Implementation

For each phase in the plan (P0 → P5):

1. **Announce the phase**
   ```
   Starting Phase [PN]: [Phase Name]
   Objective: [What this phase achieves]
   Target metrics: [Relevant targets for this phase]
   ```

2. **Implement deliverables**
   - Follow the implementation steps in order
   - Keep changes incremental and testable
   - Prefer clear, typed functions with single responsibility
   - Use vectorized operations (NumPy) where applicable
   - Prefer OpenCV (`cv2`) for imaging operations
   - Ensure reproducibility: fixed seeds, deterministic ops

3. **Handle algorithm-specific concerns**
   - Validate numerical stability
   - Check for edge cases in data
   - Verify input/output shapes and types
   - Add assertions for invariants

4. **Update the plan document**
   - Check off completed items using `- [x]`
   - Add brief notes on any adaptations

### Step 4: Phase Verification

After completing each phase, run verification:

1. **Code quality checks**
   ```bash
   ruff check .
   ruff format --check .
   pytest [relevant test files]
   ```

2. **Algorithm-specific verification**
   - Run benchmark harness and record metrics
   - Compare results against baseline
   - Verify reproducibility (same seed → same results)
   - Check memory usage and latency against targets

3. **Report results with measurements**
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
   
   Notes: [Observations, minor adaptations, or concerns]
   ```

4. **Fix issues before proceeding**
   - Do not move to the next phase with failing tests
   - Do not proceed if metrics are significantly below target
   - If a fix requires plan deviation, apply mismatch protocol

### Step 5: Performance & Accuracy Gates

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
3. Present options to user:
   - Adjust target (with justification)
   - Additional optimization work
   - Accept current performance with documented limitations

### Step 6: Completion & Handoff

When all phases are complete:

1. **Final verification**
   - Run full test suite
   - Run complete benchmark suite
   - Verify all quantitative targets met
   - Confirm reproducibility checklist

2. **Update plan document**
   - Ensure all checkboxes are marked
   - Add final metrics to Quantitative Targets table
   - Add completion timestamp

3. **Update Memory Bank**
   - Update `llm_docs/memory/activeContext.md` with completion status
   - Update `llm_docs/memory/progress.md` with completed work

4. **Summary report**
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
   
   Deviations from plan:
   - [Any adaptations and rationale]
   
   Ready for review.
   ```

## Reproducibility Requirements

**YOU MUST** ensure reproducibility at every phase:

1. **Random seeds**
   - Document all seeds used (Python, NumPy, PyTorch/TensorFlow if applicable)
   - Set seeds at the beginning of each run
   - Verify identical results across runs with same seed

2. **Deterministic operations**
   - Use deterministic algorithms where possible
   - Document any non-deterministic operations and their impact
   - Set `PYTHONHASHSEED` if hash ordering matters

3. **Version pinning**
   - Pin all dependency versions in requirements file
   - Document Python version
   - Record hardware configuration (CPU/GPU model, CUDA version if applicable)

4. **Data versioning**
   - Record dataset version or hash
   - Document any data preprocessing steps
   - Ensure train/val/test splits are deterministic

## Resuming Interrupted Work

If the plan has existing checkmarks:

1. **Trust completed work**
   - Assume checked phases are done correctly
   - Trust documented baseline metrics

2. **Verify continuity**
   - Check that baseline harness still works
   - Confirm dataset splits are unchanged
   - Verify last phase's metrics are reproducible

3. **Resume from first unchecked phase**
   - Pick up exactly where work stopped
   - Apply the same verification rigor

## Quality Guidelines

- Follow existing codebase patterns and conventions
- Respect workspace rules (code principles, ML guides)
- Use strict type hints everywhere
- Prefer vectorized operations (NumPy, OpenCV)
- Keep modules focused with single responsibility
- Write clear, typed functions
- Add assertions to validate invariants
- Document numerical considerations (precision, stability)
