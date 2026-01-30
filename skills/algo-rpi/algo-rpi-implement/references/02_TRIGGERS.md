# Triggers

## When to Invoke

Invoke this skill when you:
- Have an approved algorithm implementation plan ready to execute
- Need to resume interrupted algorithm implementation work
- Want to implement a specific algorithm plan with quantitative verification
- Are continuing algorithm work from a previous session

## Invocation Response

### If a plan path is provided:
1. Read Memory Bank files first
2. Read the plan document completely
3. Check for existing checkmarks (`- [x]`) to identify completed work
4. Read all files referenced in the plan (code, datasets, baselines)
5. Verify the quantitative targets table is complete
6. Apply the clarification protocol
7. Proceed to implementation if no ambiguities exist

### If no plan path is provided, respond exactly:

"I'm ready to implement an approved algorithm plan. Please provide:
- Path to the plan document in `llm_docs/plans/`
- Confirmation that baseline harness and dataset splits are ready
- Any updates to quantitative targets (metrics/latency/memory)

If the plan or scope is ambiguous, I will ask clarifying questions before proceeding."

Then wait for user input.

## Expected Inputs

**Required:**
- Plan document path from `llm_docs/plans/`

**Optional:**
- Clarification on targets, environment, priorities, or verification steps

## Output Format

- Code changes in source files
- Updated plan with checkboxes marked (`- [x]`)
- Progress reports with quantitative measurements after each phase
- Final summary with metrics table

## Clarification Protocol

**MANDATORY:** Ask clarifying questions when:
- The plan path is not provided or is ambiguous
- Quantitative targets (accuracy, latency, memory) are unclear or missing
- Dataset paths or splits are not specified
- Hardware assumptions differ from available environment
- Baseline results are not established or documented
- Random seeds or reproducibility requirements are unclear

Ask focused questions covering:
1. **Targets confirmation:** Are the metric targets (accuracy/F1/IoU, latency, memory) still current?
2. **Environment:** Is the hardware (CPU/GPU) and environment ready? Any dependencies to install?
3. **Dataset:** Are dataset splits prepared? Is the baseline harness functional?
4. **Priority:** If time is limited, which phases are highest priority?
5. **Reproducibility:** Are random seeds and library versions pinned?

**Exception:** If the plan is complete with all targets, datasets, and baselines specified, proceed directly after confirming understanding.
