# Code Review & Cleanup Skill

**Invoke with:** `@code-review-cleanup` or automatically triggered after implementation phases

This skill provides systematic code review and cleanup capabilities to ensure high-quality, maintainable code that follows all established guidelines and best practices.

---

## Purpose

The Code Review & Cleanup skill helps you:
- Review code for adherence to principles and style guidelines
- Identify and fix quality issues
- Clean up unnecessary code and comments
- Ensure type hints are complete and correct
- Verify test coverage and error handling
- Validate documentation appropriateness

---

## When to Use

Use this skill:
- After completing implementation phases
- Before committing code changes
- When reviewing pull requests
- When refactoring existing code
- When cleaning up technical debt
- As the final phase of R-P-I workflows

---

## Review Checklist

Use the comprehensive checklist in `references/cleanup-checklist.md` to systematically review code.

---

## Review Process

### Step 1: Preparation

1. **Identify scope:**
   - Which files were modified?
   - What is the purpose of the changes?
   - Are there related files that should be reviewed?

2. **Read guidelines:**
   - Review code principles guide
   - Review code style guide
   - Review domain-specific guides (ML/DL, data science) if applicable

3. **Gather context:**
   - Read the implementation plan (if available)
   - Understand the feature or change being reviewed
   - Note any specific concerns or areas of focus

### Step 2: Automated Checks

Run automated quality checks first:

```bash
# Linting and formatting
ruff check .
ruff format --check .

# Type checking (if configured)
mypy [files]

# Tests
pytest [test files]

# Coverage (if needed)
pytest --cov=[module] [test files]
```

**Fix all automated issues before proceeding to manual review.**

### Step 3: Manual Code Review

Review code systematically using the checklist:

#### 3.1 Code Principles Review
- [ ] Type hints are complete and correct
- [ ] Classes use proper member type declarations
- [ ] NamedTuples used for complex return types
- [ ] Functions have single responsibility
- [ ] No unnecessary one-line functions or classes
- [ ] Hardcoded values replaced with named constants
- [ ] Direct dictionary access used (not `.get()`)
- [ ] Objects used instead of indices where appropriate
- [ ] Classes used instead of dictionaries for reusable structures
- [ ] In-place modification functions don't return values
- [ ] Vectorized operations used for numerical data
- [ ] Assertions validate assumptions

#### 3.2 Code Style Review
- [ ] Comments are minimal and necessary
- [ ] No filler comments or obvious statements
- [ ] Type hints use native Python syntax (`list[str]`, `str | None`)
- [ ] Code formatted with ruff
- [ ] Double quotes used consistently
- [ ] Long strings split appropriately
- [ ] Imports organized (stdlib, third-party, local)
- [ ] Imports sorted alphabetically within groups
- [ ] Naming conventions followed (PascalCase, snake_case, UPPER_SNAKE_CASE)
- [ ] Line length within limits (100 chars)
- [ ] Function signatures wrapped appropriately

#### 3.3 Error Handling Review
- [ ] Robust error handling implemented
- [ ] Specific exceptions caught (not bare `except:`)
- [ ] Error messages are descriptive
- [ ] Logging used instead of print statements
- [ ] Appropriate log levels used (DEBUG, INFO, WARNING, ERROR)
- [ ] Assertions used to validate assumptions

#### 3.4 Testing Review
- [ ] Critical paths have test coverage
- [ ] Edge cases are tested
- [ ] Tests are clear and focused
- [ ] Test names are descriptive
- [ ] Fixtures used appropriately
- [ ] No test code in production files

#### 3.5 Documentation Review
- [ ] Docstrings only for complex logic (not obvious functions)
- [ ] API documentation updated if needed
- [ ] Examples work correctly
- [ ] README updated if needed
- [ ] No outdated documentation

#### 3.6 Performance Review
- [ ] No obvious performance issues
- [ ] Appropriate data structures used
- [ ] No unnecessary loops or operations
- [ ] Caching used where appropriate
- [ ] Vectorized operations used for numerical code

#### 3.7 Domain-Specific Review (if applicable)

**For ML/DL code:**
- [ ] Random seeds set and documented
- [ ] Dependency versions pinned
- [ ] Reproducibility ensured
- [ ] Numerical stability verified (no NaN/Inf)
- [ ] Proper batch processing implemented
- [ ] GPU/CPU handling correct

