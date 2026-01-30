# Procedure — Commit Message Generation Process

## Step 1: Verify Staged Changes

Check that changes are staged for commit:

```bash
git diff --staged
```

### If Staged Changes Exist
- Proceed to Step 2

### If No Staged Changes
Check for unstaged changes:
```bash
git diff
```

**If unstaged changes exist:**
Ask user:
```
No staged changes found. I see unstaged changes in:
- [list of modified files]

Would you like me to:
1. Stage all changes and generate commit message
2. You stage specific files first
3. Cancel

Please choose an option.
```

**If no changes at all:**
Respond:
```
No changes detected (staged or unstaged).

Please make and stage changes before generating a commit message.
```

Stop and wait for user.

---

## Step 2: Read Context (if available)

### Implementation Plan
If invoked after R-P-I workflow or plan path provided:
- Read the plan document
- Understand what was implemented
- Note the feature/fix/refactor intent
- Use this to inform commit type and message

### Code Review Summary
If invoked after code-review:
- Review the summary report
- Note what issues were fixed
- Note any significant improvements
- Include quality improvements in message if relevant

### User Notes
If user provides specific context:
- Incorporate user's description
- Use user's preferred scope if provided
- Respect user's type preference if reasonable

---

## Step 3: Analyze Changes

Read the staged diff carefully:

### Identify Change Type
Determine the primary type of change:

- **feat:** New functionality added
  - New functions, classes, modules
  - New features or capabilities
  - User-facing additions

- **fix:** Bug fixes
  - Correcting incorrect behavior
  - Handling edge cases
  - Fixing crashes or errors

- **refactor:** Code restructuring
  - Improving code structure
  - No functional changes
  - Better organization or patterns

- **docs:** Documentation only
  - README updates
  - Code comments (if only change)
  - API documentation

- **test:** Test changes
  - Adding new tests
  - Updating existing tests
  - Test infrastructure

- **chore:** Maintenance
  - Dependency updates
  - Build configuration
  - Development tools

- **perf:** Performance improvements
  - Optimization
  - Reducing complexity
  - Caching, memoization

- **style:** Code style only
  - Formatting changes
  - No logic changes
  - Whitespace, indentation

### Identify Scope
Determine the affected area:
- Module name (e.g., `auth`, `api`, `database`)
- Component (e.g., `user-service`, `payment`)
- Feature area (e.g., `login`, `checkout`)
- File/directory if specific (e.g., `utils`, `models`)

### Identify Key Changes
Note the most important changes:
- What files were modified
- What functionality was added/changed/removed
- What problem was solved
- Any breaking changes

---

## Step 4: Generate Commit Message

### Subject Line

Format: `<type>(<scope>): <description>`

**Rules:**
- Type: One of the conventional types
- Scope: Optional, area affected
- Description: Clear, imperative mood, <72 chars
- No period at end
- Lowercase (except proper nouns)

**Examples:**
```
feat(auth): add OAuth2 authentication support
fix(api): resolve race condition in user creation
refactor(database): migrate to async connection pool
docs(readme): update installation instructions
test(auth): add integration tests for login flow
chore(deps): update dependencies to latest versions
perf(search): implement caching for frequent queries
```

### Body (if needed)

Add body if:
- Changes are complex
- Context would help future readers
- Multiple areas affected
- Breaking changes

**Format:**
- Blank line after subject
- Wrap at 72 characters
- Explain why, not what (code shows what)
- Use bullet points for multiple items

**Example:**
```
feat(checkout): add support for multiple payment methods

- Implement Stripe and PayPal integrations
- Add payment method selection UI
- Update order processing to handle different providers
- Add tests for each payment provider

This enables users to choose their preferred payment method,
improving conversion rates and user satisfaction.
```

### Footer (if needed)

Add footer for:
- Breaking changes: `BREAKING CHANGE: description`
- Issue references: `Fixes #123`, `Closes #456`
- Co-authors: `Co-authored-by: Name <email>`

---

## Step 5: Present to User

Show the complete commit message to user:

```
Proposed Commit Message:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
<type>(<scope>): <subject>

<body>

<footer>
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Reasoning:
- Type: <type> because <reason>
- Scope: <scope> because <reason>
- Subject: Describes <what was changed>

Files changed:
- <list of files from git diff --staged --name-only>

Options:
1. Commit with this message
2. Modify message (provide your version)
3. Cancel

Please choose an option.
```

Wait for user response.

---

## Step 6: Handle User Response

### Option 1: User Approves
Execute commit:
```bash
git commit -m "<subject>" -m "<body>" -m "<footer>"
```

Or if using multi-line:
```bash
git commit -F - <<EOF
<subject>

<body>

<footer>
EOF
```

### Option 2: User Modifies
- Accept user's modified message
- Use their version for commit
- Execute commit with modified message

### Option 3: User Cancels
- Do not commit
- Respond: "Commit cancelled. Changes remain staged."

---

## Step 7: Verify Commit

After committing, verify success:

```bash
git log -1 --oneline
```

Report to user:
```
Commit successful ✓

Commit: <hash> <subject>

You can now push changes or continue working.
```

---

## Examples

### Example 1: Feature Addition
**Staged changes:** New authentication module

**Generated message:**
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
**Staged changes:** Fix in payment processing

**Generated message:**
```
fix(payment): prevent duplicate charge on retry

Add idempotency key to payment requests to prevent duplicate
charges when user retries failed payment. Uses transaction ID
as idempotency key.

Fixes #234
```

### Example 3: Refactoring
**Staged changes:** Code restructuring

**Generated message:**
```
refactor(api): extract validation logic to separate module

Move validation logic from route handlers to dedicated
validator module. Improves code organization and reusability.
No functional changes.
```

### Example 4: Documentation
**Staged changes:** README updates

**Generated message:**
```
docs(readme): add deployment instructions

Add step-by-step deployment guide for production environment
including environment variables, database setup, and SSL
configuration.
```

### Example 5: Multiple Related Changes
**Staged changes:** Feature with tests and docs

**Generated message:**
```
feat(search): add full-text search capability

Implement full-text search using PostgreSQL's tsvector.
Includes search indexing, query parsing, and result ranking.

- Add search index to database
- Implement search query parser
- Add search API endpoint
- Add search tests
- Update API documentation
```

---

## Special Cases

### Breaking Changes
If changes break backward compatibility:

```
feat(api): redesign user authentication endpoint

BREAKING CHANGE: Authentication endpoint now requires email
instead of username. Update all clients to use email field.

Migration guide:
- Change `username` field to `email` in login requests
- Update user model to include email field
```

### Multiple Unrelated Changes
If staged changes include unrelated modifications:

```
I notice the staged changes include multiple unrelated modifications:
- Authentication feature (feat)
- Bug fix in payment (fix)
- Documentation updates (docs)

Recommendation: Split into separate commits for better history.

Would you like me to:
1. Generate message for all changes together (not recommended)
2. Guide you through staging and committing separately
3. Cancel so you can organize changes

Please choose an option.
```

### Merge Commits
If this is a merge:

```
This appears to be a merge commit.

Suggested message:
merge: merge feature/user-auth into main

Or use default Git merge message.

Proceed with commit?
```
