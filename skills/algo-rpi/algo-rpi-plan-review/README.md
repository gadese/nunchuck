# algo-rpi-plan-review

AI/ML expert review of algorithm implementation plans for theoretical soundness, practical implications, and algorithm alternatives.

## Purpose

Acts as an AI/ML expert reviewer who evaluates algorithm implementation plans with both theoretical depth and industry experience. Reviews plans for:

- **Theoretical soundness:** Convergence properties, complexity analysis, statistical validity
- **Numerical stability:** Precision issues, overflow/underflow risks, gradient problems
- **Industry practicality:** Deployment constraints, maintenance burden, monitoring requirements
- **Algorithm alternatives:** Better-suited approaches that may have been overlooked

## When to Use

- After `algo-rpi-plan` produces an implementation plan
- As part of the `/algo-rpi-full` workflow (Phase 3)
- Standalone when you need expert validation of an algorithm plan

## What It Does

1. Reads the algorithm implementation plan
2. Evaluates algorithm choice against problem constraints
3. Checks for theoretical and practical concerns
4. Identifies numerical stability risks
5. Considers alternative algorithms when appropriate
6. Directly rewrites plan sections to fix identified issues
7. Presents a summary of changes with rationale

## What It Does NOT Do

- Does not implement code
- Does not create new plans from scratch (see `algo-rpi-plan-reimagine` for that)
- Does not reject plans arbitrarily—provides constructive feedback
- Does not always suggest alternatives—only when genuinely beneficial

## Output

Modified plan document with issues directly fixed. The plan reads as a clean, improved document — no review comments or annotations are left behind. A summary of changes with rationale is presented in chat.

## Invocation

```
/algo-rpi-plan-review
```

Or as part of the full workflow:

```
/algo-rpi-full
```
