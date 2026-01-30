# Commit Message Skill

Generate descriptive, conventional commit messages based on actual code changes.

## Overview

The `commit-message` skill analyzes staged changes and generates clear, professional commit messages following the conventional commits specification. It ensures commits are well-documented and maintain a clean project history.

**Key Features:**
- Conventional commit format (type, scope, subject, body)
- Analyzes actual staged changes
- Context-aware (uses implementation plan, code review summary)
- User confirmation before committing
- Handles edge cases (no changes, multiple unrelated changes, etc.)

## When to Use

### Use Commit Message:
- After code review is complete
- Before committing changes to version control
- As final step in R-P-I workflows
- When you want professional, conventional commit messages
- When changes are complex and need good documentation

### Integration Points:
- **After code-review:** Automatically offered in R-P-I workflows
- **Standalone:** Explicitly invoked via `/commit-message` command
- **Before push:** Generate message before pushing to remote

## Quick Start

### After Code Review (R-P-I Workflow)
```
/rpi → research → plan → implement → code-review → /commit-message
```

The skill is automatically offered after code review completes.

### Standalone Usage
```
/commit-message

[Analyzes staged changes and generates commit message]
```

### With Context
```
/commit-message

Plan: llm_docs/plans/2026-01-15-1500-plan-feature-x.md
Notes: This implements the new authentication feature
```

## Conventional Commit Format

### Structure
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Commit Types

- **feat:** New feature or functionality
- **fix:** Bug fix
- **refactor:** Code refactoring (no functional change)
- **docs:** Documentation changes only
- **test:** Adding or updating tests
- **chore:** Maintenance tasks (dependencies, build, config)
- **perf:** Performance improvements
- **style:** Code style changes (formatting, no logic change)
- **ci:** CI/CD pipeline changes
- **build:** Build system or dependencies changes
- **revert:** Reverting a previous commit

### Scope (Optional)

Examples:
- Module: `auth`, `api`, `database`
- Component: `user-service`, `payment-flow`
- Feature: `login`, `checkout`, `dashboard`

### Subject Line Rules

- Under 72 characters
- Imperative mood ("add" not "added")
- No period at end
- Lowercase (except proper nouns)
- Clear and descriptive

### Body (Optional)

Add body when:
- Changes are complex
- Context would help future readers
- Multiple areas affected
- Breaking changes introduced

Body should explain:
- Why the change was made
- What problem it solves
- Important implementation details
- Impact or side effects

### Footer (Optional)

Use for:
- Breaking changes: `BREAKING CHANGE: description`
- Issue references: `Fixes #123`, `Closes #456`
- Co-authors: `Co-authored-by: Name <email>`

## Examples

### Example 1: Feature Addition
```
feat(auth): add JWT-based authentication

Implement JWT token generation and validation for user
authentication. Includes middleware for protecting routes
and token refresh mechanism.

- Add JWT token generation on login
- Add authentication middleware
- Add token refresh endpoint
- Add tests for auth flow
```

### Example 2: Bug Fix
```
fix(payment): prevent duplicate charge on retry

Add idempotency key to payment requests to prevent duplicate
charges when user retries failed payment. Uses transaction ID
as idempotency key.

Fixes #234
```

### Example 3: Refactoring
```
refactor(api): extract validation logic to separate module

Move validation logic from route handlers to dedicated
validator module. Improves code organization and reusability.
No functional changes.
```

### Example 4: Documentation
```
docs(readme): add deployment instructions

Add step-by-step deployment guide for production environment
including environment variables, database setup, and SSL
configuration.
```

### Example 5: Performance Improvement
```
perf(search): implement caching for frequent queries

Add Redis caching layer for search queries. Reduces database
load and improves response time by 80% for common searches.

- Add Redis client configuration
- Implement cache-aside pattern
- Add cache invalidation on data updates
- Add monitoring for cache hit rate
```

### Example 6: Breaking Change
```
feat(api): redesign user authentication endpoint

BREAKING CHANGE: Authentication endpoint now requires email
instead of username. Update all clients to use email field.

Migration guide:
- Change `username` field to `email` in login requests
- Update user model to include email field
```

