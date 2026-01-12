---
name: compact
description: >
  Perform explicit, target-aware context compaction with declared loss boundaries
  and epistemic guard rails. Use to intentionally reduce context size while
  preserving decisions, constraints, and authority.
metadata:
  author: Jordan Godau
  version: 0.1.0
  skillset:
    name: compact
    schema_version: 1
    skills:
      - compact-light
      - compact-heavy
      - compact-auto
    shared:
      root: .shared
  keywords:
    - compact
    - context
    - checkpoint
    - doctrine
    - epistemics
---

# Purpose

The compact skillset exists to:

- Reduce context **intentionally**
- Preserve declared invariants
- Prevent silent drift, loss, or accidental reinterpretation

> Compaction is a controlled rewrite, not summarization.

# Member Skills

Each skill represents a **fixed epistemic authority level**:

- **compact-light** — Checkpoint (recoverability > brevity)
- **compact-heavy** — Doctrine (authority > recoverability)
- **compact-auto** — Trusted editor with rules (delegated judgment)

# Key Principle

> Invocation selects authority. Execution enforces it.

No skill accepts a `mode` parameter. Authority is encoded in the skill identity.

# Instructions

1. Refer to `.shared/references/` for shared guard rails and schemas
2. Select the appropriate member skill based on intent
3. Do not attempt to override authority levels
