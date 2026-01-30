# ALWAYS — Mandatory Actions

## Analyze Actual Changes

**YOU MUST analyze staged changes:**
```bash
git diff --staged
```

**YOU MUST understand:**
- What files were modified, added, or deleted
- What specific changes were made in each file
- The intent behind the changes
- The scope/area affected

## Use Conventional Commit Format

**YOU MUST follow conventional commit format:**

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type MUST be one of:**
- `feat`: New feature or functionality
- `fix`: Bug fix
- `refactor`: Code refactoring (no functional change)
- `docs`: Documentation changes only
- `test`: Adding or updating tests
- `chore`: Maintenance tasks (dependencies, build, config)
- `perf`: Performance improvements
- `style`: Code style changes (formatting, no logic change)
- `ci`: CI/CD pipeline changes
- `build`: Build system or dependencies changes
- `revert`: Reverting a previous commit

**Scope (optional) examples:**
- Module name: `auth`, `api`, `database`
- Component: `user-service`, `payment-flow`
- Feature area: `login`, `checkout`, `dashboard`

**Subject MUST:**
- Be under 72 characters
- Use imperative mood ("add" not "added" or "adds")
- Not end with a period
- Be lowercase (except proper nouns)
- Clearly describe what changed

## Be Specific

**YOU MUST be specific about what changed:**
- ❌ "fix bug"
- ✅ "fix null pointer exception in user authentication"

- ❌ "update code"
- ✅ "refactor payment processing to use async/await"

- ❌ "add feature"
- ✅ "feat(checkout): add support for multiple payment methods"

## Add Body When Needed

**YOU MUST add body if:**
- Changes are complex or non-obvious
- Multiple files/areas affected
- Context or reasoning would help future readers
- Breaking changes introduced

**Body should explain:**
- Why the change was made
- What problem it solves
- Any important implementation details
- Impact or side effects

## Present for Confirmation

**YOU MUST present commit message to user before committing:**
- Show the complete message
- Explain type and scope choices
- Offer option to modify
- Wait for explicit approval
- Do NOT commit without confirmation

## Verify Commit Success

**YOU MUST verify after committing:**
```bash
git log -1
```

Confirm the commit was created successfully.
