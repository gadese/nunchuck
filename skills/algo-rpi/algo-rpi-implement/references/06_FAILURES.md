# Failures

## Failure Modes and Recovery

### Missing Plan Document

**Symptom:** No plan document provided or path is invalid

**Recovery:**
1. Request plan document path from user
2. Explain that implementation requires approved plan
3. Offer to wait for planning completion

### Quantitative Targets Not Met

**Symptom:** Phase verification shows metrics below target

**Recovery:**
1. Document the gap (target vs achieved)
2. Analyze root cause (algorithm issue, data issue, implementation bug)
3. Present options to user:
   - Debug and fix implementation
   - Adjust algorithm parameters
   - Revise target (with justification)
   - Accept current performance with documented limitations
4. Get user decision before proceeding

### Baseline Harness Missing or Broken

**Symptom:** Cannot run benchmarks or measure metrics

**Recovery:**
1. Make P0 phase focus on creating baseline harness
2. Document that harness needs to be built
3. Implement minimal harness to measure metrics
4. Verify harness works before proceeding to P1

### Dataset Issues

**Symptom:** Dataset unavailable, corrupted, or different from plan expectations

**Recovery:**
1. Document the issue explicitly
2. Check if dataset path has moved
3. Verify dataset integrity (checksums, file counts)
4. If dataset is fundamentally different, STOP and present mismatch
5. Get user guidance before proceeding

### Reproducibility Failures

**Symptom:** Same seed produces different results across runs

**Recovery:**
1. Identify non-deterministic operations
2. Check for:
   - Missing seed initialization
   - Non-deterministic algorithms (e.g., CUDA operations)
   - Hash ordering issues
   - Parallel processing race conditions
3. Fix determinism issues
4. Re-verify reproducibility before proceeding

### Performance Gate Failures

**Symptom:** Phase completes but doesn't meet performance gate criteria

**Recovery:**
1. Document which gate failed and by how much
2. Analyze bottleneck or accuracy issue
3. Present options:
   - Additional optimization work (if P3)
   - Algorithm parameter tuning
   - Revise target with justification
   - Accept limitation and document
4. Get user decision before proceeding

### Numerical Instability

**Symptom:** NaN, Inf, or extreme values in computations

**Recovery:**
1. Identify where instability occurs
2. Check for:
   - Division by zero
   - Log of zero or negative
   - Overflow/underflow
   - Ill-conditioned matrices
3. Add numerical safeguards (clipping, epsilon values)
4. Verify stability on edge cases
5. Document numerical considerations

### Hardware Environment Mismatch

**Symptom:** Plan assumes GPU but only CPU available (or vice versa)

**Recovery:**
1. Present the mismatch explicitly
2. Adjust implementation for available hardware
3. Revise quantitative targets based on hardware
4. Document hardware assumptions
5. Get user confirmation before proceeding

### Dependency Conflicts

**Symptom:** Required libraries incompatible or missing

**Recovery:**
1. Document the conflict
2. Check if versions can be resolved
3. Update requirements file with compatible versions
4. Test that algorithm still works with new versions
5. Document version changes in plan notes

## Artifact Validation

Before completing implementation, verify:
- [ ] All P0-P5 phases complete with checkmarks
- [ ] Quantitative targets met or documented exceptions
- [ ] All automated checks pass (ruff, pytest)
- [ ] Reproducibility verified (same seed → same results)
- [ ] Memory Bank updated with completion status
- [ ] Final metrics table updated in plan
- [ ] Reproducibility artifacts created (requirements, seeds, configs)

## Handoff Checklist

Before handing off to review phase:
- [ ] Implementation complete with all phases done
- [ ] Plan document updated with all checkmarks
- [ ] Summary report presented with final metrics
- [ ] Memory Bank updated
- [ ] All tests passing
- [ ] Reproducibility verified

If any item fails, address it before completing the implementation phase.

## Common Implementation Pitfalls

**Avoid:**
- Skipping reproducibility verification
- Proceeding with failing tests
- Optimizing before evaluating (P3 before P2)
- Ignoring numerical stability
- Not documenting seeds and versions
- Reporting vague performance claims
- Modifying files outside plan scope
- Questioning algorithm choice (that was planning phase)

**Ensure:**
- Every metric is measured and reported
- Every phase is verified before proceeding
- Reproducibility is maintained throughout
- Quantitative targets are met or exceptions documented
- Plan checkboxes are updated as work completes
- Memory Bank is updated at completion
