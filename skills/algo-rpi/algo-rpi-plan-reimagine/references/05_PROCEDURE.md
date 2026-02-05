# Procedure

## Reimagination Process

Follow these steps in order to create an optimized v2 algorithm implementation plan.

### Phase 1: Comprehensive Context Gathering

1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

2. **Read All Plan Documents**
   - Read the original plan completely
   - Read the reviewed plan if available
   - Understand the problem statement, selected approach, and all P0-P5 phases
   - Note the quantitative targets and constraints

3. **Read the Research Document**
   - Understand the problem context and rationale
   - Note alternative approaches that were considered
   - Identify integration points and constraints
   - Understand dataset characteristics and evaluation methodology

4. **Identify Optimization Goals**
   - What feedback did the review provide?
   - What are the main weaknesses of the original plan?
   - What should we optimize for? (Latency, accuracy, simplicity, robustness, etc.)
   - What constraints are most binding? (Hardware, data, time, integration)

5. **Synthesize Understanding**
   
   Present your understanding before proceeding:

   ```markdown
   ## Reimagination Context
   
   **Problem:** [Brief problem statement]
   
   **Original Approach:** [Algorithm and rationale]
   
   **Key Constraints:**
   - Latency: [target]
   - Memory: [limit]
   - Accuracy: [target metric and value]
   - Hardware: [CPU/GPU, memory]
   
   **Optimization Goals (from review or user):**
   1. [Goal 1, e.g., "Reduce latency by 10x"]
   2. [Goal 2, e.g., "Simplify the approach"]
   3. [Goal 3, e.g., "Improve numerical stability"]
   
   **Questions to explore:**
   - Is there a simpler algorithm that would work?
   - Is there a more efficient algorithm?
   - Is the algorithm family optimal?
   - Can we better balance accuracy vs latency vs simplicity?
   ```

### Phase 2: Algorithm Space Exploration

1. **Consider Algorithm Families**
   
   Systematically explore different approaches:

   **Optimization-based:**
   - Gradient descent, Newton's method, coordinate descent
   - Convex vs non-convex
   - First-order vs second-order methods

   **Search-based:**
   - Brute force, greedy, dynamic programming
   - Tree search (A*, beam search)
   - Heuristic search

   **Learning-based:**
   - Linear models, tree-based models, neural networks
   - Supervised, unsupervised, reinforcement learning
   - Parametric vs non-parametric

   **Data structure-based:**
   - Hash tables, trees (k-d tree, ball tree, R-tree)
   - Graphs, heaps, tries
   - Spatial indexing structures

   **Heuristic-based:**
   - Domain-specific rules
   - Approximation algorithms
   - Randomized algorithms

2. **Evaluate Complexity Trade-offs**
   
   For each viable algorithm family:

   | Algorithm | Time Complexity | Space Complexity | Accuracy | Simplicity |
   |-----------|----------------|------------------|----------|------------|
   | Original  | O(?)           | O(?)             | ?%       | ?/10       |
   | Option A  | O(?)           | O(?)             | ?%       | ?/10       |
   | Option B  | O(?)           | O(?)             | ?%       | ?/10       |

3. **Consider Industry Standards**
   
   - What do practitioners use for similar problems?
   - What algorithms are proven at scale?
   - What libraries are well-maintained and widely used?
   - What approaches are taught in standard ML courses?

4. **Apply Occam's Razor**
   
   - What's the simplest algorithm that meets requirements?
   - Can a closed-form solution replace iterative optimization?
   - Can a linear model replace a neural network?
   - Can a heuristic replace a complex search?

### Phase 3: Optimal Algorithm Selection

1. **Select the Best Approach**
   
   Based on the exploration, choose the optimal algorithm:

   ```markdown
   ## Selected Approach for v2 Plan
   
   **Algorithm:** [Name and brief description]
   
   **Complexity:** O([time]) time, O([space]) space
   
   **Why This Is Optimal:**
   1. [Reason 1 with quantification]
   2. [Reason 2 with quantification]
   3. [Reason 3 with quantification]
   
   **Comparison to Original:**
   - Original: [Algorithm X] with O([complexity])
   - Reimagined: [Algorithm Y] with O([complexity])
   - Improvement: [Quantified benefit, e.g., "50x faster for n=10,000"]
   
   **Trade-offs:**
   - Gained: [Benefits]
   - Gave up: [Costs, if any]
   - Justification: [Why the trade-off is acceptable]
   ```

2. **Verify Against Constraints**
   
   - Does this meet latency targets?
   - Does this fit within memory constraints?
   - Does this achieve accuracy targets?
   - Can this be implemented with available libraries?
   - Is this maintainable in production?

3. **Check Numerical Stability**
   
   - Are there precision loss risks?
   - Could operations overflow/underflow?
   - Are gradients stable (if applicable)?
   - Is matrix conditioning considered (if applicable)?

### Phase 4: Production-Readiness Design

