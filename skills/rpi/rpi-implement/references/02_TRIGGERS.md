# Triggers

## When to Invoke

Invoke this skill when you need to:
- Execute an approved implementation plan
- Translate design decisions into working code
- Implement changes phase-by-phase with verification
- Resume interrupted implementation work

## Expected Inputs

When invoked with a plan path:
- Path to the plan document in `llm_docs/plans/`
- Optional: Additional context or constraints

When invoked without parameters, respond exactly:

"I'm ready to implement an approved technical plan. Please provide:
- Path to the plan document in `llm_docs/plans/`
- Any additional context or constraints

If the plan or scope is ambiguous, I will ask clarifying questions before proceeding."

Then wait for user input.

## Clarification Protocol

**MANDATORY**: Before beginning implementation, you MUST ask clarifying questions when:
- The plan path is not provided or is ambiguous
- Referenced files in the plan no longer exist or have changed significantly
- Success criteria are unclear or unmeasurable
- Dependencies between phases are ambiguous
- The plan references external systems or APIs you cannot verify

Ask focused questions covering:
1. **Scope confirmation**: Are there any last-minute scope changes or constraints?
2. **Environment**: Any setup steps or dependencies needed before implementation?
3. **Priority**: If time is limited, which phases are highest priority?
4. **Verification**: Any additional verification steps beyond what's in the plan?

**Exception**: If the plan is complete, unambiguous, and you have full context, proceed directly to implementation after confirming you understand the task.
