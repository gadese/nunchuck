# RPI-Plan-Review Skill

## Purpose

Staff engineer review skill for the Research-Plan-Implement workflow. Acts as a critical reviewer examining implementation plans for blind spots, edge cases, error handling, and opportunities to apply better practices.

## When to Use

Use this skill when you need to:
- Review an implementation plan before execution
- Identify potential issues or edge cases not covered in the plan
- Validate that the plan follows best practices
- Ensure error handling and edge cases are properly addressed
- Provide constructive feedback on plan quality

## Key Features

- **Critical review**: Examines plans with a staff engineer's eye for detail
- **Blind spot detection**: Identifies missing considerations and edge cases
- **Best practices**: Suggests improvements aligned with coding standards
- **Direct fixes**: Rewrites plan sections to fix issues rather than leaving comments or rejecting them
- **Constructive feedback**: Provides actionable suggestions for improvement

## Example Invocation

```
/rpi-plan-review

"Review the implementation plan at llm_docs/plans/2026-02-05-1311-plan-feature-x.md 
and identify any blind spots or missing considerations"
```

The skill will:
1. Read the plan document thoroughly
2. Identify issues across multiple dimensions (edge cases, error handling, performance, security, maintainability)
3. Directly rewrite plan sections to fix identified issues
4. Present a summary of changes made

## Review Dimensions

The review examines plans across these dimensions:
- **Edge Cases**: Boundary conditions, empty inputs, null values, concurrent access
- **Error Handling**: Exception handling, validation, graceful degradation
- **Performance**: Scalability concerns, inefficient patterns, resource usage
- **Security**: Input validation, authentication, authorization, data exposure
- **Maintainability**: Code clarity, documentation, testability, modularity
- **Dependencies**: Missing dependencies, version conflicts, circular dependencies

## Output

- **Location**: Modifies the original plan file in-place
- **Format**: Clean, improved plan with issues directly fixed (no review markers left behind)
- **Summary**: Brief explanation of key changes made

## Integration with R-P-I Workflow

1. **Research** → Produces descriptive documentation
2. **Plan** → Creates actionable implementation plan
3. **Plan Review** (this skill) → Validates and improves the plan
4. **Plan Reimagine** → Optionally rewrites for optimization
5. **Implement** → Executes the reviewed plan

## References

See `references/` directory for detailed instructions:
- `00_ROUTER.md` - Routing logic
- `01_SUMMARY.md` - Role and purpose
- `02_TRIGGERS.md` - When to invoke
- `03_ALWAYS.md` - Mandatory review checklist
- `04_NEVER.md` - Prohibited actions
- `05_PROCEDURE.md` - Step-by-step review process
- `06_FAILURES.md` - Error handling and recovery
