# Code Review & Cleanup Checklist

Use this comprehensive checklist to systematically review and clean up code.

---

## Automated Checks (Run First)

```bash
# Linting
ruff check .

# Formatting
ruff format --check .

# Type checking (if configured)
mypy [files]

# Tests
pytest [test files]

# Coverage (optional)
pytest --cov=[module] [test files]
```

**Status:**
- [ ] ruff check passes
- [ ] ruff format passes
- [ ] mypy passes (if applicable)
- [ ] pytest passes
- [ ] Coverage meets target (if applicable)

---

## Code Principles Checklist

### Type Hints & Typing
- [ ] All function arguments have type hints
- [ ] All function return values have type hints
- [ ] Class member variables have type declarations at class level
- [ ] Complex return types use NamedTuples (not nested tuples or dicts)
- [ ] Native Python syntax used (`list[str]`, `str | None`)
- [ ] No unnecessary `from __future__ import annotations`

### Code Structure & Design
- [ ] Functions have single responsibility
- [ ] No unnecessary one-line functions
- [ ] No over-engineered classes for simple operations
- [ ] Hardcoded values replaced with named constants
- [ ] Simple return values (not unnecessary dict wrapping)
- [ ] Direct dictionary access used (not `.get()`)
- [ ] Objects used instead of indices where appropriate
- [ ] Classes used instead of dicts for reusable structures
- [ ] In-place modification functions don't return values
- [ ] Each module has single responsibility
- [ ] Composition favored over inheritance

### Performance
- [ ] Vectorized operations used for numerical data
- [ ] No explicit loops where vectorization is possible
- [ ] Appropriate data structures used

### Error Handling
- [ ] Robust error handling implemented
- [ ] Specific exceptions caught (not bare `except:`)
- [ ] Assertions validate assumptions
- [ ] Error messages are descriptive

### Logging
- [ ] Logging module used (not print statements)
- [ ] Appropriate log levels used (DEBUG, INFO, WARNING, ERROR)
- [ ] Log messages are descriptive with context

### Preferred Libraries
- [ ] OpenCV (cv2) used for image processing (not PIL)
- [ ] defaultdict used instead of manual key checking

---

## Code Style Checklist

### Comments
- [ ] Comments are minimal
- [ ] No filler comments (e.g., "# this is where the change happens")
- [ ] No comments stating the obvious
- [ ] No comments repeating what code makes clear
- [ ] Docstrings only for complex logic (not obvious functions)

### Type Hints
- [ ] Type hints everywhere (no exceptions)
- [ ] Native Python syntax used (`list[str]`, `str | None`)
- [ ] All function arguments annotated
- [ ] All return values annotated

### Code Formatting
- [ ] Code formatted with ruff
- [ ] Double quotes used consistently
- [ ] Long strings split appropriately
- [ ] No lines exceeding 100 characters (unless unavoidable)

### Import Organization
- [ ] Imports grouped: stdlib, third-party, local
- [ ] Each group separated by blank line
- [ ] Imports sorted alphabetically within groups
- [ ] Absolute imports used (not relative, except within package)

### Naming Conventions
- [ ] Classes use PascalCase
- [ ] Functions/methods use snake_case
- [ ] Variables use snake_case
- [ ] Constants use UPPER_SNAKE_CASE
- [ ] Private members prefixed with underscore
- [ ] Boolean variables use `is_`, `has_`, `can_` prefixes

### Line Length and Wrapping
- [ ] Lines ≤ 100 characters
- [ ] Long function signatures wrapped (one parameter per line)
- [ ] Long strings split appropriately

---

## Testing Checklist

### Test Coverage
- [ ] Critical paths have tests
- [ ] Edge cases are tested
- [ ] Error conditions are tested
- [ ] Happy path is tested

### Test Quality
- [ ] Tests are clear and focused
- [ ] Test names are descriptive (`test_<functionality>_<scenario>`)
- [ ] Fixtures used appropriately
- [ ] No test code in production files
- [ ] Tests are independent (no interdependencies)

### Test Organization
- [ ] Tests in appropriate directory (unit/integration/e2e)
- [ ] Test files named `test_*.py`
- [ ] Shared fixtures in `conftest.py`

---

