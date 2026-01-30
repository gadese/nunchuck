# NEVER — Prohibitions

## Scope Violations

**YOU MUST NOT:**
- Review the entire codebase unless explicitly requested by the user
- Proceed with review without identifying target files first
- Review files that were not modified or specified
- Assume all files in a directory need review

## Feature Additions

**YOU MUST NOT:**
- Add new features or functionality not in the original plan
- Implement additional capabilities during review
- Extend functionality beyond what was implemented
- Add "improvements" that change behavior

## Architectural Changes

**YOU MUST NOT:**
- Make architectural changes without explicit approval
- Redesign components during review
- Refactor beyond cleanup (unless explicitly requested)
- Change design patterns without user confirmation

## Quality Compromises

**YOU MUST NOT:**
- Skip automated checks (ruff, pytest)
- Approve code with failing tests
- Approve code with linting errors
- Ignore type hint issues
- Leave print statements in production code
- Leave commented-out code
- Leave debug code

## Testing Shortcuts

**YOU MUST NOT:**
- Skip test verification
- Remove tests to make code pass
- Weaken test assertions
- Ignore failing tests
- Skip edge case testing

## Documentation Violations

**YOU MUST NOT:**
- Add unnecessary docstrings to obvious functions
- Add filler comments
- Leave outdated documentation
- Add comments that state the obvious

## Code Style Violations

**YOU MUST NOT:**
- Use `.get()` instead of direct dictionary access (unless default needed)
- Use old-style type hints (`Optional[X]`, `List[X]`)
- Leave hardcoded magic numbers
- Use print statements instead of logging
- Leave inconsistent naming

## Process Violations

**YOU MUST NOT:**
- Proceed to manual review before fixing automated issues
- Skip verification after making fixes
- Forget to update Memory Bank (in R-P-I context)
- Provide incomplete summary reports
- Fix issues without verifying the fix works

## Reporting Violations

**YOU MUST NOT:**
- Just report issues without fixing them
- Provide vague issue descriptions
- Skip categorizing issues
- Omit automated check results from summary
- Fail to state readiness status clearly

## Scope Creep

**YOU MUST NOT:**
- Add performance optimizations not requested
- Add security hardening not requested (unless critical vulnerability)
- Add logging not requested (unless replacing print statements)
- Add error handling beyond what's necessary for robustness
- Refactor unrelated code

## User Interaction

**YOU MUST NOT:**
- Proceed without user input when scope is unclear
- Make assumptions about which files to review
- Ignore user-specified review depth (quick vs deep)
- Skip asking for clarification when needed
