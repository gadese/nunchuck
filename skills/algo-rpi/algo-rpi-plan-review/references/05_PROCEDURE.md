# Procedure

## Review Process

Follow these steps in order to conduct a thorough expert review of the algorithm implementation plan.

### Phase 1: Context Gathering

1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

2. **Locate and Read the Plan Document**
   - Confirm the plan file path (typically `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-*.md`)
   - Read the entire plan document before making any judgments
   - Understand the problem statement, selected approach, and all P0-P5 phases

3. **Read the Research Document (if available)**
   - Locate the research document referenced in the plan
   - Understand the context and rationale behind algorithm selection
   - Note any constraints or requirements from the research phase

4. **Identify Key Context**
   - Problem constraints (input/output, data characteristics)
   - Quantitative targets (metrics, latency, memory)
   - Hardware assumptions (CPU/GPU, memory budget)
   - Integration points (existing codebase interfaces)
   - Selected algorithm and its rationale

### Phase 2: Systematic Review

Apply the expert review checklist from `03_ALWAYS.md` across all six dimensions:

#### 1. Algorithm Selection Review

**Questions to ask:**
- Is this the right algorithm family for the problem?
- Are there simpler algorithms that could achieve similar results?
- Are there more efficient algorithms that weren't considered?
- Does the complexity analysis match the performance targets?

**What to check:**
- Time complexity vs latency targets
- Space complexity vs memory constraints
- Trade-off justification (accuracy vs speed vs memory)
- Comparison to alternative approaches

**Common issues:**
- Using O(n²) algorithm when O(n log n) exists and would meet targets
- Choosing complex ML model when simple heuristic would suffice
- Ignoring well-established algorithms in favor of novel approaches
- Mismatched complexity assumptions (e.g., assuming sparse when data is dense)

**Example fix:** If the plan proposes brute-force O(n²) nearest neighbor search but the latency target is 50ms with n=10,000 points (~500ms expected), rewrite the algorithm selection section to use a k-d tree or ball tree for O(log n) query time instead.

#### 2. Theoretical Soundness Review

**Questions to ask:**
- Are convergence guarantees valid for this problem?
- Is the statistical reasoning correct?
- Are complexity bounds accurate?
- Are assumptions about data distribution reasonable?

**What to check:**
- Convergence proofs or citations for iterative algorithms
- Statistical test validity (assumptions met, sample size adequate)
- Big-O analysis correctness (worst-case, average-case, amortized)
- Data distribution assumptions (IID, stationarity, etc.)

**Common issues:**
- Assuming convergence without checking conditions (e.g., convexity, Lipschitz continuity)
- Using parametric tests on non-normal data
- Incorrect complexity analysis (missing hidden constants, wrong recurrence)
- Unrealistic data assumptions (e.g., assuming uniform distribution for real-world data)

**Example fix:** If the plan assumes gradient descent will converge on a non-convex loss function, rewrite the relevant P1 section to include multiple random initializations and document the non-convexity risk in the approach rationale.

#### 3. Numerical Stability Review

**Questions to ask:**
- Are there precision loss risks?
- Could operations overflow or underflow?
- Are gradients stable?
- Is matrix conditioning considered?

**What to check:**
- Subtraction of similar numbers (catastrophic cancellation)
- Large number ranges (overflow/underflow in exp, log, etc.)
- Gradient flow in deep networks or long sequences
- Matrix inversion or solving ill-conditioned systems
- Accumulation errors in iterative algorithms

**Common issues:**
- Computing variance as E[X²] - E[X]² (precision loss)
- Using exp() without clipping (overflow)
- Deep networks without gradient clipping or normalization
- Inverting nearly singular matrices
- Summing many small numbers without Kahan summation

**Example fix:** If the plan describes a softmax computation using raw exp(logits), rewrite the P1 implementation notes to specify the log-sum-exp trick: `softmax(x) = exp(x - max(x)) / sum(exp(x - max(x)))` to prevent overflow for logits > 88.

#### 4. Practical Deployment Review

**Questions to ask:**
- Are latency targets achievable on target hardware?
- Is memory usage realistic?
- Can this be monitored in production?
- Is maintenance burden reasonable?

**What to check:**
- Latency estimates vs hardware capabilities
- Memory footprint vs available RAM
- Monitoring and observability hooks
- Dependency complexity and maintenance
- Failure mode handling

**Common issues:**
- Unrealistic latency targets (not accounting for I/O, serialization)
- Memory estimates missing model weights, activations, or batch overhead
- No plan for monitoring model drift or performance degradation
- Complex dependency chains that are hard to maintain
- No graceful degradation for edge cases

**Example fix:** If the plan has a 10ms latency target that doesn't account for model loading (~200ms) or preprocessing (~30ms), either update the target to 250ms total or add model caching to the P3 optimization phase directly in the plan.

#### 5. Evaluation Rigor Review

**Questions to ask:**
- Are baselines appropriate?
- Are metrics aligned with the objective?
- Is statistical testing adequate?
- Are ablations meaningful?

**What to check:**
- Baseline quality (random, simple heuristic, prior work)
- Metric choice (does it measure what we care about?)
- Statistical significance testing (p-values, confidence intervals)
- Ablation study design (isolate component contributions)
- Test set integrity (no leakage, representative distribution)

