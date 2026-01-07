# Output Format

Each generated workflow follows this template:

```markdown
---
description: <skill description (first line)>
auto_execution_mode: 1
---

# <Skill Name>

This workflow delegates to the agent skill at `.codex/skills/<path>/`.

## Instructions

1. Read the skill manifest: `.codex/skills/<path>/SKILL.md`
2. Read all references listed in `metadata.references` in order
3. If scripts are present, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

**Path:** `.codex/skills/<path>/`
**References:** `references/`
**Scripts:** `scripts/` (if present)

## Quick Reference

<Insert skill signals/keywords here for discoverability>
```

## Naming Convention

Workflow files are named after the skill:

- Skill `refactor-dictionaries` → `.windsurf/workflows/refactor-dictionaries.md`
- Skill `plan-create` → `.windsurf/workflows/plan-create.md`
- Skillset `refactor` → `.windsurf/workflows/refactor.md`

## Skillset Workflows

For skillset orchestrators, the workflow additionally notes:

- Member skills available
- Default pipeline sequence
- How to invoke individual members vs. full pipeline
