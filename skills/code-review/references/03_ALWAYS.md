# ALWAYS — Mandatory Actions

## File Scope (CRITICAL)

**YOU MUST identify target files FIRST before any review:**
- If invoked after implementation: Use files from plan document
- If invoked standalone: Use `git status --porcelain` to identify modified files
- If user specifies files: Use the specified file list
- If no files identified: Ask user for clarification

**YOU MUST NEVER:**
- Review the entire codebase without explicit user request
- Proceed without knowing which files to review
- Assume all files need review

## Automated Checks

**YOU MUST run automated checks on target files:**

```bash
# Linting (on target files only)
ruff check [target_files]

# Formatting (on target files only)
ruff format --check [target_files]

# Type checking (if configured, on target files only)
mypy [target_files]

# Tests (on test files related to target files)
pytest [related_test_files]
```

**YOU MUST fix all automated issues before proceeding to manual review.**

## Coding Standards Reference

**YOU MUST reference `.shared/` coding standards:**
- Read `.shared/code-principles.md` for core principles
- Read `.shared/code-style.md` for style guidelines
- Read `.shared/ml-dl-guide.md` if reviewing ML/DL code
- Read `.shared/data-science-guide.md` if reviewing data science code

Apply these standards during review.

## Issue Fixing

**YOU MUST fix identified issues, not just report them:**
- Use edit tools to make corrections
- Run verification after each fix
- Ensure fixes don't break functionality
- Test after cleanup

## Verification

**YOU MUST verify fixes:**
- Re-run automated checks after fixing issues
- Verify specific functionality still works
- Check for regressions
- Ensure no new issues introduced

## Memory Bank Update

**YOU MUST update Memory Bank (if part of R-P-I workflow):**
- Update `llm_docs/memory/activeContext.md` with review completion status
- Update `llm_docs/memory/progress.md` with reviewed files and findings
- Note any significant quality improvements made

## Recommendations Document

**YOU MUST generate a recommendations document if non-trivial improvements identified:**
- Create `llm_docs/recommendations/YYYY-MM-DD-HHMM-recommendations-code-review.md`
- Include only non-trivial recommendations (not simple cleanup)
- Examples of what to include:
  - Performance optimization opportunities (algorithmic improvements, caching strategies)
  - Architecture improvements (design pattern suggestions, refactoring opportunities)
  - Readability enhancements (complex logic simplification, better abstractions)
  - Overhead reduction (unnecessary computations, redundant operations)
  - Scalability improvements
- Examples of what NOT to include:
  - Simple cleanup (comments, formatting, type hints) — fix these directly
  - Automated check fixes — fix these directly
  - Style violations — fix these directly
- Format: Markdown with clear sections per recommendation
- Each recommendation should include:
  - Current approach and issue
  - Suggested improvement
  - Expected benefit (performance gain, readability, maintainability)
  - Implementation effort estimate

## Summary Report

**YOU MUST provide a clear summary report:**
- List all files reviewed
- Categorize issues found and fixed
- Report automated check results
- Provide quality assessment
- State readiness status
- Note if recommendations document was generated

## Type Hints

**YOU MUST ensure complete type hints:**
- All function arguments have type hints
- All function return values have type hints
- Class member variables have type declarations
- Use native Python syntax (`list[str]`, `str | None`)

## Error Handling

**YOU MUST verify robust error handling:**
- Specific exceptions caught (not bare `except:`)
- Descriptive error messages
- Appropriate logging (not print statements)
- Assertions validate assumptions

## Testing

**YOU MUST verify test coverage:**
- Critical paths have tests
- Edge cases are tested
- Tests are clear and focused
- Test names are descriptive

## Code Cleanup

**YOU MUST remove unnecessary elements:**
- Debug code and print statements
- Commented-out code
- Unused imports
- Unused variables
- Filler comments
- Obvious comments
