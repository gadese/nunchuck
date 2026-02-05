# Router

## Skill Selection Logic

This skill is invoked when:

1. User explicitly calls `/algo-rpi-plan-reimagine`
2. Part of `/algo-rpi-full` workflow (Phase 4: Plan Reimagine)
3. User requests "rewrite the plan from scratch" or "reimagine the algorithm design"
4. After `algo-rpi-plan-review` identifies substantial issues requiring a fresh approach

## Prerequisites

- An algorithm implementation plan exists (original or reviewed version)
- Research document is available (provides problem context)
- User wants a fundamentally different approach or optimized design

## Handoff

**Input:** 
- Original algorithm implementation plan document path
- Research document path (optional but recommended)
- Reviewed plan path (optional, if review was done)

**Output:** 
- New plan document (v2) with optimized algorithm design
- Comparison rationale explaining differences from original

**Next Step:** Typically `algo-rpi-implement` or user review of v2 plan
