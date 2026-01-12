# Example

```markdown
---
name: plan
description: >
  Orchestrator skill for the `plan` skillset. Dispatches to member skills in a safe, predictable order.
metadata:
  author: Jordan Godau
  version: 0.1.0
  skillset:
    name: plan
    schema_version: 1
    skills:
      - plan-create
      - plan-exec
      - plan-status
    shared:
      root: .shared
---

# INSTRUCTIONS

1. Refer to `.pipelines/.INDEX.md`.
```
