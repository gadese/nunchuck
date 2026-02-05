# Always

## Mandatory Actions

### 1. Read the Entire Plan

- Read the complete plan document before starting the review
- Understand the overall objective and context
- Note the current state, desired end state, and design decisions

### 2. Review All Dimensions

Check each dimension systematically:

**Edge Cases:**
- [ ] Empty inputs, null values, undefined states
- [ ] Boundary conditions (min/max values, limits)
- [ ] Concurrent access or race conditions
- [ ] Network failures, timeouts, retries
- [ ] Partial failures or incomplete operations

**Error Handling:**
- [ ] Exception handling strategy defined
- [ ] Input validation specified
- [ ] Graceful degradation for failures
- [ ] Rollback or cleanup procedures
- [ ] Error messages and logging

**Performance:**
- [ ] Scalability considerations
- [ ] Inefficient patterns (N+1 queries, nested loops)
- [ ] Resource usage (memory, CPU, I/O)
- [ ] Caching strategy if applicable
- [ ] Database query optimization

**Security:**
- [ ] Input validation and sanitization
- [ ] Authentication and authorization
- [ ] Sensitive data handling
- [ ] SQL injection, XSS, CSRF prevention
- [ ] API security (rate limiting, tokens)

**Maintainability:**
- [ ] Code clarity and readability
- [ ] Documentation requirements
- [ ] Testability (unit, integration tests)
- [ ] Modularity and separation of concerns
- [ ] Technical debt considerations

**Dependencies:**
- [ ] All required dependencies listed
- [ ] Version compatibility checked
- [ ] No circular dependencies
- [ ] External service dependencies documented

### 3. Annotate In-Place

- Modify the plan document directly with corrections
- Use clear markers for changes (e.g., "**REVIEW NOTE:**" or "**ADDED:**")
- Preserve the original structure and formatting
- Add new sections if critical items are missing

### 4. Provide Summary

After modifying the plan, provide a brief summary:
```
## Review Summary

**Issues Found:** [count]

**Key Changes:**
- [Change 1 with section reference]
- [Change 2 with section reference]
- [Change 3 with section reference]

**Recommendation:** [Proceed / Needs revision / Critical issues]
```

### 5. Be Specific

- Reference exact sections and line numbers
- Provide concrete examples of issues
- Suggest specific solutions, not vague improvements
