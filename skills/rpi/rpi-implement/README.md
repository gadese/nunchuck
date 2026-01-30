# RPI-Implement Skill

## Purpose

Plan execution skill for the Research-Plan-Implement workflow. Translates approved technical plans into working, tested code through disciplined, phase-by-phase implementation.

## When to Use

Use this skill when you need to:
- Execute an approved implementation plan
- Translate design decisions into working code
- Implement changes with verification at each phase
- Resume interrupted implementation work

## Key Features

- **Disciplined execution**: Follows the plan while adapting to reality
- **Phase-by-phase verification**: Tests each phase before proceeding
- **Progress tracking**: Updates plan checkboxes and reports progress
- **Mismatch detection**: Identifies when codebase differs from plan expectations
- **Resumption support**: Can pick up interrupted work from checkmarks
- **Memory Bank integration**: Reads and updates workspace memory files

## Example Invocation

```
/rpi-implement

"Execute the implementation plan at 
llm_docs/plans/2026-01-15-1430-plan-image-preprocessing.md"
```

The skill will:
1. Read the plan and all referenced files
2. Evaluate any mismatches between plan and reality
3. Implement changes phase-by-phase
4. Verify each phase before proceeding
5. Update plan checkboxes and Memory Bank

## Output

- **Plan updates**: Checkboxes marked complete in plan document
- **Progress reports**: Brief summaries after each phase
- **Code changes**: Implemented via edit tools
- **Verification output**: Pass/fail status of automated checks

## Verification Process

After each phase:
1. Run automated checks (ruff, pytest, type checking)
2. Verify manual success criteria from plan
3. Report results concisely
4. Fix issues before proceeding to next phase

## Integration with R-P-I Workflow

1. **Research** → Produces descriptive documentation
2. **Plan** → Creates actionable implementation plan
3. **Implement** (this skill) → Executes the plan

## References

See `references/` directory for detailed instructions:
- `00_ROUTER.md` - Routing logic
- `01_SUMMARY.md` - Role and purpose
- `02_TRIGGERS.md` - When to invoke and clarification protocol
- `03_ALWAYS.md` - Mandatory actions
- `04_NEVER.md` - Prohibited actions
- `05_PROCEDURE.md` - Step-by-step implementation process
- `06_FAILURES.md` - Error handling and recovery
