# Failures — Error Handling and Recovery

## Automated Check Failures

### Ruff Check Fails
**Symptoms:**
- Linting errors reported
- Code style violations
- Import issues
- Unused variables/imports

**Recovery:**
1. Review ruff error messages carefully
2. Fix each issue using edit tools
3. Re-run `ruff check [target_files]`
4. Repeat until all checks pass
5. Do NOT proceed to manual review until ruff passes

**If stuck:**
- Review specific error message
- Check `.shared/code-style.md` for guidance
- Ask user if error is unclear or seems incorrect

### Ruff Format Fails
**Symptoms:**
- Formatting inconsistencies
- Line length violations
- Quote style issues

**Recovery:**
1. Run `ruff format [target_files]` to auto-fix
2. Verify changes are acceptable
3. Re-run `ruff format --check [target_files]`
4. Should pass after auto-format

**If stuck:**
- Check for lines that cannot be auto-formatted (>100 chars)
- Manually break long lines
- Verify double quotes are used consistently

### Pytest Fails
**Symptoms:**
- Test failures
- Test errors
- Import errors in tests

**Recovery:**
1. Read test failure messages carefully
2. Identify root cause:
   - Code change broke functionality → Fix code
   - Test is outdated → Update test
   - Test is incorrect → Fix test
3. Fix the issue
4. Re-run `pytest [related_test_files]`
5. Repeat until all tests pass

**If stuck:**
- Review implementation plan to understand intent
- Check if test expectations are correct
- Verify test setup and fixtures
- Ask user if test failure is expected or indicates real issue

### Type Check Fails (mypy)
**Symptoms:**
- Type hint errors
- Missing type annotations
- Incompatible types

**Recovery:**
1. Review mypy error messages
2. Add missing type hints
3. Fix incompatible type usage
4. Use native Python syntax (`list[str]`, `str | None`)
5. Re-run `mypy [target_files]`

**If stuck:**
- Check `.shared/code-principles.md` for type hint guidelines
- Verify complex return types use NamedTuples
- Ask user if type hint is unclear

## Manual Review Failures

### Cannot Identify Files to Review
**Symptoms:**
- No plan provided
- No files specified
- Git status shows no changes
- Unclear scope

**Recovery:**
1. Ask user for clarification:
```
I'm ready to review code. Please provide:
- Path to the implementation plan in `llm_docs/plans/`, OR
- List of specific files to review, OR
- Confirmation to review all modified files from git status

I will review for quality, adherence to guidelines, and best practices.
```
2. Wait for user response
3. Do NOT proceed without clear scope

### Files in Plan Don't Exist
**Symptoms:**
- Plan references files that don't exist
- Files were moved or renamed
- Plan is outdated

**Recovery:**
1. Report discrepancy to user:
```
Mismatch: Plan references files that don't exist:
- [file1]: Not found
- [file2]: Not found

Options:
1. Review files that do exist from the plan
2. Use git status to identify actual modified files
3. User provides updated file list

How should I proceed?
```
2. Wait for user decision
3. Proceed based on user choice

### Coding Standards Not Accessible
**Symptoms:**
- `.shared/` symlink broken
- Coding standards files missing
- Cannot read reference files

**Recovery:**
1. Report issue to user:
```
Cannot access coding standards at `.shared/`:
- Symlink may be broken
- Files may be missing

Please verify:
- `skills/coding-standards/references/` exists
- `.shared/` symlink points to correct location

See README.md for instructions to recreate symlink.
```
2. Proceed with review using general best practices
3. Note in summary that coding standards were not available

### Fix Introduces New Issues
**Symptoms:**
- Fixing one issue breaks tests
- Cleanup causes regressions
- Changes have unintended side effects

