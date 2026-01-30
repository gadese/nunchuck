# Router — Code Review Skill

## Default Route

Read all references in order: 01 → 02 → 03 → 04 → 05 → 06

## Review Depth Options

### Quick Review
**When to use:**
- Time-constrained situations
- Low-risk changes
- Small, focused modifications
- Routine updates

**Process:**
1. Read 01_SUMMARY.md (role and purpose)
2. Read 02_TRIGGERS.md (when to invoke)
3. Read 03_ALWAYS.md (mandatory actions)
4. Read 04_NEVER.md (prohibitions)
5. Execute automated checks only from 05_PROCEDURE.md:
   - Run `ruff check` on target files
   - Run `ruff format --check` on target files
   - Run `pytest` on related test files
6. Fix any automated issues found
7. Skip manual checklist review
8. Provide brief summary

### Deep Review
**When to use:**
- Critical code paths
- Complex implementations
- Algorithm or ML/DL code
- Production-ready code
- Security-sensitive code
- Performance-critical code

**Process:**
1. Read all references 01-06 in order
2. Execute full automated checks from 05_PROCEDURE.md
3. Execute complete manual checklist review from 05_PROCEDURE.md
4. Apply all cleanup steps
5. Verify fixes thoroughly
6. Update Memory Bank
7. Provide comprehensive summary

## Invocation Context

### Standalone Invocation
- User explicitly calls `/code-review`
- Must identify target files first (git status or user specification)
- Default to **Quick Review** unless user requests deep review

### R-P-I Workflow Invocation
- Called after implementation phase
- Files to review come from implementation plan
- Default to **Deep Review** for thoroughness
- Can downgrade to Quick Review if time-constrained

## No Files Specified

If no files are specified and no recent modifications detected:
- Ask user to specify files or scope
- Offer to review all modified files from `git status --porcelain`
- Do NOT proceed without clear scope
