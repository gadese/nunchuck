---
description: When to invoke or exit this skill.
index:
  - Invoke when
  - Do not invoke when
  - Exit immediately if
---

# Triggers

## Invoke when

- The user wants to plan but intent is not stable yet.
- There are open questions that block a deterministic plan structure.
- You need to negotiate scope and success criteria before execution.

## Do not invoke when

- A compiled plan already exists and the user wants execution (`plan-exec`).
- The user explicitly requests compilation (`plan-create`).

## Exit immediately if

- The user refuses to clarify any intent and still wants execution.

