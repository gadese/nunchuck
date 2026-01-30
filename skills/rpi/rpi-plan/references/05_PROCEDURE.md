# Procedure

## Planning Process

Follow these phases in order:

### Phase 1: Context Gathering & Initial Analysis

1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

2. **Understand the Research Document**
   - The research document is your primary source of truth
   - Read the entire research document before any other action
   - Identify all findings, constraints, and architectural patterns documented
   - Note contract mismatches, assumptions, and unknowns flagged by the research
   - Use the research as the foundation for all planning decisions

3. **Read All Additional Inputs Fully**
   - Read all explicitly mentioned files in their entirety
   - Read any JSON/data files referenced
   - Never skip or partially read any provided input

4. **Explore the Codebase (guided by research)**
   - Find relevant source files, configs, and tests identified in the research
   - Verify the research findings by reading the referenced files
   - Trace data flows and key functions mentioned in the research
   - Document any additional findings with file:line references

5. **Verify Understanding**
   - Cross-reference task requirements with research findings and actual code
   - Identify discrepancies between research and current codebase state
   - Note assumptions requiring verification

6. **Synthesize and Clarify**
   - **CRITICAL**: Present your understanding and ask clarifying questions
   - Structure:
     ```
     Based on the research and my codebase analysis, I understand we need to [accurate summary].

     **Current State:**
     - [Implementation detail with file:line reference]
     - [Relevant pattern or constraint discovered]
     - [Potential complexity or edge case identified]

     **Questions requiring clarification:**
     - [Technical question that requires human judgment]
     - [Business logic clarification]
     - [Design preference that affects implementation]
     ```
   - Only ask questions you genuinely cannot answer through code investigation
   - If no ambiguities exist, proceed to Phase 2

⏸️ **PAUSE**: Wait for user clarification before proceeding to Phase 2

### Phase 2: Research & Discovery

1. **Handle Corrections**
   - If the user corrects any misunderstanding:
   - DO NOT accept corrections blindly
   - Verify by reading the specific files/directories mentioned
   - Only proceed once facts are confirmed

2. **Propose Design Options**
   - Present 2-3 viable approaches
   - Structure:
     ```
     **Option A: [Name]**
     - Approach: [Description]
     - Pros: [Benefits]
     - Cons: [Drawbacks]
     - References: `path/to/file.py:10-50`

     **Option B: [Name]**
     - Approach: [Description]
     - Pros: [Benefits]
     - Cons: [Drawbacks]
     - References: `path/to/file.py:60-100`

     **Recommendation:** [Option] because [rationale]

     Which approach aligns best with your vision?
     ```

3. **Converge on Approach**
   - Address flaws and edge cases
   - Get explicit confirmation before proceeding

⏸️ **PAUSE**: Wait for approach confirmation before proceeding to Phase 3

### Phase 3: Plan Structure Development

Present a phased outline for approval:

```
## Proposed Plan Structure

**Overview:** [1-2 sentence summary of what we're building]

**Phases:**
1. [Phase name] — [What it accomplishes]
2. [Phase name] — [What it accomplishes]
3. [Phase name] — [What it accomplishes]

Does this phasing make sense? Should I adjust the order or granularity?
```

⏸️ **PAUSE**: Wait for structure approval before proceeding to Phase 4

### Phase 4: Detailed Plan Writing

Produce the final plan document following this template:

```markdown
# Implementation Plan — [Topic]

**Tags:** [select from taxonomy]

## 1. Overview
Brief description of what we're implementing and why.

## 2. Current State Summary
What exists now and key constraints discovered:
- `path/to/file.py:10-25` — Description of what those lines implement
- `path/to/another.py:40-67` — Description

## 3. Desired End State
Statement of the desired outcome and how it will be verified.

## 4. Key Discoveries
- Important finding with `file:line` reference
- Pattern to follow
- Constraint to work within

## 5. Design Decision
- **Chosen Approach:** [Name]
- **Rationale:** [Why this approach was selected]
- **Alternatives Considered:** [Brief mention of other options]

## 6. Out of Scope
Explicit items we are NOT doing to prevent scope creep:
- [Item 1]
- [Item 2]

## 7. Implementation Phases

### Phase 1: [Descriptive Name]
**Complexity:** S/M/L

**Objective:** What this phase achieves

**Changes by Component:**
- `path/to/backend/file.py:100-140` — Summary of change
- `path/to/tests/test_file.py:50-80` — Summary of test changes

**Implementation Steps:**
1. [Clear action]
2. [Clear action]
3. [Clear action]

**Success Criteria:**
- Automated:
  - [ ] ruff check/format passes
  - [ ] pytest suite passes
  - [ ] type checking passes (pyright)
- Manual:
  - [ ] [Specific behavior validated]
  - [ ] [Edge case verified]

**Dependencies:** [If any]

### Phase 2: [Descriptive Name]
[Same structure as Phase 1]

## 8. Risks & Mitigations
| Risk | Impact | Mitigation |
|------|--------|------------|
| [Risk 1] | [Impact] | [Mitigation strategy] |

## 9. References
- Research: `llm_docs/research/[file].md`
- Similar implementation: `path/to/file.py:line-range`
```

### Phase 5: Final Handoff

1. Present the plan summary in chat
2. Confirm the document location and filename
3. Update Memory Bank: Add design decisions to `llm_docs/memory/activeContext.md`
4. Remind: The next agent (implementation phase) will execute this plan

## Tags Taxonomy

- **AI-specific:** `models`, `inference`, `training`, `preprocessing`, `postprocessing`, `metrics`
- **App areas:** `backend`, `frontend`, `data-contracts`, `api`, `ui-integration`
- **Optional:** `image-processing`, `text-nlp`, `vector-search`, `scheduling`, `refactoring`, `testing`

## Common Implementation Patterns

**Database Changes:**
1. Schema/migration → 2. Store methods → 3. Business logic → 4. API endpoints → 5. Clients

**New Features:**
1. Research existing patterns → 2. Data model → 3. Backend logic → 4. API endpoints → 5. UI (if applicable)

**Refactoring:**
1. Document current behavior → 2. Plan incremental changes → 3. Maintain backwards compatibility → 4. Migration strategy
