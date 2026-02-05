# RPI-Plan-Reimagine Skill

## Purpose

Staff engineer reimagination skill for the Research-Plan-Implement workflow. Acts as a V2 architect who rewrites implementation plans from scratch, optimizing for robustness, readability, performance, and elegant coding patterns.

## When to Use

Use this skill when you need to:
- Optimize an implementation plan for better patterns and practices
- Rewrite a plan with the benefit of hindsight and full context
- Apply more elegant or efficient solutions
- Simplify overly complex approaches
- Leverage better algorithms or data structures

## Key Features

- **Fresh perspective**: Rewrites plans from scratch rather than incrementally improving
- **Optimization focus**: Prioritizes robustness, readability, performance, and elegance
- **Pattern recognition**: Applies optimal coding patterns (e.g., matrix operations vs loops, recursion where appropriate)
- **Simplification**: Reduces complexity while maintaining functionality
- **Full context**: Leverages all available information (research, code, reviewed plan)

## Example Invocation

```
/rpi-plan-reimagine

"Reimagine the implementation plan at llm_docs/plans/2026-02-05-1311-plan-feature-x.md
with a focus on performance and elegant patterns"
```

The skill will:
1. Read all context (research, original plan, reviewed plan, relevant code)
2. Identify opportunities for optimization and better patterns
3. Write a completely new plan (v2) from scratch
4. Present the new plan with rationale for key changes

## Optimization Dimensions

The reimagination focuses on:
- **Algorithmic Efficiency**: Better algorithms (O(n) vs O(n²), matrix operations vs nested loops)
- **Data Structures**: Optimal data structures for the use case
- **Code Patterns**: Elegant patterns (recursion, functional approaches, declarative code)
- **Simplification**: Reducing complexity and cognitive load
- **Robustness**: More resilient error handling and edge case management
- **Readability**: Clearer, more maintainable code structure

## Output

- **Location**: New file `llm_docs/plans/YYYY-MM-DD-HHMM-plan-<topic>-v2.md`
- **Format**: Complete plan rewritten from scratch
- **Rationale**: Includes explanation of key optimizations and pattern choices

## Integration with R-P-I Workflow

1. **Research** → Produces descriptive documentation
2. **Plan** → Creates actionable implementation plan
3. **Plan Review** → Validates and improves the plan
4. **Plan Reimagine** (this skill) → Rewrites for optimization
5. **Implement** → Executes the optimized plan

## References

See `references/` directory for detailed instructions:
- `00_ROUTER.md` - Routing logic
- `01_SUMMARY.md` - Role and purpose
- `02_TRIGGERS.md` - When to invoke
- `03_ALWAYS.md` - Optimization checklist
- `04_NEVER.md` - Prohibited actions
- `05_PROCEDURE.md` - Step-by-step reimagination process
- `06_FAILURES.md` - Error handling and recovery
