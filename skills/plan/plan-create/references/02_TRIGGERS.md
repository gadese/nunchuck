---
description: When to invoke or exit this skill.
index:
  - Invoke when
  - Do not invoke when
  - Exit immediately if
---

# Triggers

## Invoke when

- Plan intent has been discussed and stabilized (`plan-discuss`), and you need a compiled plan directory.
- The user requests a plan scaffold with tasks under a single active plan.

## Do not invoke when

- A compiled plan already exists and the user only wants execution (use `plan-exec`).

## Exit immediately if

- `.plan/active.yaml` is not ready (use `plan-discuss` to resolve open questions).