**For data science code:**
- [ ] Vectorized pandas/numpy operations used
- [ ] Explicit indexing (loc/iloc) used
- [ ] Categorical dtypes used for low-cardinality columns
- [ ] Visualizations have proper labels and titles
- [ ] Data validation implemented

### Step 4: Cleanup

Based on the review, clean up the code:

#### 4.1 Remove Unnecessary Code
- Remove debug code and print statements
- Remove commented-out code
- Remove unused imports
- Remove unused variables
- Remove dead code paths

#### 4.2 Remove Unnecessary Comments
- Remove comments that state the obvious
- Remove filler comments
- Remove outdated comments
- Keep only comments that explain complex logic or non-obvious decisions

#### 4.3 Simplify Code
- Consolidate duplicate code
- Simplify overly complex implementations
- Extract complex expressions into named variables
- Refactor long functions into smaller ones (if truly needed)

#### 4.4 Improve Consistency
- Ensure consistent naming across the codebase
- Ensure consistent error handling patterns
- Ensure consistent code structure
- Align with existing patterns in the codebase

### Step 5: Final Verification

After cleanup, verify everything still works:

```bash
# Run all checks again
ruff check .
ruff format --check .
pytest

# Verify specific functionality if needed
[manual verification steps]
```

### Step 6: Summary Report

Provide a summary of the review and cleanup:

```
Code Review & Cleanup Complete ✓

Files reviewed: [list]

Issues found and fixed:
- [Category]: [N] issues
  - [Specific issue and fix]
  - [Specific issue and fix]
- [Category]: [N] issues
  - [Specific issue and fix]

Automated checks:
- [x] ruff check passes
- [x] ruff format passes
- [x] pytest passes

Manual verification:
- [x] [Specific check]
- [x] [Specific check]

Code is now clean and ready for use.
```

---

## Common Issues and Fixes

### Issue: Unnecessary Comments
**Example:**
```python
# Get the user's name
name = user.get_name()

# Process the name
processed_name = process(name)
```

**Fix:**
```python
name = user.get_name()
processed_name = process(name)
```

### Issue: Missing Type Hints
**Example:**
```python
def process_data(data):
    return [x * 2 for x in data]
```

**Fix:**
```python
def process_data(data: list[int]) -> list[int]:
    return [x * 2 for x in data]
```

### Issue: Using `.get()` Instead of Direct Access
**Example:**
```python
value = mydict.get(key, default)
```

**Fix:**
```python
try:
    value = mydict[key]
except KeyError:
    value = default
```

### Issue: Print Statements Instead of Logging
**Example:**
```python
print(f"Processing {len(items)} items")
```

**Fix:**
```python
import logging

logger = logging.getLogger(__name__)
logger.info("Processing %d items", len(items))
```

### Issue: Hardcoded Values
**Example:**
```python
for attempt in range(3):
    try_operation()
```

**Fix:**
```python
MAX_RETRIES = 3

for attempt in range(MAX_RETRIES):
    try_operation()
```

---

## Best Practices

1. **Review systematically** - Use the checklist, don't skip steps
2. **Fix automated issues first** - Run ruff and pytest before manual review
3. **Be thorough but pragmatic** - Focus on real issues, not nitpicks
4. **Preserve intent** - Don't change functionality during cleanup
5. **Test after cleanup** - Always verify code still works
6. **Document significant changes** - Note any major refactoring in commit messages

---

## Integration with Workflows

This skill is automatically invoked as Phase 4 (Review & Cleanup) in:
- `/research-plan-implement` workflow
- `/algo-full-cycle` workflow

You can also invoke it manually:
```
@code-review-cleanup
```

Then specify:
- Files to review
- Scope of review (full or focused)
- Any specific concerns or areas of focus

---

## Progressive Disclosure

This skill provides progressive disclosure:
- **Quick review**: Run automated checks only
- **Standard review**: Automated checks + manual checklist
- **Deep review**: Standard review + performance analysis + security review

Choose the appropriate level based on:
- Criticality of the code
- Complexity of the changes
- Time available
- Risk tolerance

---

## References

See `references/cleanup-checklist.md` for the complete, detailed checklist.