**Recovery:**
1. Revert the problematic fix
2. Analyze the root cause more carefully
3. Consider alternative fix approach
4. Test fix in isolation before applying
5. If still stuck, report to user:
```
Issue: Fixing [problem] introduces [new problem]

Attempted fix: [description]
New issue: [description]

Options:
1. Accept original issue (if minor)
2. Different fix approach: [suggestion]
3. User guidance needed

How should I proceed?
```

## Scope Issues

### Entire Codebase Review Requested Accidentally
**Symptoms:**
- User says "review everything"
- No specific files mentioned
- Scope seems too broad

**Recovery:**
1. Confirm with user:
```
Confirming scope: Review entire codebase?

This will review all files in the project. This is typically not recommended.

Did you mean:
- Review all modified files from git status?
- Review all files in a specific module/directory?
- Review files from recent implementation?

Please clarify the intended scope.
```
2. Wait for confirmation
3. Proceed only with confirmed scope

### Review Depth Unclear
**Symptoms:**
- Not specified whether quick or deep review
- Unclear criticality of code
- Time constraints unknown

**Recovery:**
1. Ask user:
```
Review depth preference?

Quick Review (faster):
- Automated checks only
- Good for: low-risk changes, time-constrained, routine updates

Deep Review (thorough):
- Automated + full manual checklist
- Good for: critical code, complex changes, production-ready code

Which would you prefer? [Default: Deep for R-P-I, Quick for standalone]
```
2. Proceed with user's choice or default

## Quality Issues

### Too Many Issues Found
**Symptoms:**
- Dozens or hundreds of issues
- Code quality is very poor
- Review would take excessive time

**Recovery:**
1. Report to user:
```
Code Review Status: [N] issues found

Issue breakdown:
- Code Principles: [N] issues
- Code Style: [N] issues
- Testing: [N] issues
- Documentation: [N] issues

This is a significant number of issues. Options:
1. Fix all issues (will take time)
2. Fix critical issues only (specify which)
3. Defer review and improve code quality first

How should I proceed?
```
2. Wait for user decision
3. Proceed based on priority

### Cannot Fix Issue
**Symptoms:**
- Issue is unclear how to fix
- Fix requires architectural change
- Fix requires user decision

**Recovery:**
1. Document the issue clearly
2. Report to user:
```
Issue found but cannot fix automatically:

Issue: [description]
Location: [file:line]
Impact: [why this matters]

Reason cannot fix:
- [requires architectural decision / unclear intent / etc.]

Suggested fix: [if any]

User action needed: [what user should do]
```
3. Continue with other issues
4. Note in summary that some issues require user attention

## Memory Bank Issues

### Cannot Update Memory Bank
**Symptoms:**
- Memory Bank files don't exist
- Cannot write to Memory Bank
- Memory Bank structure unexpected

**Recovery:**
1. Note the issue
2. Complete review without Memory Bank update
3. Report in summary:
```
Note: Could not update Memory Bank
- Files may not exist or may be inaccessible
- Review completed successfully
- Manual Memory Bank update may be needed
```

## Verification Failures

### Tests Pass Locally But Fail in CI
**Symptoms:**
- Local pytest passes
- CI/CD pipeline fails
- Environment differences

**Recovery:**
1. Note in summary:
```
Warning: Tests pass locally but may fail in CI

Possible causes:
- Environment differences
- Missing dependencies in CI
- Platform-specific issues

Recommendation: Verify in CI before merging
```
2. Complete review with local verification only

### Cannot Verify Specific Functionality
**Symptoms:**
- Manual verification step requires running application
- Cannot test without external dependencies
- Verification requires user interaction

**Recovery:**
1. Note in summary:
```
Manual verification incomplete:
- [Specific functionality] could not be verified automatically
- Requires: [what's needed to verify]

Recommendation: User should verify [specific aspect] manually
```
2. Complete review with automated verification only

## Escalation

If you encounter an issue not covered here:
1. Document the issue clearly
2. Report to user with context
3. Suggest possible solutions
4. Wait for user guidance
5. Do NOT proceed blindly or make assumptions
