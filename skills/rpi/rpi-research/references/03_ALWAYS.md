# Always Do

## Mandatory Actions

**YOU MUST:**

1. **Ask clarifying questions when scope is ambiguous**
   - Apply the clarification protocol from 02_TRIGGERS.md
   - Wait for user answers before proceeding
   - Only proceed directly if the request is narrowly defined and unambiguous

2. **Read Memory Bank files at the start**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

3. **Describe what exists, where it exists, how it works, and how components connect**
   - Create a technical map/documentation of the existing system
   - Document the current state: components, purpose, and data flows
   - Highlight contract mismatches and note assumptions/unknowns when gaps remain

4. **Use file references only (no code blocks)**
   - Use local file paths with line ranges for references
   - Format: `path/to/file.py:10-25` — brief description
   - Do not include code blocks from files in the output

5. **Output to the correct location**
   - One document per research task
   - Location: `llm_docs/research/`
   - Filename: `YYYY-MM-DD-HHMM-research-<kebab-topic>.md`
   - No frontmatter in the output document

6. **Update Memory Bank after completion**
   - Add key findings to `llm_docs/memory/activeContext.md`
   - Document patterns discovered in `llm_docs/memory/systemPatterns.md`
