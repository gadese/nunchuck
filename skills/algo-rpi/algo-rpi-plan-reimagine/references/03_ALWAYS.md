# Always

## Mandatory Requirements

**YOU MUST:**

- **Read all available context completely** — Original plan, research document, reviewed plan (if exists), Memory Bank files

- **Read Memory Bank files** — Check `llm_docs/memory/activeContext.md`, `systemPatterns.md`, and `techContext.md` for relevant context

- **Understand the problem deeply** — Problem statement, constraints, quantitative targets, integration points, hardware assumptions

- **Identify what to optimize** — Based on review feedback or user request, determine the primary optimization goals (latency, accuracy, simplicity, etc.)

- **Consider algorithm alternatives systematically** — Explore different algorithm families, not just variations of the original approach

- **Ask the key question:** "Knowing everything I know now, what's the elegant solution?"

- **Think from first principles** — Don't be constrained by the original plan's approach; consider the problem fresh

- **Optimize for production-readiness** — Latency, memory, monitoring, graceful degradation, maintainability

- **Preserve quantitative targets** — Keep or improve upon the original targets (metrics, latency, memory)

- **Maintain P0-P5 phase structure** — Use the standard algorithm development phases

- **Provide comprehensive rationale** — Explain what changed, why it's better, and what trade-offs were made

- **Create a new plan document** — Save as `YYYY-MM-DD-HHMM-plan-algo-<topic>-v2.md`, don't overwrite the original

- **Compare to original approach** — Include a section explaining differences and improvements

- **Ensure actionability** — The v2 plan must be ready for implementation, not just theoretical

- **Verify numerical stability** — Check that the reimagined approach doesn't introduce new stability issues

- **Validate reproducibility** — Ensure the v2 plan has comprehensive reproducibility guarantees

- **Update Memory Bank** — Add design decisions to `llm_docs/memory/activeContext.md` after completing the reimagined plan

## Optimization Checklist

Apply this checklist when reimagining the plan:

### 1. Algorithm Selection Optimization
- [ ] Have I considered simpler algorithms that might work? (Occam's razor)
- [ ] Have I considered more efficient algorithms? (Better complexity)
- [ ] Is the algorithm family optimal for this problem? (Optimization vs search vs learning)
- [ ] Does the complexity analysis match the performance targets?
- [ ] Are there industry-standard algorithms I should use?

### 2. Efficiency Optimization
- [ ] Can operations be vectorized? (NumPy, PyTorch)
- [ ] Can operations be parallelized? (Multi-core, GPU)
- [ ] Are there redundant computations to eliminate?
- [ ] Can I use more cache-efficient data structures?
- [ ] Are there opportunities for precomputation or memoization?

### 3. ML Best Practices
- [ ] Are train/val/test splits rigorous? (No leakage)
- [ ] Are baselines strong enough? (Not just random)
- [ ] Are metrics aligned with the objective? (Not proxy metrics)
- [ ] Are ablations meaningful? (Isolate contributions)
- [ ] Is statistical testing adequate? (Significance, confidence intervals)
- [ ] Is evaluation representative of production? (Distribution match)

### 4. Production-Readiness
- [ ] Can we meet latency targets under load?
- [ ] Is memory usage within hardware constraints?
- [ ] Are there monitoring and observability hooks?
- [ ] Is graceful degradation handled? (Edge cases, failures)
- [ ] Is the maintenance burden reasonable?
- [ ] Will this scale to production data volumes?

### 5. Numerical Stability
- [ ] Are there precision loss risks? (Catastrophic cancellation)
- [ ] Could operations overflow/underflow? (exp, log)
- [ ] Are gradients stable? (Vanishing, exploding)
- [ ] Is matrix conditioning considered? (Ill-conditioned systems)
- [ ] Are numerical tolerances appropriate?

### 6. Simplicity and Elegance
- [ ] Is this the simplest approach that meets requirements?
- [ ] Are assumptions minimal and reasonable?
- [ ] Is the algorithm principled and well-understood?
- [ ] Would a senior ML engineer approve this design?
- [ ] Can this be explained clearly to stakeholders?

## Reimagination Process

Follow this process systematically:

### Step 1: Absorb All Context
- Read original plan completely
- Read research document completely
- Read reviewed plan if available
- Read Memory Bank files
- Understand problem, constraints, targets

### Step 2: Identify Optimization Opportunities
- What are the main weaknesses of the original plan?
- What feedback did the review provide?
- What are the primary optimization goals? (Latency, accuracy, simplicity, etc.)
- What constraints are most binding? (Hardware, data, time)

### Step 3: Explore Algorithm Space
- What algorithm families could solve this problem? (Optimization, search, learning, heuristic)
- What are the canonical algorithms in each family?
- What are the complexity/accuracy/simplicity trade-offs?
- What do industry practitioners use for similar problems?

### Step 4: Select Optimal Approach
- Which algorithm best balances all constraints?
- Why is this better than the original approach?
- What are the trade-offs? (Be explicit)
- Is this approach proven and well-understood?

### Step 5: Design for Production
- How will we meet latency targets?
- How will we manage memory?
- How will we monitor this in production?
- How will we handle failures gracefully?
- How will we maintain this over time?

### Step 6: Write the Reimagined Plan
- Follow the standard plan template (see 05_PROCEDURE.md)
- Include comprehensive rationale comparing to original
- Ensure all P0-P5 phases are detailed
- Verify quantitative targets are achievable
- Add reproducibility guarantees

### Step 7: Validate and Handoff
- Check that the plan is actionable for implementation
- Verify numerical stability considerations
- Confirm reproducibility is comprehensive
- Update Memory Bank with design decisions
- Present the v2 plan with comparison to original

## Comparison Section Requirements

The reimagined plan MUST include a comparison section:

```markdown
## Comparison to Original Plan

### Key Differences

**Algorithm Choice:**
- Original: [Algorithm X]
- Reimagined: [Algorithm Y]
- Rationale: [Why Y is better - quantify if possible]

**Complexity:**
- Original: O([original time]) time, O([original space]) space
- Reimagined: O([new time]) time, O([new space]) space
- Impact: [Quantified improvement, e.g., "50x faster for n=10,000"]

**Evaluation:**
- Original: [Baseline approach]
- Reimagined: [Enhanced baseline approach]
- Rationale: [Why the change improves rigor]

**Production-Readiness:**
- Original: [Gaps or weaknesses]
- Reimagined: [How addressed]
- Impact: [Concrete improvements]

### Trade-offs

**What we gained:**
- [Benefit 1 with quantification]
- [Benefit 2 with quantification]

**What we gave up (if anything):**
- [Trade-off 1 with justification]
- [Trade-off 2 with justification]

### Why This Is Better

[Concise summary of why the reimagined approach is superior, grounded in the optimization goals and constraints]
```

## Quality Standards

The reimagined plan must meet these standards:

- **Quantitative:** All targets are specific numbers, not vague descriptions
- **Actionable:** Implementer can execute without ambiguity
- **Rigorous:** Evaluation methodology is statistically sound
- **Production-ready:** Considers deployment, monitoring, maintenance
- **Reproducible:** Comprehensive seed management and version pinning
- **Optimal:** Best algorithm choice given all constraints
- **Elegant:** Simplest approach that meets requirements
- **Justified:** Clear rationale for all design decisions
