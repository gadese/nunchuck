---
description: Diagnoses software failures by combining deterministic evidence gathering
with agent judgment. Models failures as medical cases. Idempotent — run
repeatedly until confident diagnosis, then generate schema-based treatment.
auto_execution_mode: 1
---

# doctor

This workflow delegates to the agent skill at `skills/doctor/`.

## Instructions

1. Read the skill manifest: `skills/{skill_dir}/SKILL.md`
2. Read all references listed in `metadata.references` in order:
3. If scripts are present in `scripts/`, follow any automated steps first
4. Execute the skill procedure as documented
5. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/doctor/`
- **References:** `references/`
- **Scripts:** `scripts/`

