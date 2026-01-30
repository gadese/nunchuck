# Never Do

## Prohibited Actions

**YOU MUST NOT:**

1. **Make code changes or diffs in this step**
   - You produce plans, not implementations
   - Leave code changes to the implementation phase

2. **Include code blocks in the plan output**
   - Use file references with line ranges only
   - Format: `path/to/file.py:10-25` — description

3. **Echo secrets or config contents**
   - Reference their paths only
   - Do not include sensitive data in the plan

4. **Leave open questions in the final plan**
   - Resolve all ambiguities before finalizing
   - Ask clarifying questions during the planning process
   - The final plan must be unambiguous and ready for execution

5. **Skip the interactive planning process**
   - Always verify understanding before proposing designs
   - Always present design options before detailing
   - Always get structure approval before writing full plan

6. **Accept corrections blindly**
   - Verify by reading the specific files/directories mentioned
   - Only proceed once facts are confirmed through code investigation

7. **Make assumptions without verification**
   - If you cannot verify something through code, ask
   - Document assumptions clearly if they must be made

8. **Create plans without specific file references**
   - Every change must reference specific files and line ranges
   - Vague plans lead to implementation errors
