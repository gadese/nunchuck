---
description: What this skill is and is not.
index: []
---

# Summary

Executes the tasks defined by the active plan under `.plan/active/` by performing the real work and recording concrete results.

This skill owns:

- Updating task state during execution
- Writing **Output** and **Handoff** with verifiable results

This skill does not own:

- Defining Work steps (that is `plan-discuss` / `plan-create`)
- Changing plan structure unless the user explicitly requests it
