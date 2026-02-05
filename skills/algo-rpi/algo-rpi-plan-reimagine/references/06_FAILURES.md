# Failures

## Common Failure Modes and Recovery

### 1. Original Plan Not Found

**Symptom:** Cannot locate the original plan document

**Diagnosis:**
- File path is incorrect
- Plan was moved or deleted
- Wrong directory

**Recovery:**
1. Ask user for correct plan document path
2. List files in `llm_docs/plans/` to help locate it
3. If no plan exists, recommend running `algo-rpi-plan` first

**Prevention:**
- Always confirm plan file path before starting
- Use file existence checks

---

### 2. Research Document Not Available

**Symptom:** Cannot find the research document referenced in the plan

**Diagnosis:**
- Research path is incorrect
- Research phase was skipped
- Research document was moved or deleted

**Recovery:**
1. Proceed with reimagination based on plan content alone
2. Note the missing research context
3. Make conservative assumptions about problem constraints
4. Ask user for research document if critical context is missing

**Prevention:**
- Check research document availability early
- Don't block reimagination if research is unavailable (plan should be self-contained)

---

### 3. No Clear Optimization Goals

**Symptom:** Unclear what to optimize for (latency, accuracy, simplicity, etc.)

**Diagnosis:**
- No review feedback available
- User didn't specify optimization goals
- Original plan doesn't have obvious weaknesses

**Recovery:**
1. Ask user: "What should I optimize for in the v2 plan?"
2. If no response, default to: "Optimize for production-readiness (latency, robustness, maintainability)"
3. Proceed with general optimization across all dimensions

**Example:**
```markdown
**Optimization Goals (inferred):**
Since no specific goals were provided, I'm optimizing for:
1. Production-readiness (latency, memory, monitoring)
2. Simplicity (prefer simpler algorithms when possible)
3. Robustness (numerical stability, edge case handling)

Please confirm or adjust these goals before I proceed.
```

**Prevention:**
- Always ask about optimization goals if not clear
- Check review feedback for specific issues to address

---

### 4. Original Plan Is Already Optimal

**Symptom:** No genuine improvements can be made

**Diagnosis:**
- Original algorithm choice is optimal
- Evaluation methodology is rigorous
- Production-readiness is comprehensive
- No significant weaknesses

**Recovery:**
1. **Do NOT create a v2 plan just to justify the exercise**
2. Acknowledge that the original plan is already optimal
3. Provide brief analysis of why no reimagination is needed
4. Recommend proceeding with the original plan

**Example:**
```markdown
## Reimagination Assessment

After thorough analysis of the original plan, I conclude that it is already optimal for the given constraints.

**Strengths of Original Plan:**
- Algorithm choice (k-d tree) is optimal for O(log n) query time
- Complexity analysis is correct and matches performance targets
- Numerical stability is thoroughly addressed
- Evaluation methodology is rigorous with strong baselines
- Production-readiness is comprehensive (monitoring, error handling, etc.)
- Reproducibility guarantees are complete

**No Reimagination Needed:**
The original plan represents the best approach given the constraints. Creating a "v2" plan would introduce unnecessary complexity without genuine improvements.

**Recommendation:** Proceed to implementation with the original plan.
```

**Prevention:**
- Recognize early when the original plan is excellent
- Don't feel obligated to create v2 if no improvements exist

---

### 5. Conflicting Constraints

**Symptom:** Cannot satisfy all constraints simultaneously (e.g., 1ms latency + 99.9% accuracy + 1MB memory)

**Diagnosis:**
- Constraints are fundamentally incompatible
- Trade-offs are necessary
- Original plan may have unrealistic targets

**Recovery:**
1. Identify which constraints are in conflict
2. Analyze the trade-off space
3. Present options to the user with explicit trade-offs
4. Get user input on which constraints to prioritize

