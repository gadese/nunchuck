# Always Do

## Mandatory Actions

**YOU MUST:**

1. **Ask clarifying questions when the plan is ambiguous**
   - Apply the clarification protocol from 02_TRIGGERS.md
   - Wait for user answers before proceeding
   - Only proceed directly if the plan is complete and unambiguous

2. **Read Memory Bank files at the start**
   - Read `llm_docs/memory/activeContext.md` for current context
   - Read `llm_docs/memory/systemPatterns.md` for existing patterns

3. **Read the plan completely before starting**
   - Identify all phases, success criteria, and file references
   - Note any existing checkmarks indicating prior progress
   - Understand the dependencies between phases

4. **Read all referenced files**
   - Read every file mentioned in the plan fully (no offset/limit)
   - Verify the current state matches what the plan expects
   - Note any discrepancies for mismatch evaluation

5. **Update plan checkboxes after completing each phase**
   - Mark items as complete using `- [x]`
   - Add brief notes if you made adaptations

6. **Run verification commands before moving to the next phase**
   - Execute automated checks specified in success criteria
   - Verify manual criteria as specified
   - Do not proceed with failing tests

7. **Report progress with quantitative measurements**
   - Brief summaries after each phase
   - Include pass/fail status of verification steps
   - Note any deviations from the plan

8. **Update Memory Bank after completion**
   - Update `llm_docs/memory/activeContext.md` with completion status
   - Update `llm_docs/memory/progress.md` with completed work

9. **Follow existing codebase patterns**
   - Respect workspace rules (code principles, style guides)
   - Use type hints consistently
   - Keep changes minimal and focused
