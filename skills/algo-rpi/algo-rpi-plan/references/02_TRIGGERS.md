# Triggers

## When to Invoke

Invoke this skill when you:
- Have completed algorithm research and need to create an implementation plan
- Have existing research documentation with candidate approaches
- Want to define quantitative targets and phased implementation
- Need to plan algorithm development with reproducibility requirements

## Invocation Response

When invoked with parameters (research doc paths, problem statement, or file paths):
1. Read Memory Bank files first
2. Read all provided documents and files FULLY before any analysis
3. Proceed directly to the planning process

When invoked without parameters, respond exactly:

"I'm ready to create a detailed algorithm implementation plan. Please provide:
- Research document path(s) from `llm_docs/research/`
- Problem statement and quantitative targets (metrics/latency/memory)
- Hardware constraints (CPU/GPU/TPU, memory limits)
- Any specific files to consider (datasets, baselines, prior scripts)

If your request is ambiguous, I will ask clarifying questions before proceeding."

Then wait for user input.

## Expected Inputs

**Required:**
- Research document path from `llm_docs/research/`

**Recommended:**
- Problem statement with quantitative targets
- Hardware constraints (CPU/GPU/TPU, memory limits)
- Specific files to consider (datasets, baselines)

## Output Format

Plan document in `llm_docs/plans/YYYY-MM-DD-HHMM-plan-algo-<kebab-topic>.md` containing:
- Problem statement with quantitative targets table
- Selected approach from research
- Integration points
- P0-P5 implementation phases with success criteria
- Risks and mitigations
- Reproducibility checklist

## Clarification Protocol

**MANDATORY:** Confirm selected approach from research before planning.

If the research presents multiple viable approaches, present refined options and get user confirmation.

Ask clarifying questions when:
- Quantitative targets are not specified
- Hardware constraints are unclear
- Dataset characteristics are ambiguous
- Multiple approaches from research need selection

**Exception:** If research clearly recommends one approach with all targets specified, proceed directly after confirming understanding.
