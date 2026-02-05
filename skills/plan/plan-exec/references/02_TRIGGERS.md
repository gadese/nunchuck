---
description: When to invoke or exit this skill.
index:
  - Invoke when
  - Do not invoke when
  - Exit immediately if
---

# Triggers

## Invoke when

- An active plan exists under `.plan/active/` and the user wants execution.
- There are pending/in-progress tasks that must be completed.

## Do not invoke when

- The user wants to discuss/clarify intent (use `plan-discuss`).
- The user wants to compile a plan (use `plan-create`).

## Exit immediately if

- Focus/Inputs/Work are placeholders and the user does not want to refine them.
