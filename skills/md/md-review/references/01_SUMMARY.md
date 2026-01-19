---
description: What this skill is and is not.
index:
  - What It Does
  - What It Is Not
  - Key Pattern
---

# Summary

The **md-review** skill provides agent-driven quality assessment for markdown documents.

## What It Does

- Runs deterministic lint checks on a markdown file or directory
- Reviews document structure and clarity
- Assesses heading hierarchy and flow
- Identifies confusing or unclear sections
- Provides actionable improvement suggestions

## What It Is Not

- Not for content editing (review only)
- Not for style preferences (objective quality)
- Not a replacement for lint (complements it)

## Key Pattern

**Determinism first.** Always run `./scripts/skill.sh <target>` to produce objective lint findings first; then use those findings during the agent review.