**Example:**
```markdown
## Constraint Conflict

The current constraints cannot be satisfied simultaneously:
- Latency target: 1ms
- Accuracy target: 99.9%
- Memory limit: 1MB

**Analysis:**
- Achieving 99.9% accuracy requires a model with ~10MB parameters
- Fitting in 1MB memory requires aggressive quantization, reducing accuracy to ~95%
- Achieving 1ms latency requires approximate algorithms, reducing accuracy to ~97%

**Options:**

**Option A: Prioritize Accuracy**
- Accuracy: 99.9%
- Latency: 10ms (10x over target)
- Memory: 10MB (10x over target)

**Option B: Prioritize Latency**
- Accuracy: 97% (2.9% below target)
- Latency: 1ms (meets target)
- Memory: 5MB (5x over target)

**Option C: Prioritize Memory**
- Accuracy: 95% (4.9% below target)
- Latency: 5ms (5x over target)
- Memory: 1MB (meets target)

**Recommendation:** Please clarify which constraints are most critical.
```

**Prevention:**
- Verify constraints are achievable early
- Check for conflicts before deep optimization

---

### 6. Insufficient Domain Knowledge

**Symptom:** Problem requires specialized domain expertise you lack

**Diagnosis:**
- Algorithm involves domain-specific techniques (e.g., quantum computing, bioinformatics)
- Evaluation metrics are domain-specific
- Cannot confidently assess correctness

**Recovery:**
1. Be honest about limitations
2. Optimize what you CAN assess (software engineering, general ML practices)
3. Flag domain-specific sections as requiring expert review
4. Recommend consulting a domain expert

**Example:**
```markdown
**Domain Expertise Limitation:**

The quantum circuit optimization in this plan requires quantum computing expertise to fully assess. I've optimized the software engineering aspects (reproducibility, testing, integration, numerical stability), but the quantum algorithm design should be reviewed by a quantum computing expert.

**What I've Optimized:**
- Code structure and modularity
- Reproducibility (seeds, versions, determinism)
- Testing and evaluation framework
- Integration with existing codebase

**What Needs Expert Review:**
- Quantum circuit design and gate selection
- Quantum algorithm complexity analysis
- Quantum error correction strategies
```

**Prevention:**
- Recognize domain boundaries early
- Focus on aspects within your expertise

---

### 7. Reimagination Makes Things Worse

**Symptom:** The v2 plan is actually inferior to the original

**Diagnosis:**
- Optimization introduced new problems
- Trade-offs were not worth it
- Complexity increased without sufficient benefit

**Recovery:**
1. **Discard the v2 plan**
2. Acknowledge that the original plan is better
3. Explain what was attempted and why it didn't work
4. Recommend proceeding with the original plan

**Example:**
```markdown
## Reimagination Attempt: Not Recommended

I explored using approximate nearest neighbor (LSH) instead of exact k-d tree to reduce latency further.

**Result:** Not recommended.

**Why:**
- Latency improvement: 5ms → 2ms (2.5x faster)
- Accuracy loss: 100% → 92% (8% degradation)
- Complexity increase: Significant (tuning hash functions, multiple tables)

**Analysis:**
The 2.5x latency improvement doesn't justify the 8% accuracy loss and increased complexity. The original k-d tree approach already meets the 50ms latency target with significant margin (5ms) while maintaining exact results.

**Recommendation:** Proceed with the original plan. The k-d tree approach is optimal for this use case.
```

**Prevention:**
- Validate that optimizations actually improve the overall solution
- Don't optimize for the sake of optimizing

---

### 8. Multiple Viable Alternatives

**Symptom:** Several algorithms are roughly equivalent

**Diagnosis:**
- Multiple algorithms meet all constraints
- Trade-offs are balanced
- No clear winner

**Recovery:**
1. Present the top 2-3 alternatives
2. Explain trade-offs clearly
3. Recommend one based on secondary criteria (simplicity, maintainability, etc.)
4. Let user make final choice if preferences are unclear

