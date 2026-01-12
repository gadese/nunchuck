---
description: Orchestrator skill for the `refactor` skillset. Dispatches to member skills
auto_execution_mode: 1
---

# refactor

This workflow delegates to the agent skill at `skills/refactor/`.

## Instructions

1. Read the skill manifest: `skills/refactor/SKILL.md`
2. Read all references listed in `metadata.references` in order:
   - OUTPUT_FORMAT.md
   - SEVERITY_LEVELS.md
3. Execute the skill procedure as documented
4. Produce output in the format specified by the skill

## Skill Location

- **Path:** `skills/refactor/`
- **References:** `references/`

## Skillset

This is an orchestrator skill with member skills.

- **Members:** refactor-dictionaries, refactor-import-hygiene, refactor-inline-complexity, refactor-lexical-ontology, refactor-module-stutter, refactor-squatters, refactor-semantic-noise, refactor-structural-duplication
- **Default Pipeline:** refactor-lexical-ontology -> refactor-module-stutter -> refactor-squatters -> refactor-semantic-noise -> refactor-dictionaries -> refactor-inline-complexity -> refactor-import-hygiene -> refactor-structural-duplication

To run the full pipeline, invoke this workflow.
To run individual skills, use their specific workflows.


