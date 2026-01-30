# Failures

## Failure Modes and Recovery

### Ambiguous Problem Statement

**Symptom:** Problem is underspecified, constraints unclear, or data characteristics unknown

**Recovery:**
1. Apply clarification protocol immediately
2. Ask 2-4 focused questions covering objectives, constraints, data, environment, boundaries
3. Wait for user answers before proceeding
4. Do not proceed with research until ambiguities are resolved

### Insufficient Codebase Context

**Symptom:** Cannot find integration points, unclear how algorithm fits into system

**Recovery:**
1. Use parallel codebase scans (search, find, grep) to locate relevant files
2. Read processors, handlers, services, DTOs, schemas
3. Document what you found and what's missing
4. Ask user for specific files or integration points if still unclear

### No Existing Baseline

**Symptom:** Cannot find existing implementation or baseline results

**Recovery:**
1. Document that no baseline exists
2. Propose a trivial baseline (simplest possible solution)
3. Include baseline implementation as part of the research recommendation
4. Note this in the validation plan

### Conflicting Requirements

**Symptom:** Constraints are contradictory (e.g., high accuracy + low latency + minimal memory)

**Recovery:**
1. Document the conflict explicitly
2. Present trade-off options to user
3. Ask which constraint is highest priority
4. Adjust candidate approaches based on priority

### Limited Domain Knowledge

**Symptom:** Unfamiliar with the specific algorithmic domain or techniques

**Recovery:**
1. Research relevant algorithm families from the scope focus list
2. Cite well-known approaches by name (no external links)
3. Focus on classical/established methods over cutting-edge techniques
4. Document assumptions and unknowns clearly
5. Recommend consulting domain experts if needed

### Large or Complex Codebase

**Symptom:** Too many files to analyze, unclear where to focus

**Recovery:**
1. Start with files explicitly mentioned by user
2. Use grep/search to find relevant keywords (algorithm names, data types, metrics)
3. Prioritize integration surfaces: processors, handlers, DTOs
4. Document what you examined and what you skipped
5. Ask user to narrow scope if still overwhelming

### Sensitive Data or Secrets

**Symptom:** Encounter config files, secrets, or large data dumps

**Recovery:**
1. Do not read or echo contents
2. Reference their presence and paths only
3. Skip large data dumps in `**/data/**`, `**/images/**`, etc.
4. Continue research with available non-sensitive materials

## Artifact Validation

Before completing research, verify:
- [ ] Problem is formalized with inputs, outputs, constraints, metrics
- [ ] 3-5 candidate approaches documented with trade-offs
- [ ] Codebase interface analysis includes integration points
- [ ] Validation plan includes dataset splits, metrics, reproducibility
- [ ] Document is in `llm_docs/research/` with correct filename format
- [ ] Memory Bank updated with key findings
- [ ] No code blocks included (only file path references)
- [ ] No external links (papers cited by name only)

## Handoff Checklist

Before handing off to planning phase:
- [ ] Research document created and saved
- [ ] Findings summary presented to user
- [ ] User confirmed understanding of candidate approaches
- [ ] Memory Bank updated
- [ ] Document location confirmed

If any item fails, address it before completing the research phase.
