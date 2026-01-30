# NEVER — Prohibitions

## Generic Messages

**YOU MUST NOT use generic, uninformative messages:**
- ❌ "fix bug"
- ❌ "update code"
- ❌ "changes"
- ❌ "wip"
- ❌ "misc updates"
- ❌ "stuff"
- ❌ "fix"
- ❌ "update"

## Implementation Details in Subject

**YOU MUST NOT include implementation details in subject line:**
- ❌ "feat: add UserService class with authenticate method using bcrypt"
- ✅ "feat(auth): add user authentication service"
  - (Details go in body if needed)

## Commit Without Confirmation

**YOU MUST NOT commit without user approval:**
- Always present the message first
- Wait for explicit confirmation
- Allow user to modify if desired
- Never auto-commit

## Incorrect Type

**YOU MUST NOT use wrong commit type:**
- Don't use `feat` for bug fixes (use `fix`)
- Don't use `fix` for refactoring (use `refactor`)
- Don't use `chore` for user-facing changes (use `feat` or `fix`)
- Don't use `style` for logic changes (use appropriate type)

## Long Subject Lines

**YOU MUST NOT exceed 72 characters in subject:**
- Keep subject concise
- Move details to body
- Use abbreviations if necessary (but keep clear)

## Past Tense or Present Continuous

**YOU MUST NOT use past tense or present continuous:**
- ❌ "added feature" (past tense)
- ❌ "adding feature" (present continuous)
- ✅ "add feature" (imperative mood)

## Ending Subject with Period

**YOU MUST NOT end subject line with period:**
- ❌ "fix: resolve authentication issue."
- ✅ "fix: resolve authentication issue"

## Capitalize Subject (except type)

**YOU MUST NOT capitalize subject after colon:**
- ❌ "feat: Add new feature"
- ✅ "feat: add new feature"

## Ignore Context

**YOU MUST NOT ignore available context:**
- If implementation plan provided, read it
- If code review summary provided, use it
- If user provides notes, incorporate them
- Don't generate message in vacuum

## Commit Unstaged Changes

**YOU MUST NOT commit unstaged changes without asking:**
- Only commit what's staged
- If unstaged changes exist, ask user
- Don't auto-stage without permission

## Skip Verification

**YOU MUST NOT skip verification:**
- Always check staged changes exist
- Always verify commit succeeded
- Always confirm message with user

## Multiple Unrelated Changes

**YOU MUST NOT encourage committing unrelated changes:**
- If staged changes span multiple unrelated areas, suggest splitting
- Each commit should have single logical purpose
- Recommend separate commits for unrelated changes
