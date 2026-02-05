# Procedure

## Reimagination Process

Follow these steps in order:

### Step 1: Comprehensive Context Gathering

1. **Read the Original Plan Completely**
   - Understand the objective, current state, and desired end state
   - Note the design decisions and rationale
   - Identify the phases and their dependencies
   - Pay attention to constraints and requirements

2. **Read the Research Document**
   - If available, read the research document that informed the plan
   - Understand the problem space and solution options explored
   - Note any architectural patterns or constraints discovered

3. **Read Review Notes**
   - If the plan has been reviewed, read all review annotations
   - Understand what issues were identified
   - Consider how the V2 plan can address these more elegantly

4. **Read Referenced Code**
   - Read the key files referenced in the plan
   - Understand current patterns and conventions
   - Identify opportunities to leverage existing utilities or patterns

5. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for established patterns
   - Read `llm_docs/memory/techContext.md` for technical context

### Step 2: Identify Optimization Opportunities

Systematically analyze the plan for improvements:

#### Algorithmic Analysis

- **Current Approach**: What algorithm or approach does the plan use?
- **Complexity**: What's the time/space complexity?
- **Alternatives**: Are there better algorithms available?
- **Built-ins**: Can we leverage optimized built-in functions?

**Example Opportunities:**
- Replace nested loops with matrix operations
- Use hash tables (dicts/sets) for O(1) lookups instead of O(n) list scans
- Leverage built-in sorting/searching instead of manual implementation
- Use generators for memory efficiency

#### Data Structure Analysis

- **Current Structures**: What data structures does the plan use?
- **Operations**: What operations are performed most frequently?
- **Optimal Choice**: Is there a better data structure for these operations?

**Example Opportunities:**
- Use sets for membership testing instead of lists
- Use deques for efficient append/pop from both ends
- Use defaultdict to simplify counting/grouping logic
- Use namedtuples or dataclasses for structured data

#### Pattern Analysis

- **Current Patterns**: What coding patterns does the plan use?
- **Clarity**: Is the intent clear?
- **Elegance**: Can we use more elegant patterns?

**Example Opportunities:**
- Replace loops with comprehensions
- Use recursion for naturally recursive problems
- Use functional composition (map, filter, reduce)
- Use context managers for resource management
- Use decorators for cross-cutting concerns

#### Simplification Analysis

- **Complexity**: How complex is the current approach?
- **Nesting**: How deep is the nesting?
- **Redundancy**: Is there duplicated logic?
- **Clarity**: Is the intent immediately clear?

**Example Opportunities:**
- Extract nested logic into well-named functions
- Combine similar operations
- Use early returns to reduce nesting
- Eliminate redundant checks or computations

#### Robustness Analysis

- **Edge Cases**: How are edge cases handled?
- **Error Handling**: Is error handling clean and comprehensive?
- **Defensive Programming**: Are there defensive checks?

**Example Opportunities:**
- Use validation decorators
- Leverage type hints and runtime validation
- Use Option/Result patterns for error handling
- Add defensive checks without cluttering code

#### Readability Analysis

- **Naming**: Are names clear and descriptive?
- **Structure**: Is the code logically organized?
- **Cognitive Load**: How much do you need to hold in your head?

**Example Opportunities:**
- Improve variable and function names
- Restructure for logical flow
- Extract complex expressions into named variables
- Add strategic comments for non-obvious logic

### Step 3: Synthesize the Optimal Approach

1. **Identify the Top 3-5 Optimizations**
   - Focus on high-impact changes
   - Prioritize changes that improve multiple dimensions
   - Consider the effort-to-benefit ratio

2. **Sketch the New Approach**
   - How will the optimized approach work?
   - What are the key differences from V1?
   - What are the benefits and trade-offs?

3. **Verify Feasibility**
   - Check that the optimized approach is actually feasible
   - Verify that required libraries/functions exist
   - Ensure compatibility with existing codebase patterns

### Step 4: Write the V2 Plan from Scratch

1. **Create New Plan File**
   - Filename: `YYYY-MM-DD-HHMM-plan-<topic>-v2.md`
   - Start with a blank document

