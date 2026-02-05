# Router

## Skill Selection Logic

This skill is invoked when:

1. User explicitly calls `/algo-rpi-plan-review`
2. Part of `/algo-rpi-full` workflow (Phase 3: Plan Review)
3. User requests expert review of an algorithm implementation plan

## Prerequisites

- An algorithm implementation plan document exists (typically in `llm_docs/plans/`)
- Plan follows the standard P0-P5 phase structure
- Plan contains quantitative targets and algorithm selection rationale

## Handoff

**Input:** Algorithm implementation plan document path
**Output:** Modified plan with expert review annotations and recommendations
**Next Step:** Typically `algo-rpi-plan-reimagine` or `algo-rpi-implement`
