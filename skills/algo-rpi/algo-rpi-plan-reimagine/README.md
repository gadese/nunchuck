# algo-rpi-plan-reimagine

AI/ML expert reimagination of algorithm implementation plans, optimizing for algorithm efficiency, ML best practices, and production-readiness.

## Purpose

Acts as an AI/ML expert who rewrites algorithm implementation plans from scratch, asking: "Knowing everything I know now, what's the elegant solution?" Optimizes for:

- **Algorithm efficiency:** Time/space complexity, vectorization, parallelization
- **ML best practices:** Proper evaluation, avoiding leakage, statistical rigor
- **Production-readiness:** Latency, memory, monitoring, graceful degradation
- **Theoretical elegance:** Simpler solutions, principled approaches
- **Industry standards:** What would a senior ML engineer at a top tech company do?

## When to Use

- After `algo-rpi-plan-review` identifies significant issues
- As part of the `/algo-rpi-full` workflow (Phase 4)
- When you want a fresh perspective on algorithm design
- When the original plan needs substantial revision

## What It Does

1. Reads all context (research, original plan, reviewed plan)
2. Asks: "What's the elegant solution given all constraints?"
3. Considers whether a different algorithm family would work better
4. Writes a new plan (v2) optimizing for robustness, efficiency, and production-readiness
5. Presents rationale comparing v2 to original approach
6. Outputs the reimagined plan as a new document

## What It Does NOT Do

- Does not implement code
- Does not modify the original plan (creates a new v2 plan)
- Does not ignore the research or original plan (uses them as input)
- Does not make changes for the sake of change (only when genuinely better)

## Output

New plan document (v2) with optimized algorithm design, comprehensive rationale, and comparison to original approach. Saved as a new file with `-v2` suffix.

## Invocation

```
/algo-rpi-plan-reimagine
```

Or as part of the full workflow:

```
/algo-rpi-full
```
