# Always Do

## Mandatory Actions

**YOU MUST:**

1. **Ask clarifying questions when requirements are ambiguous**
   - Verify your understanding before proposing designs
   - Present design options and get user confirmation
   - Confirm plan structure before writing detailed phases
   - Only proceed directly if requirements are completely unambiguous

2. **Read Memory Bank files at the start**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns
   - Read `llm_docs/memory/techContext.md` for technical context

3. **Read all provided inputs fully**
   - Read the entire research document before any analysis
   - Read all explicitly mentioned files in their entirety
   - Never skip or partially read any provided input
   - Verify research findings by reading referenced files

4. **Use file references only (no code blocks)**
   - Reference local file paths with line ranges only
   - Format: `path/to/file.py:10-25` — brief description
   - Do not include code blocks in the plan output

5. **Follow the interactive planning process**
   - Phase 1: Context gathering and understanding verification
   - Phase 2: Design options and approach selection
   - Phase 3: Plan structure approval
   - Phase 4: Detailed plan writing

6. **Write measurable success criteria**
   - Include automated checks (ruff, pytest, type checking)
   - Include manual verification steps
   - Make criteria specific and testable

7. **Output to the correct location**
   - Location: `llm_docs/plans/`
   - Filename: `YYYY-MM-DD-HHMM-plan-<kebab-topic>.md`
   - Format: Markdown with references only (no code blocks, no frontmatter)

8. **Update Memory Bank after completion**
   - Add design decisions to `llm_docs/memory/activeContext.md`
   - Document patterns to follow in `llm_docs/memory/systemPatterns.md`
