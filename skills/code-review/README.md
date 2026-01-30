# Code Review Skill

Systematic code review and cleanup skill for ensuring high-quality, maintainable code.

## Overview

The `code-review` skill provides comprehensive code quality assurance through automated checks and manual review. It reviews ONLY modified or explicitly specified files, never the entire codebase unless explicitly requested.

**Key Features:**
- Scoped file review (modified or specified files only)
- Two review depths: Quick (automated only) or Deep (automated + manual)
- Integration with R-P-I workflows
- Standalone invocation support
- Comprehensive quality checklists
- Automated fix application

## When to Use

### Use Code Review:
- After completing implementation phases
- Before committing code changes
- During pull request reviews
- When refactoring existing code
- When cleaning up technical debt
- As final phase of R-P-I workflows

### Review Depth Selection

**Quick Review** (automated checks only):
- Time-constrained situations
- Low-risk changes
- Small, focused modifications
- Routine updates

**Deep Review** (automated + manual checklist):
- Critical code paths
- Complex implementations
- Algorithm or ML/DL code
- Production-ready code
- Security-sensitive code
- Performance-critical code

## Quick Start

### Standalone Usage

**Review modified files (quick):**
```
/code-review

Quick review of all modified files from git status
```

**Review specific files (deep):**
```
/code-review

Files: src/module.py, src/utils.py
Review depth: deep
```

**Review from plan:**
```
/code-review

Plan: llm_docs/plans/2026-01-15-1420-plan-implementation.md
```

### Integrated Usage (R-P-I Workflow)

Code review is automatically invoked after implementation in R-P-I workflows:
- `/rpi` → research → plan → implement → **code-review** → commit-message
- `/algo-rpi` → research → plan → implement → **code-review** → commit-message

Files to review are identified from the implementation plan.

## File Scope

**CRITICAL:** This skill reviews ONLY:
- Files modified during implementation (from plan or git status)
- Files explicitly specified by the user
- Related test files for modified code

**NEVER** reviews the entire codebase unless explicitly requested.

### File Identification Methods

1. **From Implementation Plan:** Files mentioned in plan phases
2. **From Git Status:** `git status --porcelain` (modified, added, renamed)
3. **From User:** Explicit file list or directory specification
4. **From Implement Context:** Files mentioned by implement skillsets

## Review Process

### Quick Review Process
1. Identify target files
2. Run automated checks (ruff, pytest) on target files only
3. Fix automated issues
4. Verify fixes
5. Provide summary

### Deep Review Process
1. Identify target files
2. Read Memory Bank (if R-P-I workflow)
3. Read implementation plan (if available)
4. Read coding standards from `.shared/`
5. Run automated checks on target files
6. Fix automated issues
7. Manual review using comprehensive checklist:
   - Code principles (type hints, structure, performance)
   - Code style (comments, formatting, naming)
   - Testing (coverage, quality, organization)
   - Documentation (appropriate, up-to-date)
   - Performance (data structures, vectorization)
   - Domain-specific (ML/DL, data science)
8. Cleanup (remove unnecessary code/comments, simplify, improve consistency)
9. Final verification
10. Update Memory Bank (if R-P-I workflow)
11. Provide comprehensive summary

## Coding Standards Reference

This skill references shared coding standards via `.shared/` symlink:

- `code-principles.md` — Core principles (DRY, SOLID, type hints, etc.)
- `code-style.md` — Style guidelines (naming, formatting, imports)
- `ml-dl-guide.md` — ML/DL best practices (reproducibility, numerical stability)
- `data-science-guide.md` — Data science guidelines (vectorization, visualization)

**Original Location:** `skills/coding-standards/references/`

**Symlink:** `skills/code-review/.shared/` → `../coding-standards/references/`

### Recreating the Symlink

If the `.shared/` symlink is broken or deleted, recreate it:

```bash
cd skills/code-review
rm -rf .shared  # Remove if exists
ln -s ../coding-standards/references .shared
```

Verify the symlink:
```bash
ls -la .shared
# Should show: .shared -> ../coding-standards/references
```

## Automated Checks

The skill runs the following automated checks on **target files only**:

```bash
# Linting
ruff check [target_files]

# Formatting
ruff format --check [target_files]

# Type checking (if configured)
mypy [target_files]

# Tests
pytest [related_test_files]

# Coverage (optional)
pytest --cov=[module] [related_test_files]
```

All automated issues must be fixed before proceeding to manual review.

## Manual Review Checklist

The deep review includes comprehensive manual checks:

### Code Principles
- Type hints complete and correct
- Single responsibility functions
- Named constants for hardcoded values
- Direct dictionary access (not `.get()`)
- Vectorized operations for numerical data
- Robust error handling
- Logging instead of print statements

### Code Style
- Minimal, necessary comments only
- Native Python type syntax (`list[str]`, `str | None`)
- Ruff formatting applied
- Proper import organization
- Consistent naming conventions
- Lines ≤ 100 characters

### Testing
- Critical paths tested
- Edge cases covered
- Clear, focused tests
- Descriptive test names

### Documentation
- Docstrings only for complex logic
- No docstrings for obvious functions
- API docs updated if needed

### Performance
- Appropriate data structures
- No unnecessary loops
- Vectorization where applicable

### Domain-Specific (if applicable)
- **ML/DL:** Seeds set, versions pinned, reproducibility ensured
- **Data Science:** Vectorized operations, explicit indexing, proper visualizations

## Common Issues Fixed

### Unnecessary Comments
```python
# Before
# Get the user's name
name = user.get_name()

# After
name = user.get_name()
```

