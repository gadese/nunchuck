# Research Phase Only

Execute only the research phase to document current codebase state.

## When to Use

Use this pipeline when you need to:
- Explore and document a specific area of the codebase
- Understand current implementation before planning changes
- Create technical documentation for future reference
- Analyze patterns and architecture without committing to implementation

## Process

### Phase 1: Research
**Skill:** `rpi-research`

**Objective:** Document the current state of the codebase relevant to the task.

**Steps:**
1. **Read Memory Bank**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

2. **Clarify Scope (if needed)**
   - Apply clarification protocol if research scope is ambiguous
   - Ask 2-4 focused questions covering scope, depth, focus, boundaries
   - Wait for user answers before proceeding

3. **Read Explicitly Mentioned Files**
   - Read any user-specified files fully before broader exploration

4. **Analyze and Decompose**
   - Break down research question into composable areas
   - Identify relevant components, patterns, or concepts

5. **Parallel Exploration**
   - Use parallel codebase scans (search, find, grep)
   - Prioritize backend, models/inference, frontend integration, data contracts
   - Read necessary code to confidently describe what exists

6. **Synthesis (Descriptive Only)**
   - Document current state: components, purpose, data flows
   - Highlight contract mismatches and note assumptions/unknowns
   - Provide references only (file paths with line ranges)

7. **Output Document**
   - Location: `llm_docs/research/`
   - Filename: `YYYY-MM-DD-HHMM-research-<kebab-topic>.md`
   - No frontmatter, concise but complete

8. **Update Memory Bank**
   - Add key findings to `llm_docs/memory/activeContext.md`

**Output:** Research document with findings, architecture documentation, and references

**⏸️ PAUSE POINT:** Present research findings summary to user. Research phase complete.

---

## Output Format

The research document follows this structure:

```markdown
# Research — [Topic]

**Tags**: [taxonomy tags]

## 1. Research Question
Plain restatement of the user's question after clarification

## 2. System Context Overview
Brief high-level context and architectural patterns

## 3. Findings by Area
### Backend
### Models / Inference / Pre- & Post-processing
### Frontend Integration
### Data Contracts / API Schemas
[Additional areas as needed]

## 4. Architecture Documentation
Current patterns, conventions, design implementations

## 5. Contract Mismatches (Checklist)
Async/sync mismatches, schema mismatches, etc.

## 6. Assumptions & Unknowns
Assumptions made and open questions

## 7. References
File paths with line ranges and descriptions
```

---

## Quick Reference

**Invoking research only:**
```
/rpi-research

Research question: [what you want to understand]
Scope: [areas to focus on]
Depth: [high-level or detailed]
```

---

## Next Steps

After research is complete, you can:
1. Use findings to inform manual planning
2. Invoke `/rpi-plan` with research document to create implementation plan
3. Archive research for future reference
