# Triggers

## When to Invoke

Invoke this skill when you need to:
- Understand the current state of a codebase or specific components
- Document existing architecture, patterns, and data flows
- Gather information before planning changes or new features
- Create a technical map for downstream planning agents

## Expected Inputs

- Research question or area of investigation
- Optional: Specific files or directories to focus on
- Optional: Depth level (high-level overview vs detailed analysis)

## Response Format

When invoked without parameters, respond with:

"I'm ready to perform descriptive codebase research as part of the Research-Plan-Implement workflow.

Please provide your research question. If your request is broad or ambiguous, I will ask a few clarifying questions before proceeding to ensure the research document is focused and actionable for downstream planning."

Then wait for the user's research query and apply the clarification protocol.

## Clarification Protocol

**MANDATORY**: Before conducting any research, you MUST ask clarifying questions when:
- The research scope is ambiguous or broad
- Multiple interpretations of the request are possible
- The target area, depth, or boundaries are unclear

Ask 2–4 focused questions covering:
1. **Scope**: Which areas/components should be included or excluded?
2. **Depth**: High-level overview or detailed implementation analysis?
3. **Focus**: Specific patterns, data flows, or contracts to prioritize?
4. **Boundaries**: Any files, directories, or systems explicitly out of scope?

**Exception**: If the user provides a narrowly defined question, proceed directly to research.
