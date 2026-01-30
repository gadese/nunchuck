# Failures

## Handling Failures

### When Research Scope is Too Broad
- **Symptom**: User request covers too many areas or lacks clear boundaries
- **Action**: Apply clarification protocol from 02_TRIGGERS.md
- **Recovery**: Ask focused questions to narrow scope before proceeding

### When Files Don't Exist
- **Symptom**: Referenced files or directories cannot be found
- **Action**: Document the missing files in "Assumptions & Unknowns" section
- **Recovery**: Ask user to verify paths or provide correct locations

### When Code is Unclear or Ambiguous
- **Symptom**: Implementation details are difficult to understand
- **Action**: Document what you can observe and note the ambiguity
- **Recovery**: Add to "Assumptions & Unknowns" section with specific questions

### When Sensitive Data is Encountered
- **Symptom**: Config files, secrets, or credentials found
- **Action**: Reference their presence and paths only
- **Recovery**: Do not echo contents; note their location in the research document

### When Large Assets are Encountered
- **Symptom**: Data dumps, images, archives in scope
- **Action**: Skip unless explicitly requested
- **Recovery**: Note their presence and location without reading contents

### When Contract Mismatches are Found
- **Symptom**: Inconsistencies between components (async/sync, types, schemas)
- **Action**: Document in "Contract Mismatches" checklist section
- **Recovery**: Provide file references for each mismatch found

### When Memory Bank Files Don't Exist
- **Symptom**: `llm_docs/memory/` files are missing
- **Action**: Proceed with research but note the absence
- **Recovery**: Create basic Memory Bank entries after research completion

## Artifact Validation

Before completing research:
- [ ] Output file created in `llm_docs/research/`
- [ ] Filename follows format: `YYYY-MM-DD-HHMM-research-<kebab-topic>.md`
- [ ] No frontmatter in document
- [ ] No code blocks included (references only)
- [ ] All file references include line ranges
- [ ] Contract mismatches checklist completed
- [ ] Assumptions & unknowns documented
- [ ] Memory Bank updated with key findings
