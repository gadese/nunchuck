---
description: What this skill is and is not.
index: []
---

# Summary

`plan-discuss` is the **idempotent intent-shaping** phase of planning.

It creates/updates a durable plan intent artifact at `.plan/active.yaml` and keeps it schema-valid.

This skill is responsible for:

- clarifying objective, constraints, assumptions
- enumerating success criteria
- stabilizing open questions
- proposing an initial subplan/task structure (titles only)

This skill is not responsible for:

- writing the compiled plan directory (`plan-create` does that)
- executing tasks (`plan-exec` does that)

