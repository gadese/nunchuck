---
description: What to do when things go wrong.
index:
  - Missing or invalid plan
  - Placeholder Work
  - Commands not runnable
---

# Failures

## Missing or invalid plan

- Stop and ensure a compiled plan exists at `.plan/active/` (run `plan-create`).

## Placeholder Work

- Stop and switch back to `plan-discuss` / `plan-create` to refine task Focus/Inputs/Work until it is executable.

## Commands not runnable

- Stop and instruct user to install `uv`, then re-run `./scripts/skill.sh validate`.
