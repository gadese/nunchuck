# Triggers — When to Invoke Commit Message

## Primary Triggers

### After Code Review
- Code review phase is complete
- All quality checks passed
- Code is clean and ready to commit
- Automatic invocation in R-P-I workflows

### Before Git Commit
- Changes are staged (`git add` completed)
- User is ready to commit
- Want professional, conventional commit message
- Standalone invocation

### After Implementation
- Implementation phase complete
- Changes tested and verified
- Ready to version control the changes

## Invocation Requirements

### Staged Changes Required

Before proceeding, verify that changes are staged:

```bash
git diff --staged
```

**If no staged changes:**
- Check for unstaged changes (`git diff`)
- Ask user if they want to stage all changes
- Or ask user to stage specific files first

**If staged changes exist:**
- Proceed with commit message generation

### Expected Context

When invoked, may receive:
- Implementation plan path (for context on what was implemented)
- Code review summary (for understanding changes)
- User notes or preferences for commit message
- Specific scope or type hints

## When NOT to Invoke

- No changes staged for commit
- Changes not yet reviewed (invoke code-review first)
- Work still in progress
- User wants to manually write commit message

## Expected Inputs

Optional inputs that help generate better messages:
- Implementation plan path (for context)
- Code review summary (for understanding quality improvements)
- User-specified commit type or scope
- Additional context or notes

## Expected Outputs

After generation:
- Conventional commit message (type, scope, subject, body)
- Explanation of why this type/scope was chosen
- User confirmation prompt
- Option to modify before committing
- Execution of `git commit` if user approves
