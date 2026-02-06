# Always

## Mandatory Requirements

**YOU MUST:**

- **Read the plan document completely** — Understand the problem, selected approach, quantitative targets, and all P0-P5 phases before reviewing

- **Read the research document if available** — Understand the context and rationale behind algorithm selection

- **Read Memory Bank files** — Check `llm_docs/memory/activeContext.md`, `systemPatterns.md`, and `techContext.md` for relevant context

- **Apply the expert review checklist systematically** — Cover all six review dimensions (see below)

- **Modify the plan directly** — Rewrite and improve plan sections to address identified issues; do not leave review comments or annotations

- **Provide rationale in the summary** — When presenting your summary to the user, explain WHY each modification was made

- **Quantify concerns** — Use specific numbers, complexity bounds, or measurable criteria

- **Be constructive** — Suggest solutions, not just problems

- **Preserve good decisions** — Acknowledge what's done well; don't change things unnecessarily

- **Flag critical blockers clearly** — If something would prevent successful implementation, mark it as **CRITICAL**

- **Consider algorithm alternatives thoughtfully** — Only suggest different algorithms when genuinely beneficial, not reflexively

- **Verify numerical stability** — Check for precision loss, overflow/underflow, gradient issues, matrix conditioning

- **Validate quantitative targets** — Ensure latency/memory/accuracy targets are achievable with the chosen approach

- **Check reproducibility** — Verify seeds, version pins, determinism guarantees are adequate

- **Update the plan document** — Write the modified plan back to the same file path

- **Summarize changes** — Present a concise summary of modifications and their rationale

## Expert Review Checklist

Apply this checklist systematically to every plan:

### 1. Algorithm Selection
- [ ] Is the chosen algorithm appropriate for the problem constraints?
- [ ] Are there better-suited algorithms that weren't considered?
- [ ] Does the complexity analysis (time/space) match the performance targets?
- [ ] Are the trade-offs (accuracy vs speed vs memory) well-reasoned?
- [ ] Is the algorithm family (optimization, search, ML model, etc.) the right fit?

### 2. Theoretical Soundness
- [ ] Are convergence guarantees valid for this problem?
- [ ] Is the statistical reasoning correct (hypothesis tests, confidence intervals)?
- [ ] Are complexity bounds accurate (Big-O analysis)?
- [ ] Are assumptions about data distribution reasonable?
- [ ] Are approximation errors bounded and acceptable?

### 3. Numerical Stability
- [ ] Are there precision loss risks (e.g., subtracting similar floats)?
- [ ] Could operations overflow or underflow (large/small number ranges)?
- [ ] Are gradients likely to vanish or explode (deep networks, long sequences)?
- [ ] Is matrix conditioning considered (ill-conditioned systems)?
- [ ] Are numerical tolerances (epsilon values) appropriate?
- [ ] Are accumulation errors bounded (iterative algorithms)?

### 4. Practical Deployment
- [ ] Are latency targets achievable with the chosen approach on target hardware?
- [ ] Is memory usage realistic for the target hardware and batch sizes?
- [ ] Can this be monitored effectively in production (metrics, logging)?
- [ ] Is the maintenance burden reasonable (complexity, dependencies)?
- [ ] Are failure modes handled gracefully (invalid inputs, edge cases)?
- [ ] Will this scale to production data volumes?

### 5. Evaluation Rigor
- [ ] Are baselines appropriate and sufficient (random, simple heuristic, prior work)?
- [ ] Are metrics aligned with the actual objective (not proxy metrics)?
- [ ] Is statistical testing adequate (significance tests, confidence intervals)?
- [ ] Are ablations meaningful (isolate component contributions)?
- [ ] Is the test set truly held out (no leakage from train/val)?
- [ ] Are evaluation datasets representative of production distribution?

### 6. Reproducibility
- [ ] Are random seeds fixed everywhere needed (data splits, initialization, sampling)?
- [ ] Are dependency versions pinned (libraries, frameworks)?
- [ ] Are deterministic operations enforced where critical (GPU ops, parallel reductions)?
- [ ] Can results be reproduced from the artifacts (configs, seeds, data hashes)?
- [ ] Is hardware configuration documented (CPU/GPU model, memory)?

## How to Modify the Plan

When you identify an issue, **directly rewrite the affected section** to fix it. Do not leave review comments, annotations, or markers in the plan — no one will come back to read them. The plan must be a clean, improved document after your review.

For example, if the plan says:
```markdown
- **Algorithm:** Bubble sort
- **Complexity:** O(n²) time, O(1) space
```

Do NOT add a comment like `**[EXPERT: This is too slow]**`. Instead, rewrite the section:
```markdown
- **Algorithm:** Timsort (Python built-in `sorted()`)
- **Complexity:** O(n log n) time, O(n) space
- **Rationale:** Achieves 50ms latency target while remaining simple (built-in function)
```

## Critical Issue Escalation

If you identify a **CRITICAL** issue that would prevent successful implementation:

1. Fix it directly in the plan by rewriting the affected section
2. If the fix requires a user decision (e.g., choosing between two valid approaches), note this in your summary and ask the user
3. If the issue is fundamental enough that the plan needs a complete rethink, recommend `algo-rpi-plan-reimagine` instead
