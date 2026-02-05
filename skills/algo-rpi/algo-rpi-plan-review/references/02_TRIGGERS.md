# Triggers

## When to Invoke This Skill

### Explicit Invocation
- User runs `/algo-rpi-plan-review` command
- User requests "review the algorithm plan"
- User asks for "expert validation" of a plan

### Workflow Integration
- Part of `/algo-rpi-full` workflow (Phase 3: Plan Review)
- Automatically invoked after `algo-rpi-plan` in the full workflow

### Contextual Triggers
- User expresses uncertainty about algorithm choice
- User asks "is this the right approach?"
- User mentions concerns about performance or correctness
- User wants validation before implementation

## When NOT to Invoke

- User wants a completely new plan (use `algo-rpi-plan-reimagine` instead)
- No plan document exists yet (use `algo-rpi-plan` first)
- User is asking about implementation details (that's for `algo-rpi-implement`)
- User wants general algorithm advice without a specific plan

## Prerequisites

Before starting this skill, ensure:

1. **Plan document exists:** Path to a complete algorithm implementation plan
2. **Plan follows structure:** Contains P0-P5 phases, quantitative targets, algorithm selection
3. **Context available:** Research document or problem description is accessible
4. **User intent clear:** Understand what aspect of the plan needs review (or review everything)

## Input Requirements

**Required:**
- Path to algorithm implementation plan document

**Optional but helpful:**
- Path to research document that informed the plan
- Specific concerns to focus on (e.g., "check numerical stability")
- Context about hardware constraints or deployment environment

## Output Expectations

- Modified plan document with expert annotations
- Clear rationale for each change or suggestion
- Identification of any critical issues that block implementation
- Recommendations for algorithm alternatives (if warranted)
