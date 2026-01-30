# Failures

## Failure Modes and Recovery

### Missing Research Document

**Symptom:** No research document provided or path is invalid

**Recovery:**
1. Request research document path from user
2. Explain that algorithm planning requires research foundation
3. Offer to wait for research completion or help create research document first

### Ambiguous Quantitative Targets

**Symptom:** Metric targets, latency, or memory constraints are vague or missing

**Recovery:**
1. Present what you found in research
2. Ask user to specify explicit numerical targets
3. Provide reasonable defaults based on research if user is uncertain
4. Document assumptions clearly in plan

### Multiple Viable Approaches Without Selection

**Symptom:** Research presents multiple options but user hasn't selected one

**Recovery:**
1. Present refined comparison of top 2-3 options
2. Include pros/cons from research
3. Provide recommendation with clear rationale
4. Wait for explicit user selection before proceeding
5. Do not proceed with planning until approach is confirmed

### Incomplete Research

**Symptom:** Research document lacks codebase interface analysis or candidate approaches

**Recovery:**
1. Document what's missing
2. Ask user if research should be updated first
3. If proceeding anyway, make explicit assumptions
4. Note gaps in "Risks & Unknowns" section of plan

### Conflicting Constraints

**Symptom:** Targets are contradictory (e.g., 99% accuracy + 5ms latency + 100MB memory on CPU)

**Recovery:**
1. Document the conflict explicitly
2. Present trade-off options with quantitative estimates
3. Ask user to prioritize constraints
4. Adjust plan phases to focus on highest priority constraint

### Missing Baseline

**Symptom:** No baseline metrics documented in research

**Recovery:**
1. Make P0 phase focus on establishing baseline
2. Document that baseline is unknown
3. Include baseline establishment as critical P0 deliverable
4. Adjust success criteria for P1/P2 to be relative to P0 baseline

### Unclear Dataset Characteristics

**Symptom:** Dataset size, splits, or characteristics not specified

**Recovery:**
1. Ask user for dataset details
2. Make reasonable assumptions based on problem domain
3. Document assumptions in plan
4. Include dataset analysis as part of P0 phase

### Hardware Environment Mismatch

**Symptom:** Research assumes GPU but only CPU available (or vice versa)

**Recovery:**
1. Present the mismatch explicitly
2. Adjust algorithm selection if needed (e.g., lighter model for CPU)
3. Revise quantitative targets based on available hardware
4. Document hardware assumptions clearly
5. Get user confirmation before proceeding

## Artifact Validation

Before completing plan, verify:
- [ ] Quantitative targets table is complete with explicit numbers
- [ ] All P0-P5 phases have clear objectives and success criteria
- [ ] Integration points reference specific files from research
- [ ] Reproducibility checklist is included
- [ ] Risks and mitigations are documented
- [ ] Document is in `llm_docs/plans/` with correct filename format
- [ ] Memory Bank updated with design decisions
- [ ] No code blocks included (only file path references)

## Handoff Checklist

Before handing off to implementation phase:
- [ ] Plan document created and saved
- [ ] Plan summary presented to user with quantitative targets
- [ ] User confirmed understanding and approved plan structure
- [ ] Memory Bank updated
- [ ] Document location confirmed

If any item fails, address it before completing the planning phase.

## Common Planning Pitfalls

**Avoid:**
- Vague targets like "good accuracy" or "fast enough"
- Skipping reproducibility requirements
- Planning optimization before evaluation (P3 before P2)
- Omitting baseline comparison
- Leaving approach selection ambiguous
- Including implementation details or code in plan
- Using external links instead of local paths
- Forgetting to update Memory Bank

**Ensure:**
- Every metric has a number
- Every phase has measurable success criteria
- Reproducibility is non-negotiable
- Baseline is established before optimization
- Approach is explicitly selected and confirmed
- Plan is actionable without additional clarification