### Missing Type Hints
```python
# Before
def process_data(data):
    return [x * 2 for x in data]

# After
def process_data(data: list[int]) -> list[int]:
    return [x * 2 for x in data]
```

### Print Statements
```python
# Before
print(f"Processing {len(items)} items")

# After
import logging
logger = logging.getLogger(__name__)
logger.info("Processing %d items", len(items))
```

### Hardcoded Values
```python
# Before
for attempt in range(3):
    try_operation()

# After
MAX_RETRIES = 3
for attempt in range(MAX_RETRIES):
    try_operation()
```

### Old-Style Type Hints
```python
# Before
from typing import Optional, List
def process(items: Optional[List[str]]) -> List[int]:
    pass

# After
def process(items: list[str] | None) -> list[int]:
    pass
```

## Recommendations Document

When non-trivial improvement opportunities are identified, the skill generates a recommendations document:

**Location:** `llm_docs/recommendations/YYYY-MM-DD-HHMM-recommendations-code-review.md`

### What Gets Documented

**Include (non-trivial improvements):**
- Performance optimizations (algorithmic improvements, caching strategies)
- Architecture improvements (design patterns, refactoring opportunities)
- Readability enhancements (complex logic simplification, better abstractions)
- Overhead reduction (unnecessary computations, redundant operations)
- Scalability improvements (bottlenecks, concurrency opportunities)

**Exclude (fix directly instead):**
- Simple cleanup (comments, formatting, unused code)
- Automated check fixes (ruff, pytest, mypy issues)
- Style violations (naming, imports, line length)
- Type hints (missing or incorrect annotations)
- Obvious bugs (fix immediately)

### Document Structure

Each recommendation includes:
- Current approach and issue
- Suggested improvement
- Expected benefit (performance, readability, maintainability)
- Implementation effort estimate (Low/Medium/High)
- Priority (Low/Medium/High)
- Files affected

## Output Summary

After review, the skill provides a comprehensive summary:

```
Code Review Complete ✓

Review Type: [Quick / Deep]
Files reviewed: [list with line counts]

Issues found and fixed:
- Code Principles: [N] issues
  - [Specific issue and fix]
- Code Style: [N] issues
  - [Specific issue and fix]
- Testing: [N] issues
  - [Specific issue and fix]
- Documentation: [N] issues
  - [Specific issue and fix]

Automated checks:
- [x] ruff check passes
- [x] ruff format passes
- [x] pytest passes ([N] tests)

Manual verification:
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

## Integration with Other Skills

### After Implementation
```
/rpi-implement → /code-review → /commit-message
/algo-rpi-implement → /code-review → /commit-message
```

### With Commit Message
After code review, invoke `/commit-message` to generate a conventional commit message based on the reviewed changes.

### With Doctor
If review reveals issues requiring debugging, invoke `/doctor` for systematic diagnosis.

### With Memory Bank
In R-P-I workflows, code review automatically updates Memory Bank with:
- Review completion status
- Files reviewed
- Issues found and fixed
- Quality improvements made

## Best Practices

1. **Always identify files first** — Never proceed without knowing what to review
2. **Fix automated issues first** — Don't do manual review until ruff/pytest pass
3. **Be thorough but pragmatic** — Focus on real issues, not nitpicks
4. **Preserve intent** — Don't change functionality during cleanup
5. **Test after cleanup** — Always verify code still works
6. **Use appropriate depth** — Quick for routine, Deep for critical
7. **Reference coding standards** — Use `.shared/` guidelines consistently

## Skill Structure

```
code-review/
├── SKILL.md                    # Skill definition with frontmatter
├── README.md                   # This file
├── .shared/                    # Symlink to coding-standards/references/
└── references/
    ├── 00_ROUTER.md           # Review depth routing logic
    ├── 01_SUMMARY.md          # Role and purpose
    ├── 02_TRIGGERS.md         # When to invoke, file identification
    ├── 03_ALWAYS.md           # Mandatory actions
    ├── 04_NEVER.md            # Prohibitions
    ├── 05_PROCEDURE.md        # Complete review process with checklist
    └── 06_FAILURES.md         # Error handling and recovery
```

## Examples

### Example 1: Standalone Quick Review
```
/code-review

Review all modified files (quick review)
```

### Example 2: Standalone Deep Review
```
/code-review

Files: src/algorithm.py, src/optimizer.py, tests/test_algorithm.py
Review depth: deep
Focus: numerical stability and performance
```

### Example 3: From Implementation Plan
```
/code-review

Plan: llm_docs/plans/2026-01-15-1500-plan-feature-x.md
Review depth: deep
```

### Example 4: Integrated in R-P-I
```
/rpi

Task: Implement user authentication
[... research, plan, implement phases ...]
[code-review automatically invoked]
[commit-message offered after review]
```

## Troubleshooting

### Symlink Broken
If `.shared/` symlink is broken:
```bash
cd skills/code-review
rm -rf .shared
ln -s ../coding-standards/references .shared
```

### Cannot Identify Files
If no files can be identified:
- Provide implementation plan path, OR
- Specify files explicitly, OR
- Confirm to review all modified files from git status

### Too Many Issues
If review finds excessive issues:
- Fix critical issues only
- Defer review and improve code quality first
- Break review into smaller chunks

### Tests Fail After Cleanup
If cleanup breaks tests:
- Revert problematic changes
- Analyze root cause more carefully
- Consider alternative fix approach

## See Also

- `rpi/` — Generic R-P-I workflow (includes code review)
- `algo-rpi/` — Algorithm R-P-I workflow (includes code review)
- `commit-message/` — Generate commit messages after review
- `coding-standards/` — Shared coding guidelines
- `doctor/` — Diagnose failures if issues found
- `memory-bank/` — Memory Bank management
