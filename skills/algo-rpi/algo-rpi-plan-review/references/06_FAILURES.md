# Failures

## Common Failure Modes and Recovery

### 1. Plan Document Not Found

**Symptom:** Cannot locate the plan document at the specified path

**Diagnosis:**
- Check if the file path is correct
- Verify the file exists in `llm_docs/plans/`
- Confirm the filename follows the pattern `YYYY-MM-DD-HHMM-plan-algo-*.md`

**Recovery:**
1. Ask user to provide the correct plan document path
2. List files in `llm_docs/plans/` to help locate it
3. If no plan exists, recommend running `algo-rpi-plan` first

**Prevention:**
- Always confirm plan file path before starting review
- Use file existence checks before reading

---

### 2. Plan Missing Required Sections

**Symptom:** Plan document lacks P0-P5 phases, quantitative targets, or algorithm selection

**Diagnosis:**
- Plan may be incomplete or from a different workflow
- Plan may not follow the standard Algo-RPI structure

**Recovery:**
1. Identify which sections are missing
2. Note this in the review as a **CRITICAL** issue
3. Recommend regenerating the plan with `algo-rpi-plan`
4. If only minor sections are missing, add them during review

**Prevention:**
- Verify plan structure early in the review process
- Check for required sections before deep analysis

---

### 3. Research Document Not Available

**Symptom:** Plan references a research document that cannot be found

**Diagnosis:**
- Research document path is incorrect
- Research phase was skipped
- Research document was moved or deleted

**Recovery:**
1. Proceed with review based on plan content alone
2. Note the missing research context in the review
3. Flag any algorithm decisions that seem under-justified
4. Recommend providing research document for full context

**Prevention:**
- Check research document availability early
- Don't block review if research is unavailable (plan should be self-contained)

---

### 4. Insufficient Context for Algorithm Evaluation

**Symptom:** Cannot determine if algorithm choice is appropriate due to missing problem constraints

**Diagnosis:**
- Plan lacks clear problem statement
- Quantitative targets are vague or missing
- Hardware constraints not specified

**Recovery:**
1. Note missing context as **IMPORTANT** issues
2. Add placeholders for missing information
3. Recommend clarifying constraints before implementation
4. Make conservative assumptions and document them

**Prevention:**
- Check for complete problem statement early
- Verify quantitative targets are specific (not "fast" but "50ms")

---

### 5. Conflicting Information Between Research and Plan

**Symptom:** Research document recommends one algorithm, but plan selects a different one

**Diagnosis:**
- Planner may have made a justified deviation
- Planner may have misunderstood the research
- Research may have presented multiple options

**Recovery:**
1. Note the discrepancy in the review
2. Evaluate both options objectively
3. If plan's choice is justified, acknowledge it
4. If research's choice is better, recommend reverting with rationale
5. Ask user for clarification if genuinely ambiguous

**Prevention:**
- Always read both research and plan documents
- Look for explicit justification of algorithm choice in plan

---

### 6. Unrealistic Targets That Cannot Be Met

**Symptom:** Quantitative targets are fundamentally impossible with any algorithm

**Diagnosis:**
- Targets may be based on incorrect assumptions
- Hardware constraints may be unrealistic
- Problem may be computationally intractable

**Recovery:**
1. Mark as **CRITICAL** issue
2. Explain why targets are impossible (with complexity analysis)
3. Provide realistic alternative targets with justification
4. Recommend revising requirements with stakeholders

**Example:**
```markdown
---
**EXPERT REVIEW:** Unrealistic Latency Target

**Rationale:** The plan targets 1ms latency for processing 1M data points. Even reading the data from memory takes ~3ms (assuming 3GB/s bandwidth). No algorithm can achieve this target.

**Recommendation:** Revise latency target to 50ms (achievable with optimized O(n) algorithm) or reduce data size to 10K points (achievable in 1ms).

**Severity:** CRITICAL
---
```

**Prevention:**
- Sanity-check targets against fundamental limits (I/O bandwidth, memory access time)
- Compare targets to known benchmarks or prior work

---

### 7. Numerical Stability Issues Not Recognized by Planner

**Symptom:** Plan includes operations that will cause precision loss, overflow, or underflow

**Diagnosis:**
- Planner may lack numerical computing expertise
- Issues may be subtle (e.g., catastrophic cancellation)

**Recovery:**
1. Mark as **IMPORTANT** or **CRITICAL** depending on severity
2. Explain the numerical issue concretely (with example values)
3. Provide specific fix (e.g., log-sum-exp trick, Kahan summation)
4. Add verification to appropriate phase (usually P4 robustness)

**Example:**
```markdown
---
**EXPERT REVIEW:** Numerical Stability Risk

**Rationale:** Computing standard deviation as sqrt(E[X²] - E[X]²) will lose precision when variance is small relative to mean. For X ~ N(1000, 1), this formula gives incorrect results due to catastrophic cancellation.

**Recommendation:** Use Welford's online algorithm or two-pass algorithm: variance = E[(X - mean)²]. Add numerical stability test in P4 with small-variance data.

**Severity:** IMPORTANT
---
```

