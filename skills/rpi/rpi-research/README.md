# RPI-Research Skill

## Purpose

Descriptive codebase research skill for the Research-Plan-Implement workflow. Produces technical documentation about the current system state without proposing changes or improvements.

## When to Use

Use this skill when you need to:
- Understand the current state of a codebase before making changes
- Document existing architecture, patterns, and data flows
- Create a technical map for downstream planning
- Investigate specific components or areas of the system

## Key Features

- **Strictly descriptive**: Documents what exists, not what should exist
- **Clarification-first**: Asks questions before broad or ambiguous research
- **Reference-based**: Uses file paths with line ranges, no code blocks
- **Memory Bank integration**: Reads and updates workspace memory files
- **Contract mismatch detection**: Identifies inconsistencies between components

## Example Invocation

```
/rpi-research

"I need to understand how the image processing pipeline works, specifically 
the preprocessing steps before model inference."
```

The skill will ask clarifying questions about scope and depth, then produce a research document in `llm_docs/research/`.

## Output

- **Location**: `llm_docs/research/YYYY-MM-DD-HHMM-research-<topic>.md`
- **Format**: Markdown with file references only (no code blocks)
- **Sections**: Research question, findings by area, architecture, contract mismatches, assumptions

## Integration with R-P-I Workflow

1. **Research** (this skill) → Produces descriptive documentation
2. **Plan** → Uses research to create implementation plan
3. **Implement** → Executes the plan

## References

See `references/` directory for detailed instructions:
- `00_ROUTER.md` - Routing logic
- `01_SUMMARY.md` - Role and purpose
- `02_TRIGGERS.md` - When to invoke and clarification protocol
- `03_ALWAYS.md` - Mandatory actions
- `04_NEVER.md` - Prohibited actions
- `05_PROCEDURE.md` - Step-by-step research process
- `06_FAILURES.md` - Error handling and recovery
