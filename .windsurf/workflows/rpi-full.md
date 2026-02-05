# rpi-full

This workflow delegates to the agent skill at `skills/rpi/` using the Full Workflow pipeline.

## Skill Root

- **Path:** `skills/rpi/`
- **Manifest:** `SKILL.md`
- **Pipeline:** `.pipelines/04_FULL_WORKFLOW.md`

## Purpose

Complete Research-Plan-Implement cycle with integrated plan review, plan reimagination, code review, and commit message generation. This is the most thorough workflow, suitable for complex tasks requiring high quality and robustness.

## Workflow Phases

1. **Research** → Document current codebase state
2. **Plan** → Create implementation plan
3. **Plan Review** → Staff engineer review for blind spots and best practices
4. **Plan Reimagine** → Rewrite plan from scratch for optimization
5. **Implement** → Execute approved plan
6. **Code Review** → Review code quality
7. **Commit Message** → Generate commit message

## Usage

```
/rpi-full

Task: [describe what you want to build/change]
Files: [relevant files if known]
Constraints: [any requirements or limitations]
```

## When to Use

Use this workflow for:
- Complex features with many edge cases
- Performance-critical implementations
- Security-sensitive changes
- Refactoring with optimization opportunities
- When you want maximum quality and robustness

For simpler tasks, consider using `/rpi` (default workflow) instead.