**Common issues:**
- Weak baselines that make results look better than they are
- Proxy metrics that don't correlate with actual objective
- No significance testing (can't distinguish signal from noise)
- Missing ablations (can't attribute performance to specific components)
- Test set contamination (data leakage from train/val)

**Example fix:** If the plan only compares to a random baseline for image classification, add a logistic regression baseline to the P0 phase directly in the plan to establish a stronger reference point.

#### 6. Reproducibility Review

**Questions to ask:**
- Are random seeds fixed everywhere?
- Are dependency versions pinned?
- Are deterministic operations enforced?
- Can results be reproduced from artifacts?

**What to check:**
- Random seed documentation (data splits, initialization, sampling)
- Dependency version pinning (requirements.txt, environment.yml)
- Determinism enforcement (GPU ops, parallel reductions)
- Artifact completeness (configs, seeds, data hashes)
- Hardware documentation (CPU/GPU model, memory)

**Common issues:**
- Missing seeds for data augmentation or dropout
- Unpinned dependency versions (e.g., "numpy>=1.20")
- Non-deterministic GPU operations (cuDNN, scatter/gather)
- Incomplete artifacts (missing config files or data versions)
- No hardware documentation (results vary across GPUs)

**Example fix:** If the reproducibility checklist is missing a data augmentation seed, add it directly to the checklist in the plan (e.g., "Data augmentation seed: 789").

### Phase 3: Direct Modification

1. **Prioritize Issues**
   - Rank identified issues: CRITICAL > IMPORTANT > SUGGESTION
   - Focus on issues that would affect implementation correctness or feasibility

2. **Rewrite Affected Sections**
   - For each issue, directly rewrite the relevant plan section to fix it
   - Do NOT leave review comments, annotations, or markers — no one will read them
   - The plan should read as a clean, improved document after your edits
   - Preserve the overall structure (P0-P5 phases)

3. **Verify Modifications**
   - Ensure the plan reads coherently after all changes
   - Check that quantitative targets are still present and realistic
   - Verify that the plan remains actionable for implementation
   - Confirm no sections were deleted without replacement

### Phase 4: Summary and Handoff

1. **Summarize Changes**
   
   Present a concise summary of the review:

   ```markdown
   ## Expert Review Summary
   
   **Plan Reviewed:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-topic.md`
   
   **Overall Assessment:** [APPROVED | APPROVED WITH CHANGES | NEEDS REVISION]
   
   **Critical Issues:** [count]
   - [Brief description of each critical issue]
   
   **Important Issues:** [count]
   - [Brief description of each important issue]
   
   **Suggestions:** [count]
   - [Brief description of suggestions]
   
   **Key Changes Made:**
   1. [Major change 1 with rationale]
   2. [Major change 2 with rationale]
   3. [etc.]
   
   **Recommendation:** [Proceed to implementation | Proceed to plan-reimagine | Revise and re-review]
   ```

2. **Update the Plan Document**
   - Write the modified plan back to the original file path
   - Ensure the plan reads as a clean, improved document (no leftover review markers)
   - Preserve formatting and structure

3. **Recommend Next Steps**
   - If **APPROVED:** Proceed to `algo-rpi-implement`
   - If **APPROVED WITH CHANGES:** Proceed to `algo-rpi-plan-reimagine` or `algo-rpi-implement` (user choice)
   - If **NEEDS REVISION:** Recommend addressing critical issues before proceeding

## Quality Guidelines

### Be Specific and Quantitative

**Bad:** "This might be slow."
**Good:** "O(n²) complexity will take ~500ms for n=10,000, exceeding the 50ms latency target."

**Bad:** "Consider using a better algorithm."
**Good:** "Replace linear search with k-d tree to reduce query time from O(n) to O(log n), achieving ~5ms latency."

### Be Constructive

**Bad:** "This won't work in production."
**Good:** "The current approach doesn't handle network timeouts. Add retry logic with exponential backoff in P4 robustness phase."

### Balance Rigor and Pragmatism

- Don't demand perfection where "good enough" suffices
- Do insist on correctness for critical components (numerical stability, statistical validity)
- Consider the cost/benefit of suggestions (is the improvement worth the complexity?)

### Respect the Planner's Work

- Assume competence; look for genuine issues
- Acknowledge good decisions explicitly
- Don't rewrite sections just to use different words
- Focus on substantive improvements, not style preferences

### Know When to Suggest Alternatives

**Suggest alternatives when:**
- Complexity doesn't match performance targets (O(n²) vs O(n log n))
- Numerical stability is fundamentally problematic (ill-conditioned operations)
- A simpler algorithm would achieve similar results (Occam's razor)
- Industry-standard approach exists and is clearly superior

**Don't suggest alternatives when:**
- The chosen algorithm is reasonable and meets targets
- Alternatives are marginally better but significantly more complex
- The suggestion is based on personal preference, not objective criteria
- The planner already considered and rejected the alternative (check research doc)

## Example Review Flow

### Input Plan Excerpt
```markdown
## 3. Selected Approach
- **Algorithm:** Bubble sort
- **Complexity:** O(n²) time, O(1) space
- **Rationale:** Simple to implement and understand
```

### Expert Review Process

1. **Check algorithm selection:** Bubble sort is O(n²), but for n=10,000 and 50ms target, this is ~500ms
2. **Consider alternatives:** Quicksort O(n log n) or built-in sort would be ~5ms
3. **Assess severity:** CRITICAL (10x over latency target)
4. **Rewrite the section directly:**

```markdown
## 3. Selected Approach
- **Algorithm:** Timsort (Python built-in `sorted()`)
- **Complexity:** O(n log n) time, O(n) space
- **Rationale:** Achieves 50ms latency target while remaining simple (built-in function). Adaptive algorithm performs well on partially sorted data.
```

### Output Summary (presented in chat, NOT written into the plan)
```markdown
## Expert Review Summary

**Overall Assessment:** APPROVED WITH CHANGES

**Critical Issues Fixed:** 1
- Replaced bubble sort O(n²) with Timsort O(n log n) to meet latency target

**Recommendation:** Proceed to implementation with revised plan.
```
