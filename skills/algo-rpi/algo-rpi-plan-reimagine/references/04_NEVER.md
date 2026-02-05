# Never

## Prohibited Actions

**YOU MUST NEVER:**

- **Reimagine without reading all context** — You need the full picture (research, original plan, review) to optimize effectively

- **Change things for the sake of change** — Only reimagine when genuinely better, not to justify the exercise

- **Ignore the original plan's strengths** — If something was done well, preserve it

- **Introduce unnecessary complexity** — Simpler is better; don't over-engineer

- **Recommend unproven techniques** — Stick to well-established algorithms and practices

- **Ignore practical constraints** — Theoretical elegance is worthless if it can't deploy

- **Overwrite the original plan** — Always create a new v2 document

- **Skip the comparison section** — Must explain what changed and why

- **Make vague improvements** — "This is better" is useless; quantify the improvement

- **Introduce new numerical stability issues** — Check that optimizations don't break correctness

- **Weaken reproducibility** — The v2 plan must be at least as reproducible as the original

- **Ignore review feedback** — If a review was done, address the issues it raised

- **Change quantitative targets arbitrarily** — Only adjust if the original targets were unrealistic

- **Abandon the P0-P5 structure** — This is the standard algorithm development framework

- **Add implementation code** — This is a planning skill, not implementation

- **Create multiple plan versions** — One v2 plan, not v2, v3, v4, etc.

- **Modify files outside the plan document** — Only create the new v2 plan

- **Skip Memory Bank updates** — Design decisions must be recorded

- **Assume the original planner was incompetent** — Assume competence; look for genuine improvements

## Approaches to Avoid

### Over-Engineering
**Bad:** "Let's use a custom neural architecture with attention mechanisms and multi-task learning"
**Good:** "A simple logistic regression achieves 95% accuracy, meeting the target"

### Premature Optimization
**Bad:** "Let's implement SIMD vectorization and GPU kernels in P1"
**Good:** "P1 focuses on correctness; P3 will optimize based on profiling results"

### Novelty for Novelty's Sake
**Bad:** "Let's try this new algorithm from a recent paper"
**Good:** "Let's use k-d trees, a well-established O(log n) solution used in production at scale"

### Ignoring Constraints
**Bad:** "This algorithm is theoretically optimal but requires 100GB RAM"
**Good:** "This algorithm achieves near-optimal results within the 8GB memory constraint"

### Vague Improvements
**Bad:** "The new approach is more efficient"
**Good:** "The new approach reduces time complexity from O(n²) to O(n log n), achieving 50x speedup for n=10,000"

## Tone to Avoid

- **Dismissive:** "The original plan was completely wrong"
- **Arrogant:** "Obviously, the right approach is..."
- **Vague:** "This seems better"
- **Overly cautious:** "Maybe we could possibly consider..."
- **Condescending:** "Any experienced ML engineer would know..."

## Appropriate Tone

- **Constructive:** "Building on the original plan's foundation, here's an optimized approach"
- **Specific:** "Switching from bubble sort to Timsort reduces latency from 500ms to 5ms"
- **Balanced:** "The original algorithm choice was reasonable, but we can achieve better efficiency with..."
- **Confident:** "Based on the constraints and requirements, here's the optimal design"
- **Respectful:** "The original plan identified the right problem; this reimagination optimizes the solution"

## Scope Boundaries

**This skill reimagines plans. It does NOT:**

- Implement code (that's `algo-rpi-implement`)
- Review existing plans (that's `algo-rpi-plan-review`)
- Conduct research (that's `algo-rpi-research`)
- Run experiments or benchmarks
- Modify source code files
- Create test cases (those go in the plan for the implementer)
- Make multiple iterations (create one v2 plan, not v2, v3, v4)

**Stay within scope:** Create one optimized v2 plan with comprehensive rationale.

## When NOT to Reimagine

Don't reimagine if:

- **Original plan is already optimal** — No genuine improvements to make
- **Changes would be cosmetic** — Different wording but same substance
- **Improvements are marginal** — Not worth the complexity of having two plans
- **User just wants minor edits** — Use `algo-rpi-plan-review` instead
- **No context available** — Can't optimize without understanding the problem

**If the original plan is already excellent, say so clearly:**

```markdown
## Reimagination Assessment

After thorough analysis of the original plan, research document, and review feedback, I conclude that the original plan is already optimal for the given constraints.

**Strengths of Original Plan:**
- Algorithm choice (k-d tree) is optimal for O(log n) query time
- Numerical stability is thoroughly addressed
- Evaluation methodology is rigorous
- Production-readiness is comprehensive

**No Reimagination Needed:**
The original plan represents the best approach given the constraints. Proceeding with a "v2" plan would introduce unnecessary complexity without genuine improvements.

**Recommendation:** Proceed to implementation with the original plan.
```

## Trade-off Transparency

When making trade-offs, be explicit:

**Bad:**
```markdown
The new algorithm is better.
```

**Good:**
```markdown
**Trade-off:** The new algorithm (approximate nearest neighbor) sacrifices 2% accuracy for 100x speedup.

**Justification:** The latency requirement (10ms) cannot be met with exact nearest neighbor (1000ms), and 98% accuracy still exceeds the 95% target. This trade-off is necessary and acceptable.
```

## Avoid These Common Mistakes

1. **Changing algorithm without justification** — Always explain WHY the new algorithm is better
2. **Ignoring the research document** — The research provides critical context
3. **Breaking integration interfaces** — The plan must align with existing codebase
4. **Introducing untested libraries** — Prefer established, well-maintained libraries
5. **Weakening evaluation rigor** — The v2 plan must be at least as rigorous as the original
6. **Adding phases beyond P0-P5** — Stick to the standard structure
7. **Creating an unimplementable plan** — The plan must be actionable, not just theoretical
8. **Forgetting to update Memory Bank** — Design decisions must be recorded

## Remember

You're optimizing, not criticizing. The goal is to create the best possible plan, not to prove the original was wrong. Frame the v2 plan as "here's an even better approach" not "the original was flawed."
