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

### Plan Already Optimal

**Symptom**: After analysis, no significant optimizations are found

**Response**:
```
## Plan Analysis Complete

**Plan Reviewed:** `[path]`

After thorough analysis, the current plan is already well-optimized:

✅ **Algorithmic Efficiency**: Optimal algorithms chosen
✅ **Data Structures**: Appropriate structures for the operations
✅ **Code Patterns**: Clean, elegant patterns used
✅ **Simplicity**: Approach is already simple and clear
✅ **Robustness**: Edge cases and errors well-handled
✅ **Readability**: Clear and maintainable structure

**Recommendation:** No reimagination needed. Proceed with the current plan.

**Rationale:** The plan demonstrates good engineering practices and there are no 
meaningful optimizations that would justify a rewrite. The effort to reimagine 
would not yield significant benefits.
```

### Insufficient Context

**Symptom**: Not enough information to reimagine effectively

**Response**:
```
I need additional context to reimagine this plan effectively.

**Missing Information:**
- [What's missing]

**Available Options:**
1. Provide the research document at `[path]`
2. Provide specific optimization goals (performance, simplicity, etc.)
3. Proceed with limited context (may miss optimization opportunities)

What would you like to do?
```

### Optimization Requires Breaking Changes

**Symptom**: The best optimization would require breaking changes

**Response**:
```
## Optimization Analysis

I've identified a significant optimization opportunity, but it requires breaking changes:

**Proposed Optimization:**
[Description of optimization]

**Benefits:**
- [Benefit 1]
- [Benefit 2]

**Breaking Changes Required:**
- [Breaking change 1]
- [Breaking change 2]

**Options:**
1. **Accept breaking changes**: Proceed with V2 plan including breaking changes
2. **Constrain to compatibility**: Create V2 plan with non-breaking optimizations only
3. **Stick with V1**: Keep original plan if breaking changes are not acceptable

Which approach would you prefer?
```

### User Disagrees with Optimization

**Symptom**: User questions or challenges the proposed optimizations

**Response**:
1. **Acknowledge**: "Thank you for the feedback. Let me reconsider."
2. **Clarify**: Ask specific questions to understand the concern
3. **Verify**: Re-examine the optimization with the user's perspective
4. **Adjust**: If the user is correct, acknowledge and revise
5. **Explain**: If the optimization is valid, provide more detailed rationale

**Example**:
```
You raise a good point about [concern].

Let me reconsider this optimization:

[Analysis with user's perspective]

You're right that [acknowledgment]. I'll adjust the V2 plan to [adjustment].

OR

I understand your concern. Here's why I still recommend this optimization:

[Detailed rationale with examples]

However, if you prefer the V1 approach because [user's rationale], we can 
proceed with V1 or create a hybrid approach. What would you prefer?
```

### V2 Plan More Complex Than V1

**Symptom**: The reimagined plan is actually more complex than the original

**Response**:
```
## Reimagination Review

After writing the V2 plan, I've realized it's more complex than V1:

**V1 Complexity:** [Assessment]
**V2 Complexity:** [Assessment]

**Why V2 is more complex:**
[Explanation]

**Recommendation:** Stick with V1 plan.

**Rationale:** The optimizations I attempted introduce more complexity than they 
save. The V1 plan is simpler and more maintainable. Sometimes the straightforward 
approach is the best approach.
```

### Optimization Assumptions Invalid

**Symptom**: After verification, the optimization assumptions don't hold

**Response**:
```
## Optimization Verification Failed

I proposed an optimization based on [assumption], but after verifying against 
the codebase, this assumption is invalid:

**Assumption:** [What I assumed]
**Reality:** [What's actually true]
**Impact:** [Why the optimization won't work]

**Revised Approach:**
I'll focus on other optimization opportunities that are valid:
- [Alternative optimization 1]
- [Alternative optimization 2]

Proceeding with revised V2 plan.
```

## Recovery Strategies

### Incomplete Analysis

If you realize mid-writing that you missed an optimization opportunity:
1. Acknowledge: "I've identified an additional optimization"
2. Analyze the new opportunity
3. Incorporate it into the V2 plan
4. Update the summary to include it

### Over-Optimization

If you realize you're over-engineering:
1. Step back and assess: "Is this actually simpler?"
2. Compare V2 complexity to V1 complexity honestly
3. If V2 is more complex, acknowledge it
4. Either simplify V2 or recommend sticking with V1

### Missing Critical Detail

If you realize you omitted something important from V1:
1. Acknowledge: "I need to include [detail] from V1"
2. Add the missing detail to V2
3. Ensure V2 is as thorough as V1
4. Update the summary if needed