1. **Optimize for Latency**
   
   - Can operations be vectorized? (NumPy, PyTorch)
   - Can operations be parallelized? (Multi-core, GPU)
   - Are there opportunities for precomputation?
   - Can we use more cache-efficient data structures?

2. **Optimize for Memory**
   
   - Can we use in-place operations?
   - Can we stream data instead of loading all at once?
   - Can we use memory-efficient data types?
   - Can we release memory eagerly?

3. **Design for Monitoring**
   
   - What metrics should we track? (Latency, throughput, accuracy, errors)
   - What logging is needed? (Inputs, outputs, intermediate states)
   - How will we detect model drift?
   - How will we debug production issues?

4. **Plan for Graceful Degradation**
   
   - How do we handle invalid inputs?
   - How do we handle resource exhaustion?
   - How do we handle edge cases?
   - What are the failure modes and how do we recover?

### Phase 5: Evaluation Methodology Enhancement

1. **Strengthen Baselines**
   
   - Are baselines strong enough to demonstrate real value?
   - Should we add more baselines? (Simple heuristic, prior work)
   - Are baselines implemented correctly?

2. **Refine Metrics**
   
   - Do metrics align with the actual objective?
   - Should we add secondary metrics?
   - Are metrics computed correctly?
   - Do we need custom metrics for this problem?

3. **Enhance Statistical Rigor**
   
   - Are significance tests appropriate?
   - Should we use confidence intervals?
   - Should we run multiple trials?
   - How do we handle multiple comparisons?

4. **Improve Ablations**
   
   - What components should be ablated?
   - How do we isolate contributions?
   - Are ablations meaningful and interpretable?

### Phase 6: Write the Reimagined Plan

Use the standard plan template with enhancements:

```markdown
# Algorithm Implementation Plan — [Topic] (v2)

**Tags:** [select from taxonomy]

**Version:** 2 (Reimagined)
**Original Plan:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-topic.md`
**Reimagined By:** AI/ML Expert Optimizer
**Reimagination Date:** [Date]

## 0. Reimagination Summary

**Why v2 Was Created:**
[Brief explanation: review feedback, optimization goals, etc.]

**Key Improvements:**
1. [Improvement 1 with quantification]
2. [Improvement 2 with quantification]
3. [Improvement 3 with quantification]

**What Changed:**
- Algorithm: [Original] → [New]
- Complexity: O([original]) → O([new])
- [Other key changes]

---

## 1. Problem Statement
[Same as original, unless problem formulation changed]

## 2. Quantitative Targets
| Metric | Target | Baseline | Notes |
|--------|--------|----------|-------|
| [Primary metric] | [value] | [current] | [context] |
| Latency | [ms] | [current] | [hardware context] |
| Memory | [MB/GB] | [current] | [constraints] |

