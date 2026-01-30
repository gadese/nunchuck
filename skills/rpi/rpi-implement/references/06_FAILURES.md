# Failures

## Handling Failures

### When Plan Path is Not Provided
- **Symptom**: No plan document specified
- **Action**: Request the plan path from user
- **Recovery**: Cannot proceed without a plan

### When Plan File Doesn't Exist
- **Symptom**: Specified plan file not found
- **Action**: Verify the path and ask user to confirm
- **Recovery**: Request correct path or create plan first

### When Major Mismatch is Detected
- **Symptom**: Codebase state differs significantly from plan expectations
- **Action**: Apply mismatch protocol from 05_PROCEDURE.md
- **Recovery**: Present options and wait for user decision

### When Tests Fail After Implementation
- **Symptom**: Verification steps fail
- **Action**: Debug the issue before proceeding
- **Recovery**: Fix the problem or ask for help if stuck

### When Success Criteria are Unclear
- **Symptom**: Cannot determine if phase is complete
- **Action**: Ask user for clarification on success criteria
- **Recovery**: Get specific, measurable criteria before proceeding

### When External Dependencies are Missing
- **Symptom**: Required libraries or services not available
- **Action**: Document the missing dependency
- **Recovery**: Ask user about setup steps or environment configuration

### When Implementation Requires Plan Deviation
- **Symptom**: Plan approach doesn't work due to unforeseen issues
- **Action**: Document the issue and propose alternative
- **Recovery**: Get user approval before deviating from plan

### When Memory Bank Files Don't Exist
- **Symptom**: `llm_docs/memory/` files are missing
- **Action**: Proceed with implementation but note the absence
- **Recovery**: Create basic Memory Bank entries after completion

### When Work is Interrupted
- **Symptom**: Implementation stopped mid-phase
- **Action**: Apply resumption protocol from 05_PROCEDURE.md
- **Recovery**: Verify continuity and resume from first unchecked item

## Artifact Validation

Before completing implementation:
- [ ] All phases in plan marked complete
- [ ] All automated checks pass (ruff, pytest, type checking)
- [ ] All manual success criteria verified
- [ ] Plan document updated with completion notes
- [ ] Memory Bank updated with completion status
- [ ] No failing tests or unresolved issues
- [ ] All deviations from plan documented

## Quality Guidelines

- Follow existing codebase patterns and conventions
- Respect workspace rules (code principles, style guides)
- Write code for clarity and maintainability
- Use type hints consistently
- Keep changes minimal and focused
- Prefer `ruff` for formatting
