# Always

## Mandatory Actions

### 1. Read All Available Context

- **Original Plan**: Read the complete plan document
- **Research Document**: Read the research document if available
- **Review Notes**: Read any review annotations or notes in the plan
- **Relevant Code**: Read key files referenced in the plan to understand current patterns
- **Memory Bank**: Read `llm_docs/memory/` files for project context

### 2. Identify Optimization Opportunities

Systematically look for:

**Algorithmic Improvements:**
- [ ] Can we use a better algorithm? (e.g., O(n) instead of O(n²))
- [ ] Can we leverage built-in optimized functions?
- [ ] Can we use vectorization or matrix operations instead of loops?
- [ ] Can we reduce redundant computations?

**Data Structure Improvements:**
- [ ] Is the data structure optimal for the operations? (set vs list, dict vs array)
- [ ] Can we reduce memory usage?
- [ ] Can we improve cache locality?

**Pattern Improvements:**
- [ ] Can we use recursion elegantly?
- [ ] Can we use comprehensions instead of loops?
- [ ] Can we use functional composition?
- [ ] Can we make the code more declarative?

**Simplification Opportunities:**
- [ ] Can we reduce nesting depth?
- [ ] Can we eliminate redundant logic?
- [ ] Can we combine similar operations?
- [ ] Can we clarify intent with better abstractions?

**Robustness Improvements:**
- [ ] Can we handle edge cases more elegantly?
- [ ] Can we improve error handling?
- [ ] Can we add defensive checks without cluttering code?

**Readability Improvements:**
- [ ] Can we improve naming?
- [ ] Can we restructure for clarity?
- [ ] Can we reduce cognitive load?

### 3. Write the New Plan from Scratch

- Start with a blank document
- Use the same plan template structure
- Write each section fresh, incorporating optimizations
- Reference the original plan for context but don't copy-paste
- Include all necessary sections (Overview, Current State, Phases, etc.)

### 4. Document Key Optimizations

Add a new section to the plan:

```markdown
## Optimizations from V1

This V2 plan incorporates the following key optimizations:

1. **[Optimization Category]**: [Description]
   - **V1 Approach**: [Original approach]
   - **V2 Approach**: [New approach]
   - **Rationale**: [Why this is better]
   - **Impact**: [Expected improvement]

2. **[Optimization Category]**: [Description]
   - **V1 Approach**: [Original approach]
   - **V2 Approach**: [New approach]
   - **Rationale**: [Why this is better]
   - **Impact**: [Expected improvement]
```

### 5. Maintain Functional Equivalence

- The new plan must achieve the same end goal as the original
- Do not remove required functionality
- Do not introduce breaking changes unless explicitly justified
- Preserve compatibility requirements

### 6. Save as V2

- Save the new plan with `-v2` suffix: `YYYY-MM-DD-HHMM-plan-<topic>-v2.md`
- Keep the original plan unchanged
- Reference the original plan in the V2 plan header

### 7. Present Comparison

After writing the V2 plan, provide a summary:

```markdown
## Plan Reimagination Complete

**Original Plan:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-topic.md`
**New Plan (V2):** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-topic-v2.md`

**Key Optimizations:**

1. **Algorithmic**: [Brief description]
2. **Data Structures**: [Brief description]
3. **Patterns**: [Brief description]
4. **Simplification**: [Brief description]

**Expected Benefits:**
- Performance: [Expected improvement]
- Maintainability: [Expected improvement]
- Robustness: [Expected improvement]

**Recommendation:** Use V2 plan for implementation.
```
