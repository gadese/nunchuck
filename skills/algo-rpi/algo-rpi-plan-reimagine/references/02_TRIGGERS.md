# Triggers

## When to Invoke This Skill

### Explicit Invocation
- User runs `/algo-rpi-plan-reimagine` command
- User requests "rewrite the plan from scratch"
- User asks to "reimagine the algorithm design"
- User wants "a fresh perspective on the approach"

### Workflow Integration
- Part of `/algo-rpi-full` workflow (Phase 4: Plan Reimagine)
- Automatically invoked after `algo-rpi-plan-review` in the full workflow

### Contextual Triggers
- Review identified multiple critical issues requiring substantial revision
- User is unsatisfied with the original plan's approach
- User wants to explore alternative algorithm designs
- User asks "is there a better way to do this?"

## When NOT to Invoke

- User wants minor edits to existing plan (use `algo-rpi-plan-review` instead)
- No plan exists yet (use `algo-rpi-plan` first)
- User is asking about implementation details (that's for `algo-rpi-implement`)
- Original plan is already optimal (don't reimagine for the sake of it)

## Prerequisites

Before starting this skill, ensure:

1. **Original plan exists:** Path to an algorithm implementation plan (original or reviewed)
2. **Research available:** Access to the research document that informed the plan
3. **Context understood:** Clear understanding of the problem, constraints, and requirements
4. **Rationale for reimagining:** Know WHY we're reimagining (review feedback, user request, etc.)

## Input Requirements

**Required:**
- Path to original algorithm implementation plan document

**Highly Recommended:**
- Path to research document
- Path to reviewed plan (if review was done)
- Specific areas to optimize (e.g., "focus on latency" or "simplify the approach")

**Optional:**
- Additional constraints or requirements not in the original plan
- Feedback from stakeholders or users

## Output Expectations

- New plan document (v2) with optimized algorithm design
- Comprehensive rationale comparing v2 to original
- Clear explanation of what changed and why
- Preserved structure (P0-P5 phases, quantitative targets)
- Actionable plan ready for implementation
