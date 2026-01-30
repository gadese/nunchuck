# Failures — Error Handling and Recovery

## No Staged Changes

**Symptoms:**
- `git diff --staged` returns empty
- User invoked commit-message but nothing staged

**Recovery:**
1. Check for unstaged changes: `git diff`
2. If unstaged changes exist, ask user:
   ```
   No staged changes found. I see unstaged changes in:
   - [list files]
   
   Would you like me to:
   1. Stage all changes and generate commit message
   2. You stage specific files first
   3. Cancel
   ```
3. If no changes at all:
   ```
   No changes detected (staged or unstaged).
   
   Please make and stage changes before generating a commit message.
   ```
4. Wait for user action

## Git Not Available

**Symptoms:**
- `git` command not found
- Not in a git repository

**Recovery:**
1. Check if in git repository: `git status`
2. If not a git repo:
   ```
   Error: Not in a git repository.
   
   Please initialize git repository first:
   git init
   
   Or navigate to a git repository.
   ```
3. If git not installed:
   ```
   Error: Git is not installed or not in PATH.
   
   Please install git and try again.
   ```

## Commit Fails

**Symptoms:**
- `git commit` returns error
- Commit hooks fail
- Pre-commit checks fail

**Recovery:**
1. Capture error message
2. Report to user:
   ```
   Commit failed with error:
   [error message]
   
   Common causes:
   - Pre-commit hooks failed (fix issues and retry)
   - Commit message format rejected (check hooks)
   - Repository in conflicted state (resolve conflicts)
   
   Would you like to:
   1. Retry with same message
   2. Generate new message
   3. Cancel
   ```
3. Follow user's choice

## Cannot Determine Change Type

**Symptoms:**
- Changes are ambiguous
- Multiple types apply
- Unclear intent

**Recovery:**
1. Ask user:
   ```
   I'm having trouble determining the commit type.
   
   The changes include:
   - [describe changes]
   
   This could be:
   - feat: If this adds new functionality
   - fix: If this corrects a bug
   - refactor: If this restructures without changing behavior
   
   Which type best describes these changes?
   ```
2. Use user's choice
3. Proceed with generation

## Multiple Unrelated Changes

**Symptoms:**
- Staged changes span multiple unrelated areas
- Different types of changes mixed
- Would be better as separate commits

**Recovery:**
1. Identify distinct change groups
2. Recommend to user:
   ```
   I notice the staged changes include multiple unrelated modifications:
   
   Group 1: Authentication feature (feat)
   - src/auth/login.py
   - src/auth/middleware.py
   
   Group 2: Bug fix in payment (fix)
   - src/payment/processor.py
   
   Group 3: Documentation updates (docs)
   - README.md
   
   Recommendation: Split into separate commits for clearer history.
   
   Would you like me to:
   1. Generate message for all changes together (not recommended)
   2. Guide you through staging and committing separately
   3. Cancel so you can organize changes
   ```
3. Follow user's preference

## User Rejects Message

**Symptoms:**
- User doesn't like generated message
- Wants different type or scope
- Wants different wording

**Recovery:**
1. Ask for feedback:
   ```
   I understand you'd like to modify the message.
   
   What would you like to change?
   - Different type? (current: <type>)
   - Different scope? (current: <scope>)
   - Different subject? (current: <subject>)
   - Different body?
   - Provide complete custom message?
   ```
2. Regenerate based on feedback
3. Present new version
4. Repeat until user approves

## Subject Too Long

**Symptoms:**
- Generated subject exceeds 72 characters
- Cannot shorten without losing clarity

**Recovery:**
1. Try abbreviations or shorter wording
2. If still too long, move details to body:
   ```
   Subject line is too long ([N] characters, max 72).
   
   Original: <long subject>
   
   Shortened: <abbreviated subject>
   
   Details moved to body:
   <full description>
   
   Is this acceptable?
   ```
3. Get user approval

## Merge Conflict State

**Symptoms:**
- Repository has unresolved conflicts
- Cannot commit until conflicts resolved

**Recovery:**
1. Detect conflict state: `git status`
2. Report to user:
   ```
   Error: Repository has unresolved merge conflicts.
   
   Conflicted files:
   - [list files]
   
   Please resolve conflicts before committing:
   1. Edit conflicted files
   2. Stage resolved files: git add <files>
   3. Invoke commit-message again
   ```

## Detached HEAD State

**Symptoms:**
- Repository in detached HEAD state
- Commit would create orphaned commit

**Recovery:**
1. Detect state: `git status`
2. Warn user:
   ```
   Warning: Repository is in detached HEAD state.
   
   Committing now will create an orphaned commit.
   
   Recommendation:
   1. Create a branch: git checkout -b <branch-name>
   2. Then commit changes
   
   Or:
   1. Return to a branch: git checkout <branch-name>
   2. Then commit changes
   
   Proceed anyway? (not recommended)
   ```
3. Wait for user decision

## Empty Commit

**Symptoms:**
- All changes are whitespace or formatting
- No meaningful changes to commit

**Recovery:**
1. Analyze changes
2. If truly empty:
   ```
   Warning: Staged changes appear to be whitespace/formatting only.
   
   This might not warrant a commit.
   
   Would you like to:
   1. Commit anyway (use style type)
   2. Unstage and skip commit
   3. Review changes again
   ```
3. Follow user's choice

## Context Unavailable

**Symptoms:**
- Implementation plan not found
- Code review summary not available
- Cannot access context files

**Recovery:**
1. Proceed with available information
2. Note in message generation:
   ```
   Note: Could not access implementation plan/code review summary.
   
   Generating message based solely on staged changes.
   
   Message may be less detailed than usual.
   ```
3. Generate best possible message from diff alone

## Escalation

If you encounter an issue not covered here:
1. Document the issue clearly
2. Report to user with context
3. Suggest possible solutions
4. Wait for user guidance
5. Do NOT commit without user approval
