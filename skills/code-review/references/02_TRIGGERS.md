# Triggers — When to Invoke Code Review

## Primary Triggers

### After Implementation Phase
- Implementation phase of R-P-I workflow is complete
- Code changes have been made according to plan
- All implementation success criteria met
- Ready for quality assurance before commit

### Before Committing Code
- Code changes are staged or ready to stage
- Want to ensure quality before version control commit
- Need to verify adherence to guidelines
- Want to catch issues before they enter the codebase

### During Pull Request Review
- Reviewing code changes from team members
- Need systematic quality check
- Want to ensure consistency with codebase standards

### During Refactoring
- Cleaning up existing code
- Removing technical debt
- Improving code quality
- Modernizing legacy code

## Invocation Requirements

### MANDATORY: Identify Target Files First

Before proceeding with review, you MUST identify which files to review:

**Option 1: From Implementation Plan**
- If invoked after R-P-I implementation phase
- Read the plan document to identify modified/created files
- Use the files listed in implementation phases

**Option 2: From Git Status**
- If invoked standalone without plan context
- Run `git status --porcelain` to identify modified files
- Filter out untracked files that existed before current work session
- Focus on modified (M), added (A), renamed (R) files

**Option 3: User Specification**
- User explicitly provides list of files to review
- User specifies directory or module to review
- User requests review of specific components

**Option 4: From Implement Skillset Context**
- The `rpi-implement` or `algo-rpi-implement` skills should mention files modified/added
- Use this context to identify review scope
- Cross-reference with plan if available

### If No Files Identified

If no files can be identified and no recent modifications detected:

**Response:**
```
I'm ready to review code. Please provide:
- Path to the implementation plan in `llm_docs/plans/`, OR
- List of specific files to review, OR
- Confirmation to review all modified files from git status

I will review for quality, adherence to guidelines, and best practices.
```

Then wait for user input. **DO NOT proceed without clear scope.**

## When NOT to Invoke

- No code changes have been made
- Changes are purely documentation (unless doc quality review requested)
- Changes are configuration only (unless config review requested)
- Code is still in active development (wait for completion)
- Automated checks haven't been run yet (run them first)

## Expected Inputs

When invoked, expect one or more of:
- Path to implementation plan document
- List of modified files
- Scope specification (module, directory, component)
- Review depth preference (quick vs deep)
- Specific areas of concern or focus

## Expected Outputs

After review, provide:
- Summary of files reviewed
- Issues found and fixed (categorized)
- Automated check results (ruff, pytest)
- Quality assessment
- Readiness status for commit/deployment
- Updated Memory Bank (if part of R-P-I workflow)