2. **Write Plan Header**
   ```markdown
   # Implementation Plan — [Topic] (V2 - Optimized)

   **Tags:** [same as V1]
   **Original Plan:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-topic.md`
   **Optimization Focus:** [Brief description of optimization goals]
   ```

3. **Write Each Section Fresh**

   **Section 1: Overview**
   - Rewrite the overview incorporating the optimized approach
   - Keep it concise and clear

   **Section 2: Current State Summary**
   - Same as V1 unless new insights discovered
   - Add any additional relevant findings

   **Section 3: Desired End State**
   - Same functional goal as V1
   - May describe implementation differently

   **Section 4: Key Discoveries**
   - Include discoveries from V1
   - Add any new insights from reimagination process

   **Section 5: Design Decision**
   - Describe the optimized approach
   - Explain why it's better than V1
   - Mention V1 approach as an alternative considered

   **Section 6: Out of Scope**
   - Same as V1 unless scope changes

   **Section 7: Implementation Phases**
   - Rewrite phases incorporating optimizations
   - May have different phasing if approach is significantly different
   - Ensure each phase is clear and actionable
   - Include specific file references and line ranges
   - Define success criteria

   **Section 8: Optimizations from V1** (NEW)
   - Document key optimizations
   - Explain rationale for each
   - Describe expected benefits

   **Section 9: Risks & Mitigations**
   - Update based on new approach
   - Add any new risks introduced by optimizations

   **Section 10: References**
   - Include all references from V1
   - Add any new references

4. **Ensure Completeness**
   - Verify all sections are present
   - Ensure all file references include line ranges
   - Check that success criteria are measurable
   - Confirm dependencies are listed

### Step 5: Present the V2 Plan

Provide a summary in chat:

```markdown
## Plan Reimagination Complete

**Original Plan:** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-topic.md`
**New Plan (V2):** `llm_docs/plans/YYYY-MM-DD-HHMM-plan-topic-v2.md`

**Key Optimizations:**

1. **Algorithmic Efficiency**
   - V1: [Original approach]
   - V2: [Optimized approach]
   - Impact: [Expected improvement]

2. **Data Structures**
   - V1: [Original structures]
   - V2: [Optimized structures]
   - Impact: [Expected improvement]

3. **Code Patterns**
   - V1: [Original patterns]
   - V2: [Optimized patterns]
   - Impact: [Expected improvement]

4. **Simplification**
   - V1: [Original complexity]
   - V2: [Simplified approach]
   - Impact: [Expected improvement]

**Expected Benefits:**
- **Performance**: [Quantitative or qualitative improvement]
- **Maintainability**: [How it's easier to maintain]
- **Robustness**: [How it's more robust]
- **Readability**: [How it's clearer]

**Trade-offs:**
- [Any trade-offs made, if applicable]

**Recommendation:** Use V2 plan for implementation.

**Next Steps:**
1. Review the V2 plan
2. Confirm the optimizations align with your goals
3. Proceed to implementation with V2 plan
```

### Step 6: Wait for User Response

- Do not automatically proceed to implementation
- Wait for user to review and approve the V2 plan
- Be ready to explain any optimization in more detail
- Be ready to adjust if user prefers V1 approach for certain aspects

## Example Optimization Patterns

### Pattern 1: Loop to Comprehension

**V1:**
```python
results = []
for item in items:
    if item.is_valid():
        results.append(item.transform())
```

**V2:**
```python
results = [item.transform() for item in items if item.is_valid()]
```

### Pattern 2: Nested Loops to Matrix Operation

**V1:**
```python
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[i][j] = matrix[i][j] * 2
```

**V2:**
```python
result = matrix * 2  # NumPy vectorization
```

### Pattern 3: Manual Search to Set Lookup

**V1:**
```python
def is_valid(item, valid_items):
    for valid in valid_items:
        if item == valid:
            return True
    return False
```

**V2:**
```python
valid_set = set(valid_items)
def is_valid(item, valid_set):
    return item in valid_set
```

### Pattern 4: Nested If to Early Return

**V1:**
```python
def process(data):
    if data is not None:
        if len(data) > 0:
            if data.is_valid():
                return data.transform()
    return None
```

**V2:**
```python
def process(data):
    if data is None or len(data) == 0:
        return None
    if not data.is_valid():
        return None
    return data.transform()
```

### Pattern 5: Manual Iteration to Built-in

**V1:**
```python
max_value = items[0]
for item in items[1:]:
    if item > max_value:
        max_value = item
```

**V2:**
```python
max_value = max(items)
```