## 3. Selected Approach (v2)
- **Algorithm:** [Name and brief description]
- **Complexity:** O([time]) time, O([space]) space
- **Rationale:** [Why this approach is optimal given all constraints]
- **Key Trade-offs:** [What we're optimizing for vs. accepting]
- **Improvement over v1:** [Quantified benefit]

## 4. Integration Points
[Same as original, unless interfaces changed]

## 5. Hardware & Runtime Assumptions
[Same as original, unless assumptions changed]

## 6. Out of Scope
[Same as original, plus any new exclusions]

## 7. Implementation Phases

### P0: Baseline & Harness
[Enhanced or optimized version of original P0]

### P1: Prototype
[Enhanced or optimized version of original P1]

### P2: Evaluation
[Enhanced or optimized version of original P2]

### P3: Optimization
[Enhanced or optimized version of original P3]

### P4: Robustness
[Enhanced or optimized version of original P4]

### P5: Packaging
[Enhanced or optimized version of original P5]

## 8. Risks & Mitigations
[Updated risks based on new approach]

## 9. Reproducibility Checklist
[Enhanced reproducibility guarantees]

## 10. References
[Same as original, plus any new references]

---

## 11. Comparison to Original Plan

### Key Differences

**Algorithm Choice:**
- Original: [Algorithm X]
- Reimagined: [Algorithm Y]
- Rationale: [Why Y is better - quantify if possible]

**Complexity:**
- Original: O([original time]) time, O([original space]) space
- Reimagined: O([new time]) time, O([new space]) space
- Impact: [Quantified improvement]

**Evaluation:**
- Original: [Baseline approach]
- Reimagined: [Enhanced baseline approach]
- Rationale: [Why the change improves rigor]

**Production-Readiness:**
- Original: [Gaps or weaknesses]
- Reimagined: [How addressed]
- Impact: [Concrete improvements]

**Numerical Stability:**
- Original: [Approach]
- Reimagined: [Enhanced approach]
- Impact: [Improved robustness]

### Trade-offs

**What we gained:**
- [Benefit 1 with quantification]
- [Benefit 2 with quantification]
- [Benefit 3 with quantification]

**What we gave up (if anything):**
- [Trade-off 1 with justification]
- [Trade-off 2 with justification]

### Why This Is Better

[Concise summary of why the reimagined approach is superior, grounded in the optimization goals and constraints. Should be 2-3 paragraphs maximum, focusing on the most important improvements.]

---

## 12. Implementation Recommendation

**Recommendation:** Proceed with v2 plan for implementation.

**Rationale:** [Why v2 is the better choice for implementation]

**Next Steps:**
1. Review v2 plan with stakeholders (if needed)
2. Proceed to `algo-rpi-implement` with v2 plan
3. Compare v2 results to v1 predictions during P2 evaluation
```

### Phase 7: Validation and Handoff

1. **Verify Plan Quality**
   
   - [ ] All P0-P5 phases are detailed and actionable
   - [ ] Quantitative targets are specific and achievable
   - [ ] Algorithm choice is justified with complexity analysis
   - [ ] Numerical stability is addressed
   - [ ] Reproducibility is comprehensive
   - [ ] Comparison section explains what changed and why
   - [ ] Trade-offs are explicit and justified

2. **Save the v2 Plan**
   
   - Filename: `YYYY-MM-DD-HHMM-plan-algo-<topic>-v2.md`
   - Location: `llm_docs/plans/`
   - Do NOT overwrite the original plan

3. **Update Memory Bank**
   
   - Add design decisions to `llm_docs/memory/activeContext.md`
   - Note the algorithm choice and rationale
   - Record any important trade-offs or constraints

4. **Present Summary**
   
   ```markdown
   ## Reimagined Plan Complete
   
   **v2 Plan Created:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-topic-v2.md`
   
   **Key Improvements:**
   1. [Improvement 1]
   2. [Improvement 2]
   3. [Improvement 3]
   
   **Algorithm Change:** [Original] → [New]
   **Complexity Improvement:** O([original]) → O([new])
   **Expected Benefit:** [Quantified improvement]
   
   **Recommendation:** Proceed to implementation with v2 plan.
   ```

## Quality Guidelines

### Be Specific and Quantitative

**Bad:** "The new algorithm is faster."
**Good:** "The new algorithm reduces time complexity from O(n²) to O(n log n), achieving 50x speedup for n=10,000 (500ms → 10ms)."

### Be Constructive and Respectful

**Bad:** "The original plan was completely wrong."
**Good:** "Building on the original plan's foundation, this v2 optimizes for latency by using a more efficient algorithm."

### Balance Optimization and Pragmatism

- Don't over-engineer for marginal gains
- Do insist on significant improvements (10x, not 10%)
- Consider the cost/benefit of complexity
- Prefer simple, proven solutions over novel, complex ones

### Justify All Changes

Every difference from the original plan must have a clear rationale:
- Why is this better?
- What do we gain?
- What do we give up (if anything)?
- Is the trade-off worth it?

## Example Reimagination Flow

### Input: Original Plan Excerpt
```markdown
## 3. Selected Approach
- **Algorithm:** Brute-force nearest neighbor search
- **Complexity:** O(n²) time, O(n) space
- **Rationale:** Simple and guaranteed to find exact nearest neighbor
```

### Reimagination Process

1. **Identify issue:** O(n²) is too slow for n=10,000 and 50ms latency target
2. **Explore alternatives:** k-d tree, ball tree, LSH, approximate NN
3. **Select optimal:** k-d tree (O(log n) query, exact results, well-established)
4. **Verify:** 10,000 points × log(10,000) ≈ 130,000 ops ≈ 5ms ✓
5. **Write v2 section:**

```markdown
## 3. Selected Approach (v2)
- **Algorithm:** k-d tree nearest neighbor search
- **Complexity:** O(n log n) build time, O(log n) query time, O(n) space
- **Rationale:** Achieves exact nearest neighbor with logarithmic query time, meeting the 50ms latency target for n=10,000 (estimated 5ms per query)
- **Key Trade-offs:** Adds O(n log n) build time, but this is amortized across many queries
- **Improvement over v1:** 100x faster queries (500ms → 5ms for n=10,000)
```

### Output: Comparison Section
```markdown
## 11. Comparison to Original Plan

### Key Differences

**Algorithm Choice:**
- Original: Brute-force linear search
- Reimagined: k-d tree spatial index
- Rationale: Reduces query complexity from O(n) to O(log n), achieving 100x speedup

**Complexity:**
- Original: O(n²) total time for n queries
- Reimagined: O(n log n) build + O(n log n) query = O(n log n) total
- Impact: For n=10,000, reduces total time from 500ms to 5ms per query

### Why This Is Better

The k-d tree approach maintains exact nearest neighbor results while achieving logarithmic query time. This is a well-established algorithm used in production ML systems (scikit-learn, FAISS) and meets the 50ms latency target with significant margin. The one-time O(n log n) build cost is negligible compared to the query savings.
```
