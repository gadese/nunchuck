# Failures

## Error Handling

### Plan File Not Found

**Symptom**: The specified plan file does not exist

**Response**:
```
I cannot find the plan file at `[path]`.

Please verify:
- The file path is correct
- The plan has been created (use `/rpi-plan` if needed)
- The file is in the expected location (usually `llm_docs/plans/`)

Available plan files:
- [list files in llm_docs/plans/]
```

### Plan File Unreadable

**Symptom**: The plan file exists but cannot be read (permissions, encoding issues)

**Response**:
```
I cannot read the plan file at `[path]`.

Error: [specific error message]

Please check:
- File permissions
- File encoding (should be UTF-8)
- File is not corrupted
```

### Plan Malformed

**Symptom**: The plan file exists but is missing critical sections or is not in the expected format

**Response**:
```
The plan at `[path]` appears to be incomplete or malformed.

Missing or invalid sections:
- [list issues]

Should I:
1. Proceed with review anyway and flag these structural issues
2. Wait for the plan to be completed first

Please advise.
```

### No Issues Found

**Symptom**: The plan is exceptionally well-written with no improvements needed

**Response**:
```
## Plan Review Complete

**Plan Reviewed:** `[path]`

**Issues Found:** 0

This plan is comprehensive and well-considered. It addresses:
✅ Edge cases and boundary conditions
✅ Error handling and validation
✅ Performance considerations
✅ Security requirements
✅ Maintainability and testability
✅ Dependencies and external services

**Recommendation:** ✅ **Proceed to implementation** - No changes needed.

**Next Steps:** The plan is ready for implementation.
```

### Fundamental Design Flaw

**Symptom**: The plan has a critical design flaw that makes it unworkable

**Response**:
```
## Plan Review Complete

**Plan Reviewed:** `[path]`

**Critical Issue Identified:**

[Describe the fundamental flaw clearly]

**Why This Is Critical:**
[Explain the impact]

**Suggested Approach:**
[Provide a high-level alternative approach]

**Recommendation:** 🚫 **Critical issues** - This design flaw must be addressed before implementation.

**Next Steps:**
1. Discuss the alternative approach
2. Decide whether to revise the current plan or use `/rpi-plan-reimagine` for a fresh perspective
```

### User Disagrees with Review

**Symptom**: User challenges the review findings or suggests the review is incorrect

**Response**:
1. **Acknowledge**: "Thank you for the feedback. Let me reconsider."
2. **Verify**: Re-read the relevant sections of the plan and code
3. **Clarify**: Ask specific questions to understand the disagreement
4. **Adjust**: If the user is correct, acknowledge and update the review
5. **Explain**: If the review is valid, provide more detailed rationale

**Example**:
```
You're right to question that. Let me re-examine [specific section].

[After re-reading]

I see now that [explanation]. You're correct that [acknowledgment].

I'll update the review to reflect this.
```

OR

```
I understand your concern. Let me clarify why I flagged this:

[Detailed explanation with specific examples]

However, if you prefer to proceed with the current approach because [user's rationale], 
I can remove that review note. What would you like to do?
```

## Recovery Strategies

### Incomplete Review

If you realize mid-review that you missed a dimension:
1. Acknowledge: "I need to complete the review of [dimension]"
2. Go back and review that dimension
3. Update the plan with additional findings
4. Provide an updated summary

### Over-Nitpicking

If you realize you're being too pedantic:
1. Step back and assess: "Are these issues high-impact?"
2. Remove trivial comments
3. Focus on the most important 3-5 issues
4. Provide a revised summary focusing on high-impact items

### Unclear Plan Section

If a section of the plan is ambiguous:
1. Flag it clearly: "**REVIEW QUESTION:** This section is unclear. [Specific question]"
2. Do not assume or guess the intent
3. Ask the user for clarification
4. Continue reviewing other sections
