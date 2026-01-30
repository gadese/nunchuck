# Procedure — Code Review Process

## Step 1: Identify Files to Review

**CRITICAL FIRST STEP:** Determine which files need review.

### Option A: From Implementation Plan
If invoked after R-P-I implementation phase:
1. Read the plan document from `llm_docs/plans/`
2. Identify all files mentioned in implementation phases
3. Note files that were modified or created
4. Include related test files

### Option B: From Git Status
If invoked standalone:
1. Run `git status --porcelain` to identify modified files
2. Filter results:
   - Include: Modified (M), Added (A), Renamed (R) files
   - Exclude: Untracked (??) files that existed before current session
3. Identify related test files for modified code
4. Present list to user for confirmation

### Option C: User Specification
If user provides explicit file list:
1. Use the specified files
2. Verify files exist
3. Identify related test files
4. Confirm scope with user if ambiguous

### Option D: From Implement Context
If `rpi-implement` or `algo-rpi-implement` mentions modified files:
1. Use the files mentioned in implementation context
2. Cross-reference with plan if available
3. Include related test files

### If No Files Identified
Ask user:
```
I'm ready to review code. Please provide:
- Path to the implementation plan in `llm_docs/plans/`, OR
- List of specific files to review, OR
- Confirmation to review all modified files from git status

I will review for quality, adherence to guidelines, and best practices.
```

**DO NOT proceed without clear scope.**

---

## Step 2: Context Gathering

### Read Memory Bank (if R-P-I workflow)
- Read `llm_docs/memory/activeContext.md` for current context
- Read `llm_docs/memory/systemPatterns.md` for existing patterns to verify

### Read Implementation Plan (if available)
- Understand what was supposed to be implemented
- Note the success criteria and scope
- Understand the intent behind changes

### Read Coding Standards
- Read `.shared/code-principles.md` for core principles
- Read `.shared/code-style.md` for style guidelines
- Read `.shared/ml-dl-guide.md` if reviewing ML/DL code
- Read `.shared/data-science-guide.md` if reviewing data science code

---

## Step 3: Automated Checks

Run automated quality checks on **target files only**:

```bash
# Linting (specify target files)
ruff check [target_files]

# Formatting (specify target files)
ruff format --check [target_files]

# Type checking (if configured, specify target files)
mypy [target_files]

# Tests (specify related test files)
pytest [related_test_files]

# Coverage (optional, if needed)
pytest --cov=[module] [related_test_files]
```

### Automated Checks Status
- [ ] ruff check passes
- [ ] ruff format passes
- [ ] mypy passes (if applicable)
- [ ] pytest passes
- [ ] Coverage meets target (if applicable)

**Fix all automated issues before proceeding to manual review.**

---

## Step 4: Manual Code Review

### Quick Review (Automated Only)
If quick review requested:
1. Skip to Step 5 (Cleanup) for automated fixes only
2. Skip manual checklist
3. Proceed to Step 6 (Verification)

### Deep Review (Full Checklist)
If deep review requested or default for R-P-I workflow:

#### 4.1 Code Principles Review

**Type Hints & Typing:**
- [ ] All function arguments have type hints
- [ ] All function return values have type hints
- [ ] Class member variables have type declarations at class level
- [ ] Complex return types use NamedTuples (not nested tuples or dicts)
- [ ] Native Python syntax used (`list[str]`, `str | None`)
- [ ] No unnecessary `from __future__ import annotations`

**Code Structure & Design:**
- [ ] Functions have single responsibility
- [ ] No unnecessary one-line functions
- [ ] No over-engineered classes for simple operations
- [ ] Hardcoded values replaced with named constants
- [ ] Simple return values (not unnecessary dict wrapping)
- [ ] Direct dictionary access used (not `.get()` unless default needed)
- [ ] Objects used instead of indices where appropriate
- [ ] Classes used instead of dicts for reusable structures
- [ ] In-place modification functions don't return values
- [ ] Each module has single responsibility
- [ ] Composition favored over inheritance

**Performance:**
- [ ] Vectorized operations used for numerical data
- [ ] No explicit loops where vectorization is possible
- [ ] Appropriate data structures used

**Error Handling:**
- [ ] Robust error handling implemented
- [ ] Specific exceptions caught (not bare `except:`)
- [ ] Assertions validate assumptions
- [ ] Error messages are descriptive

**Logging:**
- [ ] Logging module used (not print statements)
- [ ] Appropriate log levels used (DEBUG, INFO, WARNING, ERROR)
- [ ] Log messages are descriptive with context

**Preferred Libraries:**
- [ ] OpenCV (cv2) used for image processing (not PIL)
- [ ] defaultdict used instead of manual key checking

#### 4.2 Code Style Review

**Comments:**
- [ ] Comments are minimal
- [ ] No filler comments (e.g., "# this is where the change happens")
- [ ] No comments stating the obvious
- [ ] No comments repeating what code makes clear
- [ ] Docstrings only for complex logic (not obvious functions)

