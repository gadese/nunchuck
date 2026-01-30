# RPI-Plan Skill

## Purpose

Technical planning skill for the Research-Plan-Implement workflow. Transforms research findings into actionable, phased implementation plans ready for execution.

## When to Use

Use this skill when you need to:
- Create an implementation plan based on research findings
- Design a phased approach for new features or changes
- Define clear success criteria and risk mitigation
- Transform descriptive documentation into executable steps

## Key Features

- **Interactive planning**: Multiple checkpoints for user confirmation
- **Design options**: Presents 2-3 viable approaches before detailing
- **Phased structure**: Breaks work into incremental, testable phases
- **Measurable criteria**: Includes automated and manual verification steps
- **Risk awareness**: Identifies risks and mitigation strategies
- **Reference-based**: Uses file paths with line ranges, no code blocks

## Example Invocation

```
/rpi-plan

"Create an implementation plan for adding image preprocessing based on the 
research document at llm_docs/research/2026-01-15-1400-research-image-pipeline.md"
```

The skill will:
1. Verify understanding and ask clarifying questions
2. Present design options for user selection
3. Propose plan structure for approval
4. Write detailed plan with phases and success criteria

## Output

- **Location**: `llm_docs/plans/YYYY-MM-DD-HHMM-plan-<topic>.md`
- **Format**: Markdown with file references only (no code blocks)
- **Sections**: Overview, current state, design decision, phases, risks, references

## Interactive Process

The planning process includes three pause points:
1. **Understanding verification** - Confirm interpretation of requirements
2. **Design options** - Present approaches and get user selection
3. **Structure approval** - Confirm phasing before detailed writing

This ensures the plan aligns with user expectations before investing time in details.

## Integration with R-P-I Workflow

1. **Research** → Produces descriptive documentation
2. **Plan** (this skill) → Creates actionable implementation plan
3. **Implement** → Executes the plan

## References

See `references/` directory for detailed instructions:
- `00_ROUTER.md` - Routing logic
- `01_SUMMARY.md` - Role and purpose
- `02_TRIGGERS.md` - When to invoke and clarification protocol
- `03_ALWAYS.md` - Mandatory actions
- `04_NEVER.md` - Prohibited actions
- `05_PROCEDURE.md` - Step-by-step planning process
- `06_FAILURES.md` - Error handling and recovery
