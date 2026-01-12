---
description: Orchestrator skill for the `plan` skillset. Manages bounded work units with
auto_execution_mode: 1
---

# plan

This workflow delegates to the agent skill at `skills/plan/`.

## Instructions

1. Read the skill manifest: `skills/plan/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/plan/`
- **References:** `references/`

## Skillset

This is an orchestrator skill with member skills.

- **Members:** plan-create, plan-exec, plan-status, plan-review

To run the full pipeline, invoke this workflow.
To run individual skills, use their specific workflows.