**Type Hints:**
- [ ] Type hints everywhere (no exceptions)
- [ ] Native Python syntax used (`list[str]`, `str | None`)
- [ ] All function arguments annotated
- [ ] All return values annotated

**Code Formatting:**
- [ ] Code formatted with ruff
- [ ] Double quotes used consistently
- [ ] Long strings split appropriately
- [ ] No lines exceeding 100 characters (unless unavoidable)

**Import Organization:**
- [ ] Imports grouped: stdlib, third-party, local
- [ ] Each group separated by blank line
- [ ] Imports sorted alphabetically within groups
- [ ] Absolute imports used (not relative, except within package)

**Naming Conventions:**
- [ ] Classes use PascalCase
- [ ] Functions/methods use snake_case
- [ ] Variables use snake_case
- [ ] Constants use UPPER_SNAKE_CASE
- [ ] Private members prefixed with underscore
- [ ] Boolean variables use `is_`, `has_`, `can_` prefixes

**Line Length and Wrapping:**
- [ ] Lines ≤ 100 characters
- [ ] Long function signatures wrapped (one parameter per line)
- [ ] Long strings split appropriately

#### 4.3 Testing Review

**Test Coverage:**
- [ ] Critical paths have tests
- [ ] Edge cases are tested
- [ ] Error conditions are tested
- [ ] Happy path is tested

**Test Quality:**
- [ ] Tests are clear and focused
- [ ] Test names are descriptive (`test_<functionality>_<scenario>`)
- [ ] Fixtures used appropriately
- [ ] No test code in production files
- [ ] Tests are independent (no interdependencies)

**Test Organization:**
- [ ] Tests in appropriate directory (unit/integration/e2e)
- [ ] Test files named `test_*.py`
- [ ] Shared fixtures in `conftest.py`

#### 4.4 Documentation Review

**Code Documentation:**
- [ ] Docstrings only for complex logic
- [ ] No docstrings for obvious functions
- [ ] API documentation updated (if public API changed)
- [ ] Examples work correctly
- [ ] No outdated documentation

**Project Documentation:**
- [ ] README updated (if needed)
- [ ] Architecture docs updated (if structure changed)
- [ ] Deployment docs updated (if deployment changed)

#### 4.5 Performance Review

**General Performance:**
- [ ] No obvious performance issues
- [ ] Appropriate data structures used
- [ ] No unnecessary loops or operations
- [ ] Caching used where appropriate

**Numerical Performance:**
- [ ] Vectorized operations used (NumPy, pandas)
- [ ] No explicit loops for vectorizable operations
- [ ] Appropriate numerical precision

#### 4.6 Domain-Specific Review (if applicable)

**For ML/DL code:**
- [ ] Random seeds set and documented
- [ ] Dependency versions pinned
- [ ] Hardware configuration documented
- [ ] Dataset version/hash recorded
- [ ] No NaN or Inf values
- [ ] Numerical stability verified
- [ ] Proper batch processing
- [ ] GPU/CPU handling correct
- [ ] Appropriate metrics used
- [ ] Baseline comparison documented

**For data science code:**
- [ ] Vectorized pandas/numpy operations used
- [ ] Explicit indexing (loc/iloc) used
- [ ] Categorical dtypes used for low-cardinality columns
- [ ] Method chaining used appropriately
- [ ] Plots have proper labels, titles, legends
- [ ] Color schemes are accessible

---

## Step 5: Cleanup

Based on the review, clean up the code:

### 5.1 Remove Unnecessary Code
- [ ] Debug code removed
- [ ] Print statements removed (use logging)
- [ ] Commented-out code removed
- [ ] Unused imports removed
- [ ] Unused variables removed
- [ ] Dead code paths removed

### 5.2 Remove Unnecessary Comments
- [ ] Obvious comments removed
- [ ] Filler comments removed
- [ ] Outdated comments removed
- [ ] Only complex logic comments remain

### 5.3 Simplify Code
- [ ] Duplicate code consolidated
- [ ] Overly complex implementations simplified
- [ ] Complex expressions extracted into named variables
- [ ] Long functions refactored (if truly needed)

### 5.4 Improve Consistency
- [ ] Consistent naming across codebase
- [ ] Consistent error handling patterns
- [ ] Consistent code structure
- [ ] Aligned with existing patterns

---

## Step 6: Final Verification

After cleanup, verify everything still works:

```bash
# Run all checks again on target files
ruff check [target_files]
ruff format --check [target_files]
pytest [related_test_files]

# Manual verification (if needed)
[specific functionality tests]
```

### Final Verification Status
- [ ] ruff check passes
- [ ] ruff format passes
- [ ] pytest passes
- [ ] Specific functionality verified
- [ ] No regressions introduced

---

