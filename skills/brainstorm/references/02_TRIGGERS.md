---
description: Activation signals and invocation conditions for the brainstorm skill.
index:
  - Invoke When
  - Do Not Invoke When
  - Exit If
  - Expected Inputs
  - Expected Outputs
---

# Triggers — Brainstorm Skill

## Invoke When

- User wants to explore approaches for a problem before committing to one
- User is unsure which algorithm family or technique to use
- User says "brainstorm" or invokes `/brainstorm`
- User wants to understand trade-offs between multiple approaches
- User is stuck on approach selection and needs structured exploration
- User has a novel problem and wants to survey the solution landscape

## Do Not Invoke When

- User has already chosen an approach and wants implementation — use `rpi-implement` or `algo-rpi-implement`
- User wants codebase research about existing code — use `rpi-research`
- User wants formal algorithm analysis with quantitative targets — use `algo-rpi-research`
- User wants a quick answer to a specific technical question (no exploration needed)
- User wants code review — use `code-review`

## Exit If

- User has converged on a shortlist and wants to move forward
- User explicitly requests to stop brainstorming
- User wants to skip to implementation

## Expected Inputs

- Problem description (required — ask if not provided)
- Constraints (optional — can be gathered during CLARIFY phase)
- Prior work or approaches already considered (optional)
- Specific files or context to read (optional)

## Expected Outputs

- Interactive narrowing conversation (2-7 rounds depending on complexity)
- Formal brainstorm document at `llm_docs/research/YYYY-MM-DD-HHMM-research-brainstorm-<topic>.md`
- Updated Memory Bank (`llm_docs/memory/activeContext.md`)
