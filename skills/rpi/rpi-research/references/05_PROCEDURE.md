# Procedure

## Research Process

Follow these steps in order:

### Step 1: Read Memory Bank
- Read `llm_docs/memory/activeContext.md` for current context
- Read `llm_docs/memory/systemPatterns.md` for existing patterns
- Read `llm_docs/memory/techContext.md` for technical context

### Step 2: Clarify (if needed)
- **CRITICAL**: Apply the clarification protocol if the request is ambiguous
- Ask 2-4 focused questions about scope, depth, focus, and boundaries
- Wait for user answers before proceeding
- If specific files are mentioned and scope is clear, proceed to Step 3

### Step 3: Read Explicitly Mentioned Files
- Read any user-specified files fully before broader exploration
- Use complete file reads (no offset/limit) for full context

### Step 4: Analyze and Decompose the Research Question
- Break down the user's query into composable research areas
- Take time to deeply reason about the underlying patterns, connections, and architectural implications
- Identify specific components, patterns, or concepts to investigate
- Consider which directories, files, or architectural patterns are relevant

### Step 5: Internal Task Tracking
- Maintain an internal checklist of areas to investigate
- Track findings as you go (do not include this in the output document)

### Step 6: Parallel Exploration (after Step 3)
- Use parallel codebase scans (search, find, grep) to locate relevant symbols and files
- Prioritize the focus areas listed in 01_SUMMARY.md
- Read only the necessary code to confidently describe what exists
- Prioritize breadth over depth initially, then drill down as needed

### Step 7: Synthesis (Descriptive Only)
- Document the current state: components, purpose, and how data flows between them
- Highlight contract mismatches (see checklist in output template)
- Note assumptions/unknowns when gaps remain
- Do not include code blocks; provide references only (local file paths with line ranges)

### Step 8: Output Document
- One document per research task
- Location: `llm_docs/research/`
- Filename: `YYYY-MM-DD-HHMM-research-<kebab-topic>.md`
- No frontmatter
- Keep the content concise but complete for downstream LLM planning

### Step 9: Diagrams (Gated)
- If a diagram would significantly improve understanding, ask for confirmation first
- Provide a one-line justification before producing any diagram

### Step 10: Final Handoff
1. Present a brief "Findings Summary" in chat with key file references
2. Ask if a diagram would be helpful (with one-line justification)
3. Confirm the document location and filename
4. Update Memory Bank: Add key findings to `llm_docs/memory/activeContext.md`
5. Remind: The next agent (planning phase) will use this document—do not include plans or recommendations

## Output Document Template

```markdown
# Research — [Topic]

**Tags**: [select from taxonomy, extend as needed]

## 1. Research Question
- Plain restatement of the user's question after clarification

## 2. System Context Overview
- Brief high-level context of the examined areas
- Architectural patterns observed

## 3. Findings by Area

### Backend
- What exists, where, and how it behaves
- References only: `path/to/file.py:10-25` — what those lines implement

### Models / Inference / Pre- & Post-processing
- Model loading, inference entry points, pre/post steps, local artifact paths (paths only)
- References only with line ranges

### Frontend Integration
- Where AI features surface, API calls, state management touchpoints
- References only with line ranges

### Data Contracts / API Schemas
- Request/response structures, validators, serializers, typing
- References only with line ranges

### [Additional Component/Area as needed]
- Description of what exists
- File references: `path/to/file.py:10-25` — brief description
- How it connects to other components
- Current implementation details (without evaluation)

## 4. Architecture Documentation
- Current patterns, conventions, and design implementations found
- Integration points and boundaries

## 5. Contract Mismatches (Checklist)
- [ ] Async vs Sync mismatches across boundaries (handlers/services/mocks)
- [ ] Request/response schema mismatches between server and client
- [ ] Return type/shape discrepancies
- [ ] Error/exception contract inconsistencies
- Include references only (local path + line ranges) for each item found

## 6. Assumptions & Unknowns
- Assumptions made due to incomplete information
- Open questions that would resolve gaps

## 7. References
- `path/to/file.py:123-147` — Brief description
- `path/to/other.tsx:45-62` — Brief description
```

## Tags Taxonomy (extend as needed)

- **AI/ML**: `models`, `inference`, `training`, `preprocessing`, `postprocessing`, `metrics`
- **Application**: `backend`, `frontend`, `data-contracts`, `api`, `ui-integration`
- **Domain**: `image-processing`, `text-nlp`, `vector-search`, `scheduling`, `auth`, `data-pipeline`