## Documentation Checklist

### Code Documentation
- [ ] Docstrings only for complex logic
- [ ] No docstrings for obvious functions
- [ ] API documentation updated (if public API changed)
- [ ] Examples work correctly
- [ ] No outdated documentation

### Project Documentation
- [ ] README updated (if needed)
- [ ] Architecture docs updated (if structure changed)
- [ ] Deployment docs updated (if deployment changed)

---

## Performance Checklist

### General Performance
- [ ] No obvious performance issues
- [ ] Appropriate data structures used
- [ ] No unnecessary loops or operations
- [ ] Caching used where appropriate

### Numerical Performance
- [ ] Vectorized operations used (NumPy, pandas)
- [ ] No explicit loops for vectorizable operations
- [ ] Appropriate numerical precision

---

## Domain-Specific Checklists

### Machine Learning / Deep Learning

#### Reproducibility
- [ ] Random seeds set and documented
- [ ] Dependency versions pinned
- [ ] Hardware configuration documented
- [ ] Dataset version/hash recorded

#### Numerical Stability
- [ ] No NaN or Inf values
- [ ] Numerical stability verified
- [ ] Appropriate precision used

#### Model Implementation
- [ ] Proper batch processing
- [ ] GPU/CPU handling correct
- [ ] Learning rate scheduling implemented (if applicable)
- [ ] Early stopping implemented (if applicable)

#### Evaluation
- [ ] Appropriate metrics used
- [ ] Baseline comparison documented
- [ ] Statistical significance tested (if applicable)

### Data Science / Pandas

#### Data Operations
- [ ] Vectorized pandas/numpy operations used
- [ ] Explicit indexing (loc/iloc) used
- [ ] Categorical dtypes used for low-cardinality columns
- [ ] Method chaining used appropriately

#### Visualizations
- [ ] Plots have proper labels
- [ ] Plots have titles
- [ ] Plots have legends (if needed)
- [ ] Color schemes are accessible

#### Notebooks
- [ ] Clear sections with markdown cells
- [ ] Meaningful cell execution order
- [ ] Explanatory text in markdown cells
- [ ] Code cells are focused and modular

---

## Cleanup Checklist

### Remove Unnecessary Code
- [ ] Debug code removed
- [ ] Print statements removed (use logging)
- [ ] Commented-out code removed
- [ ] Unused imports removed
- [ ] Unused variables removed
- [ ] Dead code paths removed

### Remove Unnecessary Comments
- [ ] Obvious comments removed
- [ ] Filler comments removed
- [ ] Outdated comments removed
- [ ] Only complex logic comments remain

### Simplify Code
- [ ] Duplicate code consolidated
- [ ] Overly complex implementations simplified
- [ ] Complex expressions extracted into named variables
- [ ] Long functions refactored (if truly needed)

### Improve Consistency
- [ ] Consistent naming across codebase
- [ ] Consistent error handling patterns
- [ ] Consistent code structure
- [ ] Aligned with existing patterns

---

## Final Verification

### Automated Checks (Run Again)
- [ ] ruff check passes
- [ ] ruff format passes
- [ ] pytest passes
- [ ] Type checking passes (if applicable)

### Manual Verification
- [ ] Specific functionality verified
- [ ] Edge cases tested manually
- [ ] No regressions introduced
- [ ] Code behaves as expected

---

## Summary Template

```
Code Review & Cleanup Complete ✓

Files reviewed: [list]

Issues found and fixed:
- Code Principles: [N] issues
  - [Specific issue]
  - [Specific issue]
- Code Style: [N] issues
  - [Specific issue]
  - [Specific issue]
- Testing: [N] issues
  - [Specific issue]
- Documentation: [N] issues
  - [Specific issue]
- Performance: [N] issues
  - [Specific issue]

Automated checks:
- [x] ruff check passes
- [x] ruff format passes
- [x] pytest passes

Manual verification:
- [x] [Specific check]
- [x] [Specific check]

Code is clean and ready for use.
```

---

## Notes

- This checklist is comprehensive. Not all items apply to every review.
- Focus on items relevant to the code being reviewed.
- Be thorough but pragmatic - focus on real issues, not nitpicks.
- Always verify code still works after cleanup.