**Prevention:**
- Always review numerical operations carefully
- Check for common pitfalls (subtraction of similar numbers, exp/log without clipping)

---

### 8. Plan Requires Complete Rewrite

**Symptom:** Multiple critical issues that would require rewriting most of the plan

**Diagnosis:**
- Algorithm choice is fundamentally wrong
- Approach doesn't match problem constraints
- Plan was based on incorrect assumptions

**Recovery:**
1. **Do NOT rewrite the plan yourself** (that's the job of `algo-rpi-plan-reimagine`)
2. Document all critical issues clearly
3. Recommend using `algo-rpi-plan-reimagine` instead of trying to patch
4. Provide high-level guidance on what the reimagined plan should address

**Example:**
```markdown
## Expert Review Summary

**Overall Assessment:** NEEDS COMPLETE REVISION

**Critical Issues:** 5
- Algorithm complexity O(n³) cannot meet latency targets
- Numerical stability issues in core computation
- Evaluation methodology has data leakage
- Reproducibility guarantees insufficient
- Integration interfaces incompatible with existing codebase

**Recommendation:** This plan requires substantial revision. Recommend using `/algo-rpi-plan-reimagine` to create a new plan from scratch, addressing:
1. Use O(n log n) algorithm (e.g., k-d tree) instead of O(n³) brute force
2. Apply log-sum-exp trick for numerical stability
3. Fix train/test split to prevent leakage
4. Add comprehensive seed management
5. Align interfaces with existing codebase (see research doc section 4)
```

**Prevention:**
- Recognize early when issues are too numerous for patching
- Don't waste time on detailed annotations if complete rewrite is needed

---

### 9. Unable to Assess Without Domain Expertise

**Symptom:** Plan involves specialized domain knowledge (e.g., quantum computing, bioinformatics) that you lack

**Diagnosis:**
- Algorithm requires domain-specific expertise
- Evaluation metrics are domain-specific
- You cannot confidently assess correctness

**Recovery:**
1. Be honest about limitations
2. Review what you CAN assess (code structure, reproducibility, general software engineering)
3. Flag domain-specific sections as requiring expert review
4. Recommend consulting a domain expert

**Example:**
```markdown
**[EXPERT NOTE: The quantum circuit optimization in P3 requires quantum computing expertise to fully assess. I've verified the software engineering aspects (reproducibility, testing, integration), but recommend consulting a quantum algorithms expert to validate the circuit design and optimization strategy.]**
```

**Prevention:**
- Recognize domain boundaries early
- Focus on aspects within your expertise (numerical stability, software engineering, ML best practices)

---

### 10. Plan Is Already Excellent

**Symptom:** No significant issues found during review

**Diagnosis:**
- Plan is well-designed and thorough
- Planner has strong expertise
- Research phase was comprehensive

**Recovery:**
1. **This is not a failure!** Acknowledge the quality of the work
2. Provide minor suggestions if any (SUGGESTION severity)
3. Approve the plan for implementation
4. Don't invent issues just to justify the review

**Example:**
```markdown
## Expert Review Summary

**Overall Assessment:** APPROVED

**Critical Issues:** 0
**Important Issues:** 0
**Suggestions:** 2
- Consider adding GPU profiling in P3 to identify optimization opportunities
- P5 could include a deployment checklist for production readiness

**Key Strengths:**
- Algorithm choice is well-justified and appropriate for constraints
- Numerical stability is thoroughly addressed
- Evaluation methodology is rigorous with proper baselines and significance testing
- Reproducibility is comprehensive

**Recommendation:** Proceed to implementation. This is a high-quality plan.
```

**Prevention:**
- Don't feel obligated to find issues if none exist
- Acknowledge good work explicitly

---

## General Recovery Principles

1. **Be transparent:** If you can't assess something, say so clearly
2. **Be constructive:** Always provide a path forward, not just criticism
3. **Be proportional:** Match severity to actual impact (don't over-dramatize)
4. **Be specific:** Vague concerns are useless; quantify and provide examples
5. **Be respectful:** Assume competence; look for genuine issues, not nitpicks

## When to Escalate to User

Escalate to the user when:
- Plan document cannot be found or is corrupted
- Critical issues require stakeholder input (e.g., revising requirements)
- Conflicting information needs clarification
- Domain expertise beyond your capability is required
- Multiple critical issues suggest complete rewrite is needed

## When to Proceed Despite Issues

Proceed with review despite:
- Missing research document (plan should be self-contained)
- Minor formatting inconsistencies
- Sections in different order than expected (as long as content is present)
- Unfamiliar libraries (as long as they're well-established)

Focus on substantive issues, not cosmetic ones.
