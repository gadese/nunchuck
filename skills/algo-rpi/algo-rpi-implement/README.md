# Algo-RPI Implement

Algorithm implementation execution for the Algo-RPI workflow.

## Purpose

This skill executes approved algorithm implementation plans with quantitative verification and reproducibility. It implements algorithms phase by phase (P0-P5), measures performance against targets, and ensures results are reproducible.

## When to Use

Use this skill when you:
- Have an approved algorithm implementation plan ready to execute
- Need to resume interrupted algorithm implementation work
- Want to implement with quantitative verification at each phase
- Are continuing algorithm work from a previous session

## Key Features

- **Phase-by-phase execution** following P0-P5 structure
- **Quantitative verification** after each phase with metrics tables
- **Performance gates** at P1, P2, P3, P4 milestones
- **Reproducibility enforcement** with seeds, versions, deterministic ops
- **Progress tracking** with plan checkbox updates
- **Mismatch evaluation** before implementation begins

## Output

- Code changes in source files
- Updated plan with checkboxes marked (`- [x]`)
- Progress reports with quantitative measurements after each phase
- Final summary with metrics table comparing target vs achieved vs baseline

## Invocation

```
/algo-rpi-implement

Plan document: llm_docs/plans/[filename].md
Targets: [confirm or update]
Environment: [hardware ready, dependencies installed]
Dataset: [splits prepared, baseline harness functional]
```

## P0-P5 Implementation Flow

**P0: Baseline & Harness**
- Establish baseline metrics
- Create dataset splits with fixed seeds
- Build benchmark harness
- Verify: Baseline documented, splits reproducible, harness functional

**P1: Prototype**
- Implement minimal viable algorithm
- Verify correctness on test cases
- Check metrics on small subset
- Verify: Correct output, metrics within tolerance, tests pass

**P2: Evaluation**
- Full dataset evaluation
- Ablation studies
- Statistical significance testing
- Verify: Primary metric ≥ target, statistically significant, ablations documented

**P3: Optimization**
- Profile and optimize
- Vectorize and parallelize
- Meet latency/memory targets
- Verify: Latency ≤ target, memory ≤ target, no accuracy regression

**P4: Robustness**
- Edge case testing
- Determinism verification
- Error handling
- Verify: Edge cases pass, deterministic, graceful failure

**P5: Packaging**
- Documentation
- Examples
- Reproducibility artifacts
- Verify: Docs complete, example works, reproducible

## Performance Gates

After each major phase, verify quantitative targets:

**Gate 1 (after P1):** Correctness on test cases, metrics within tolerance on small subset

**Gate 2 (after P2):** Primary metric meets target on full test set, statistically significant

**Gate 3 (after P3):** Latency and memory meet targets, no accuracy regression

**Gate 4 (after P4):** Edge cases pass, deterministic, graceful failure

If a gate fails:
1. Document gap (target vs achieved)
2. Analyze root cause
3. Present options (adjust target, additional work, accept limitation)
4. Get user decision

## Reproducibility Requirements

**Mandatory for every phase:**

1. **Random seeds:** Document and set all seeds (Python, NumPy, PyTorch/TF)
2. **Deterministic ops:** Use deterministic algorithms, document non-deterministic ops
3. **Version pinning:** Pin dependencies in requirements file
4. **Data versioning:** Record dataset version/hash
5. **Verification:** Same seed → same results across multiple runs

## Example

```
/algo-rpi-implement

Plan document: llm_docs/plans/2026-01-15-1430-plan-algo-object-detection.md
```

The skill will:
1. Read plan and verify prerequisites (baseline, dataset, harness)
2. Execute P0: Establish baseline (mAP@0.5=0.87, latency=45ms)
3. Execute P1: Implement YOLOv8 prototype, verify correctness
4. Execute P2: Full evaluation, achieve mAP@0.5=0.96 (target: 0.95) ✓
5. Execute P3: Optimize to 28ms latency (target: 30ms) ✓
6. Execute P4: Test edge cases, verify determinism ✓
7. Execute P5: Create docs and reproducibility artifacts ✓
8. Report final metrics and update Memory Bank

## Quantitative Reporting

Every phase reports metrics in table format:

| Metric | Target | Achieved | Baseline | Status |
|--------|--------|----------|----------|--------|
| mAP@0.5 | 0.95 | 0.96 | 0.87 | ✓ |
| Latency | 30ms | 28ms | 45ms | ✓ |
| Memory | 2GB | 1.8GB | 3.2GB | ✓ |

All claims must be backed by measurements.

## Mismatch Evaluation

Before implementing, the skill evaluates discrepancies:

**Minor mismatches (proceed with adaptation):**
- Line numbers shifted
- Variable names differ slightly
- Dataset path moved
- Baseline metrics differ <5%

**Major mismatches (STOP and ask):**
- Quantitative targets missing
- Dataset unavailable
- Baseline harness broken
- Hardware mismatch
- Dependencies incompatible

## Integration with Algo-RPI Workflow

This is the third phase of the Algo-RPI workflow:
1. **Research** (`algo-rpi-research`) → Formalize problem, explore solutions
2. **Plan** (`algo-rpi-plan`) → Select approach, create implementation plan
3. **Implement** (this skill) → Execute plan with quantitative verification

## See Also

- `algo-rpi-research/` — Algorithm research skill
- `algo-rpi-plan/` — Algorithm planning skill
- `rpi-implement/` — General software implementation (use for non-algorithmic tasks)
- `code-review/` — Code quality review (invoke after implementation)
- `coding-standards/` — Shared coding guidelines
