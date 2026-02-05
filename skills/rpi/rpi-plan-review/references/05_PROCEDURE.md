# Procedure

## Review Process

Follow these steps in order:

### Step 1: Read and Understand

1. **Read the Plan Completely**
   - Read the entire plan document from start to finish
   - Understand the objective, current state, and desired end state
   - Note the design decisions and rationale
   - Identify the phases and their dependencies

2. **Read Referenced Files**
   - If the plan references specific files with line ranges, read those sections
   - Verify that the plan's understanding of the current state is accurate
   - Check if any critical files or patterns are missing from the plan

3. **Understand the Context**
   - What problem is being solved?
   - What are the constraints and requirements?
   - What is the scope (and out of scope)?

### Step 2: Systematic Review

Review the plan across all dimensions. For each dimension, ask:

#### Edge Cases Review

- **Empty/Null Inputs**: Does the plan handle empty collections, null values, undefined states?
- **Boundary Conditions**: Are min/max values, limits, and thresholds considered?
- **Concurrent Access**: If applicable, does the plan address race conditions or concurrent modifications?
- **Network Issues**: Are timeouts, retries, and network failures handled?
- **Partial Failures**: What happens if an operation partially succeeds?

**Action**: Note any missing edge case handling.

#### Error Handling Review

- **Exception Strategy**: Is there a clear approach to exception handling?
- **Input Validation**: Are inputs validated before processing?
- **Graceful Degradation**: Does the system fail gracefully or crash?
- **Rollback/Cleanup**: Are there procedures for rolling back failed operations?
- **Logging**: Are errors logged with sufficient detail for debugging?

**Action**: Note any missing error handling.

#### Performance Review

- **Scalability**: Will this approach scale with increased load?
- **Inefficient Patterns**: Are there N+1 queries, nested loops, or other inefficiencies?
- **Resource Usage**: Are memory, CPU, or I/O resources used efficiently?
- **Caching**: Should caching be considered?
- **Database Queries**: Are queries optimized?

**Action**: Note any performance concerns.

#### Security Review

- **Input Validation**: Are all inputs sanitized and validated?
- **Authentication**: Is authentication required and properly implemented?
- **Authorization**: Are access controls in place?
- **Data Exposure**: Is sensitive data protected?
- **Common Vulnerabilities**: Are SQL injection, XSS, CSRF prevented?

**Action**: Note any security gaps.

#### Maintainability Review

- **Code Clarity**: Will the implementation be clear and readable?
- **Documentation**: Are documentation requirements specified?
- **Testability**: Are unit and integration tests planned?
- **Modularity**: Is the design modular and maintainable?
- **Technical Debt**: Are any shortcuts or debt items acknowledged?

**Action**: Note any maintainability concerns.

#### Dependencies Review

- **Required Dependencies**: Are all dependencies listed?
- **Version Compatibility**: Are version constraints specified?
- **Circular Dependencies**: Are there any circular dependency risks?
- **External Services**: Are external service dependencies documented?

**Action**: Note any missing dependencies.

### Step 3: Annotate the Plan

1. **Open the Plan for Editing**
   - Use the edit tool to modify the plan document

2. **Add Review Notes**
   - For each issue found, add a note in the relevant section
   - Use clear markers like "**REVIEW NOTE:**" or "**ADDED:**"
   - Be specific about what's missing and why it matters

3. **Add Missing Sections**
   - If critical items are completely missing, add new sections
   - Example: If error handling is not mentioned, add an "Error Handling Strategy" subsection

4. **Preserve Structure**
   - Keep the original plan structure intact
   - Add annotations inline rather than rewriting sections
   - Maintain the original formatting and style

### Step 4: Summarize Changes

After modifying the plan, provide a summary in chat:

```markdown
## Plan Review Complete

**Plan Reviewed:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-topic.md`

**Issues Found:** [count]

**Key Changes Made:**

1. **Edge Cases** (Section X, Phase Y):
   - Added handling for empty input collections
   - Added boundary condition checks for user limits

2. **Error Handling** (Section X, Phase Y):
   - Added exception handling strategy
   - Added rollback procedure for failed operations

3. **Performance** (Section X, Phase Y):
   - Flagged potential N+1 query issue
   - Suggested caching strategy for frequently accessed data

4. **Security** (Section X, Phase Y):
   - Added input validation requirements
   - Added authentication check

5. **Dependencies** (Section X):
   - Added missing library dependency with version

**Recommendation:** [Choose one]
- ✅ **Proceed to implementation** - Plan is solid with minor improvements added
- ⚠️ **Needs revision** - Some issues require user decision before proceeding
- 🚫 **Critical issues** - Plan has fundamental flaws that must be addressed

**Next Steps:**
[If proceeding] The plan has been updated and is ready for implementation.
[If needs revision] Please review the annotated sections and provide guidance on [specific issues].
[If critical] The following issues must be resolved: [list critical issues].
```

### Step 5: Wait for User Response

- If recommendation is "Proceed", wait for user confirmation
- If recommendation is "Needs revision" or "Critical issues", wait for user guidance
- Do not automatically proceed to the next phase

## Example Annotation

**Before:**
```markdown
### Phase 2: Add User Validation

**Implementation Steps:**
1. Create validation function
2. Call validation in API endpoint
3. Return error if invalid
```

**After:**
```markdown
### Phase 2: Add User Validation

**REVIEW NOTE:** Consider edge cases and error handling

**Implementation Steps:**
1. Create validation function
   - **ADDED:** Handle null/undefined inputs
   - **ADDED:** Validate email format with regex
   - **ADDED:** Check username length (min 3, max 50 chars)
2. Call validation in API endpoint
   - **ADDED:** Wrap in try-catch for validation errors
3. Return error if invalid
   - **ADDED:** Return 400 status with descriptive error message
   - **ADDED:** Log validation failures for monitoring

**ADDED: Error Handling:**
- Validation errors return 400 with `{"error": "validation_failed", "details": [...]}`
- Unexpected errors return 500 and are logged
- All errors include request ID for tracing
```

## Review Checklist

Before completing the review, verify:

- [ ] Read entire plan document
- [ ] Reviewed all 6 dimensions (edge cases, errors, performance, security, maintainability, dependencies)
- [ ] Annotated plan with specific, actionable feedback
- [ ] Added missing sections if critical items were absent
- [ ] Preserved original plan structure
- [ ] Provided summary with recommendation
- [ ] Identified any questions requiring user decision