**Example:**
```markdown
## Algorithm Selection: Multiple Viable Options

Three algorithms meet all constraints:

**Option A: k-d tree**
- Latency: 5ms
- Accuracy: 100% (exact)
- Complexity: Medium (well-established library)
- Best for: Exact results, moderate dimensions (d<20)

**Option B: Ball tree**
- Latency: 7ms
- Accuracy: 100% (exact)
- Complexity: Medium (well-established library)
- Best for: Exact results, high dimensions (d>20)

**Option C: Approximate NN (FAISS)**
- Latency: 2ms
- Accuracy: 99.5% (approximate)
- Complexity: High (requires tuning)
- Best for: Extreme scale, latency-critical

**Recommendation:** Option A (k-d tree) because:
1. Meets latency target with margin (5ms << 50ms)
2. Provides exact results (no accuracy trade-off)
3. Simple to implement and maintain (scikit-learn)
4. Dimensionality is moderate (d=10)

If you prefer Option B or C, please let me know.
```

**Prevention:**
- Use secondary criteria to break ties (simplicity, maintainability)
- Recommend the most pragmatic option

---

### 9. v2 Plan Diverges Too Much from Original

**Symptom:** The v2 plan is fundamentally different from the original

**Diagnosis:**
- Algorithm family changed (e.g., optimization → learning)
- Problem formulation changed
- Integration interfaces changed

**Recovery:**
1. Verify that the divergence is justified
2. Ensure integration interfaces are still compatible
3. Clearly explain why such a large change is necessary
4. Consider whether this should be a new plan, not a v2

**Example:**
```markdown
## Major Divergence from Original Plan

**Original Approach:** Optimization-based (gradient descent)
**Reimagined Approach:** Learning-based (neural network)

**Why This Large Change:**
The original optimization approach assumes a known objective function, but the research document reveals that the objective is learned from data. This fundamentally changes the problem from optimization to supervised learning.

**Impact:**
- Algorithm family: Optimization → Supervised learning
- Complexity: O(n iterations) → O(n epochs × batch size)
- Evaluation: Convergence metrics → Generalization metrics

**Justification:**
This change aligns the approach with the actual problem. The original plan was based on an incorrect problem formulation.

**Integration:**
The input/output interfaces remain the same, so integration with existing codebase is preserved.
```

**Prevention:**
- Verify problem formulation early
- Ensure large changes are justified by fundamental issues

---

### 10. Unable to Quantify Improvements

**Symptom:** Cannot provide specific numbers for improvements

**Diagnosis:**
- Improvements are qualitative (e.g., "more maintainable")
- Lack of baseline measurements
- Complexity analysis is difficult

**Recovery:**
1. Provide qualitative improvements where quantitative is impossible
2. Use order-of-magnitude estimates where exact numbers aren't available
3. Be honest about uncertainty
4. Focus on improvements that CAN be quantified

**Example:**
```markdown
**Improvement: Enhanced Maintainability**

**Original:** Custom implementation of gradient descent with manual learning rate tuning
**Reimagined:** Use scikit-learn's built-in optimizer with automatic learning rate scheduling

**Quantified Benefits:**
- Code reduction: ~200 lines → ~20 lines (10x less code to maintain)
- Bug risk: Custom code → Well-tested library (estimated 10x fewer bugs)
- Development time: ~2 weeks → ~2 days (estimated 5x faster)

**Qualitative Benefits:**
- Better documentation (scikit-learn docs vs custom docs)
- Community support (Stack Overflow, GitHub issues)
- Future updates (library improvements vs manual maintenance)

**Note:** Maintainability improvements are estimated based on industry experience. Actual benefits may vary.
```

**Prevention:**
- Quantify what you can, estimate what you can't
- Be transparent about uncertainty

---

## General Recovery Principles

1. **Be transparent:** If you can't do something, say so clearly
2. **Be pragmatic:** Don't create v2 if original is already optimal
3. **Be specific:** Quantify improvements whenever possible
4. **Be honest:** Acknowledge limitations and uncertainties
5. **Be respectful:** The original plan may already be excellent

## When to Escalate to User

Escalate when:
- Optimization goals are unclear
- Constraints are conflicting
- Multiple viable alternatives exist with no clear winner
- Domain expertise beyond your capability is required
- Original plan is already optimal (confirm before stopping)

## When to Proceed Despite Issues

Proceed despite:
- Missing research document (use plan as primary source)
- Minor formatting inconsistencies
- Unfamiliar libraries (as long as they're well-established)
- Uncertainty about minor details (make reasonable assumptions)

Focus on substantive improvements, not perfection.