## Process Flow

### Step 1: Verify Staged Changes
- Check `git diff --staged`
- If no staged changes, ask user to stage or cancel

### Step 2: Read Context
- Implementation plan (if available)
- Code review summary (if available)
- User notes (if provided)

### Step 3: Analyze Changes
- Determine change type (feat, fix, refactor, etc.)
- Identify scope (module, component, feature)
- Identify key changes and their purpose

### Step 4: Generate Message
- Create subject line (<72 chars, imperative mood)
- Add body if changes are complex
- Add footer if breaking changes or issue refs

### Step 5: Present to User
- Show complete message
- Explain type and scope choices
- List files changed
- Offer options: commit, modify, or cancel

### Step 6: Execute Commit
- If user approves, execute `git commit`
- Verify commit succeeded
- Report commit hash and summary

## Good vs. Bad Messages

### ❌ Bad Messages
```
fix bug
update code
changes
wip
misc updates
stuff
```

### ✅ Good Messages
```
fix(auth): resolve null pointer exception in user authentication
refactor(payment): migrate to async connection pool
feat(checkout): add support for multiple payment methods
docs(api): update authentication endpoint documentation
test(auth): add integration tests for login flow
```

## Special Cases

### Multiple Unrelated Changes
If staged changes include unrelated modifications, the skill will recommend splitting into separate commits:

```
I notice the staged changes include multiple unrelated modifications:
- Authentication feature (feat)
- Bug fix in payment (fix)
- Documentation updates (docs)

Recommendation: Split into separate commits for better history.
```

### No Staged Changes
If no changes are staged, the skill will check for unstaged changes and offer to stage them:

```
No staged changes found. I see unstaged changes in:
- src/auth/login.py
- src/payment/processor.py

Would you like me to:
1. Stage all changes and generate commit message
2. You stage specific files first
3. Cancel
```

### Merge Commits
For merge commits, the skill will suggest using the default Git merge message or a custom message.

## Integration with Other Skills

### After Code Review
```
/code-review → /commit-message
```

Code review completes, all checks pass, then commit message is generated.

### With Implementation Plan
```
/rpi-implement → /code-review → /commit-message
```

Implementation plan provides context for what was implemented, improving message quality.

### With Memory Bank
In R-P-I workflows, commit information is added to Memory Bank for cross-session continuity.

## Best Practices

1. **Stage changes first** — Ensure changes are staged before invoking
2. **Use context** — Provide implementation plan or notes for better messages
3. **Review before committing** — Always review the generated message
4. **Split unrelated changes** — Commit logically related changes together
5. **Add body for complex changes** — Explain why, not just what
6. **Reference issues** — Link to issue tracker when applicable
7. **Use conventional format** — Maintains consistent project history

## Skill Structure

```
commit-message/
├── SKILL.md                    # Skill definition with frontmatter
├── README.md                   # This file
└── references/
    ├── 00_ROUTER.md           # Routing logic (linear process)
    ├── 01_SUMMARY.md          # Role and purpose
    ├── 02_TRIGGERS.md         # When to invoke
    ├── 03_ALWAYS.md           # Mandatory actions
    ├── 04_NEVER.md            # Prohibitions
    ├── 05_PROCEDURE.md        # Complete generation process
    └── 06_FAILURES.md         # Error handling and recovery
```

## Troubleshooting

### No Staged Changes
Stage changes first:
```bash
git add <files>
```

Or stage all:
```bash
git add .
```

### Commit Failed
Check for:
- Pre-commit hooks failing
- Commit message format rejected by hooks
- Repository in conflicted state

### Subject Too Long
The skill will automatically shorten or move details to body.

### Wrong Type Selected
Provide feedback and the skill will regenerate with correct type.

## See Also

- `code-review/` — Code quality review (invoke before commit-message)
- `rpi/` — Generic R-P-I workflow (includes commit-message)
- `algo-rpi/` — Algorithm R-P-I workflow (includes commit-message)
- `memory-bank/` — Memory Bank management
