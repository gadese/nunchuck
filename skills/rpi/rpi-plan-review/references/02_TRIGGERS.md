# Triggers

## When to Invoke

This skill should be invoked when:

1. **Explicit Request**: User calls `/rpi-plan-review` with a plan file path
2. **Workflow Integration**: The `/rpi-full` workflow reaches Phase 3 (Plan Review)
3. **Quality Gate**: Before proceeding to implementation, as a quality checkpoint

## Required Inputs

- **Plan File Path**: Path to the implementation plan document (usually in `llm_docs/plans/`)
- The plan must exist and be readable

## Clarification Protocol

If the plan file path is not provided or unclear:
1. Ask: "Which implementation plan should I review? Please provide the file path."
2. If multiple plans exist, list them and ask for selection
3. If the plan file doesn't exist, report the error and ask for correction

If the plan is incomplete or malformed:
1. Report the specific issues found (e.g., missing sections, invalid format)
2. Ask whether to proceed with review anyway or wait for plan completion

## When NOT to Invoke

- Do not invoke if no plan exists yet (use `/rpi-plan` first)
- Do not invoke for research documents (those are inputs to planning, not plans themselves)
- Do not invoke for code files (use code review tools instead)
