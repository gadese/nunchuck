# Triggers

## When to Invoke

This skill should be invoked when:

1. **Explicit Request**: User calls `/rpi-plan-reimagine` with a plan file path
2. **Workflow Integration**: The `/rpi-full` workflow reaches Phase 4 (Plan Reimagine)
3. **Optimization Opportunity**: After plan review reveals opportunities for better approaches
4. **Complexity Concerns**: When the original plan seems overly complex

## Required Inputs

- **Plan File Path**: Path to the implementation plan document (usually in `llm_docs/plans/`)
- **Optional: Research File Path**: Path to the research document (if available)
- The plan must exist and be readable

## Clarification Protocol

If the plan file path is not provided or unclear:
1. Ask: "Which implementation plan should I reimagine? Please provide the file path."
2. If multiple plans exist, list them and ask for selection
3. If the plan file doesn't exist, report the error and ask for correction

If additional context would be helpful:
1. Ask: "Is there a research document I should reference? (optional)"
2. Ask: "Are there specific optimization goals? (e.g., performance, simplicity, robustness)"
3. Proceed with available context if user doesn't provide additional information

## When NOT to Invoke

- Do not invoke if no plan exists yet (use `/rpi-plan` first)
- Do not invoke if the plan is already optimal (no significant improvements possible)
- Do not invoke for trivial changes (use plan review instead)
- Do not invoke if the original approach is fundamentally correct and well-structured
