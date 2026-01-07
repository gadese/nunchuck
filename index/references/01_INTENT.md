# Intent

This skill maintains a discoverable index of all skills in the repository.

## Problem

Skills are only useful if agents can find them. Without an index:

- Agents must traverse the filesystem to discover skills
- Keyword matching against skill descriptions requires reading every SKILL.md
- Skillset membership and pipelines are not surfaced for orchestration
- Passive skill utilization is unreliable

## Solution

Generate a single `INDEX.md` at `.codex/skills/INDEX.md` that contains:

1. **Quick Reference Table** — name → path mapping for direct lookup
2. **Skillset Hierarchy** — orchestrators with member skills and default pipelines
3. **Standalone Skills** — individual skills not part of a skillset
4. **Keyword Index** — reverse lookup from keyword to skill(s)

## When to Regenerate

Run this skill whenever:

- A new skill or skillset is added
- A skill's keywords or description change
- Skillset pipelines are modified
- The index appears stale or incomplete
