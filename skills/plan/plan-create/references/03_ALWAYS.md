---
description: Non-negotiable invariants for this skill.
index: []
---

# Always

- Always read references in the order declared by `00_ROUTER.md`.
- Always compile into `.plan/active/` (single active plan model).
- Always keep tasks bounded and written as checkable steps.
- Always leave `Output` and `Handoff` empty in task files (those are for `plan-exec`).
- Always keep all tasks `pending` at creation time. `plan-exec` is responsible for selecting the single `in_progress` task.