## Step 7: Generate Recommendations Document (if needed)

If non-trivial improvement opportunities were identified during review:

### When to Generate
Generate a recommendations document when you identify:
- **Performance optimizations:** Algorithmic improvements, caching strategies, computational efficiency
- **Architecture improvements:** Better design patterns, refactoring opportunities, structural enhancements
- **Readability enhancements:** Complex logic that could be simplified, better abstractions
- **Overhead reduction:** Unnecessary computations, redundant operations, resource waste
- **Scalability improvements:** Bottlenecks, concurrency opportunities, resource management

### When NOT to Generate
Do NOT include in recommendations (fix these directly instead):
- Simple cleanup: Comments, formatting, unused code
- Automated check fixes: Ruff, pytest, mypy issues
- Style violations: Naming, imports, line length
- Type hints: Missing or incorrect type annotations
- Obvious bugs: These should be fixed immediately

### Document Format

**Location:** `llm_docs/recommendations/YYYY-MM-DD-HHMM-recommendations-code-review.md`

**Template:**
```markdown
# Code Review Recommendations

**Date:** YYYY-MM-DD HH:MM
**Files Reviewed:** [list]
**Review Type:** [Quick/Deep]

## Summary

Brief overview of the recommendations and their potential impact.

## Recommendations

### 1. [Recommendation Title]

**Current Approach:**
[Describe the current implementation and what could be improved]

**Issue:**
[Explain the problem: performance bottleneck, complexity, overhead, etc.]

**Suggested Improvement:**
[Detailed description of the recommended change]

**Expected Benefit:**
- Performance: [e.g., "Reduce time complexity from O(n²) to O(n log n)"]
- Readability: [e.g., "Simplify nested logic, reduce cognitive load"]
- Maintainability: [e.g., "Easier to extend, clearer separation of concerns"]
- Overhead: [e.g., "Eliminate redundant database queries"]

**Implementation Effort:** [Low/Medium/High]

**Priority:** [Low/Medium/High]

**Files Affected:**
- `path/to/file.py:line_range`

---

### 2. [Next Recommendation]

[... repeat structure ...]

## Implementation Notes

[Any additional context, dependencies, or considerations for implementing these recommendations]
```

### Example Recommendations

**Good (include):**
- "Replace nested loops with vectorized NumPy operations for 10x performance gain"
- "Extract complex validation logic into separate validator class for better testability"
- "Implement caching layer to reduce redundant API calls"
- "Refactor 200-line function into smaller, focused functions"

**Bad (fix directly, don't document):**
- "Add type hints to function parameters"
- "Remove commented-out code"
- "Fix ruff formatting issues"
- "Rename variable to follow snake_case convention"

---

## Step 8: Update Memory Bank

If part of R-P-I workflow, update Memory Bank:
- Update `llm_docs/memory/activeContext.md` with review completion status
- Update `llm_docs/memory/progress.md` with:
  - Files reviewed
  - Issues found and fixed
  - Quality improvements made
  - Recommendations document path (if generated)

---

## Step 9: Summary Report

Provide a comprehensive summary:

```
Code Review Complete ✓

Review Type: [Quick / Deep]
Files reviewed: [list with line counts]

Issues found and fixed:
- Code Principles: [N] issues
  - [Specific issue and fix]
  - [Specific issue and fix]
- Code Style: [N] issues
  - [Specific issue and fix]
  - [Specific issue and fix]
- Testing: [N] issues
  - [Specific issue and fix]
- Documentation: [N] issues
  - [Specific issue and fix]
- Performance: [N] issues
  - [Specific issue and fix]

Automated checks:
- [x] ruff check passes
- [x] ruff format passes
- [x] pytest passes ([N] tests)

Manual verification:
- [x] [Specific check]
- [x] [Specific check]

Quality assessment:
- Code principles: [Compliant / Issues fixed]
- Code style: [Compliant / Issues fixed]
- Testing: [Adequate / Needs improvement]
- Documentation: [Appropriate / Updated]

Recommendations:
- [x] Recommendations document generated: llm_docs/recommendations/YYYY-MM-DD-HHMM-recommendations-code-review.md
  OR
- [ ] No non-trivial recommendations identified

Code is clean and ready for [commit/deployment/next phase].
```

---

## Common Issues and Fixes

### Issue: Unnecessary Comments
**Example:**
```python
# Get the user's name
name = user.get_name()
```

**Fix:**
```python
name = user.get_name()
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

**Fix (when default needed):**
```python
value = mydict.get(key, default)  # OK when default is needed
```

**Fix (when no default needed):**
```python
value = mydict[key]  # Direct access when key must exist
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

### Issue: Old-Style Type Hints
**Example:**
```python
from typing import Optional, List

def process(items: Optional[List[str]]) -> List[int]:
    pass
```

**Fix:**
```python
def process(items: list[str] | None) -> list[int]:
    pass
```
