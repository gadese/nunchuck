# Triggers

## When to Invoke

Invoke this skill when you need to:
- Create an implementation plan based on research findings
- Design a phased approach for implementing new features or changes
- Transform descriptive documentation into actionable steps
- Define success criteria and risk mitigation strategies

## Expected Inputs

When invoked with parameters:
- Research document path(s) from `llm_docs/research/`
- Task description and constraints
- Optional: Specific files that must be considered

When invoked without parameters, respond exactly:

"I'm ready to create a detailed implementation plan. Please provide:
- Research document path(s) from `llm_docs/research/`
- Task description and constraints
- Any specific files that must be considered

If your request is ambiguous, I will ask clarifying questions before proceeding."

Then wait for user input.

## Clarification Protocol

**MANDATORY**: Before finalizing the plan, you MUST ask clarifying questions when:
- The task requirements are ambiguous or broad
- Multiple design approaches are viable
- Business logic or technical preferences are unclear
- The phasing or granularity needs confirmation

The planning process includes multiple interactive checkpoints:
1. **Understanding verification** - Confirm your interpretation of requirements
2. **Design options** - Present 2-3 viable approaches for user selection
3. **Structure approval** - Get approval on phasing before writing detailed plan

**Exception**: If the research document and task are completely unambiguous, you may proceed more directly, but still confirm the chosen approach.
