---
description: Orchestrator skill for the `doctor` skillset. A diagnostic protocol that
auto_execution_mode: 1
---

# doctor

This workflow delegates to the agent skill at `skills/doctor/`.

## Instructions

1. Read the skill manifest: `skills/doctor/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - ONTOLOGY.md
   - PHILOSOPHY.md
   - OPERATING_RULES.md
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/doctor/`
- **References:** `references/`

## Skillset

This is an orchestrator skill with member skills.

- **Members:** doctor-intake, doctor-triage, doctor-exam, doctor-treatment
- **Default Pipeline:** doctor-intake -> doctor-triage -> doctor-exam -> doctor-treatment

To run the full pipeline, invoke this workflow.
To run individual skills, use their specific workflows.


