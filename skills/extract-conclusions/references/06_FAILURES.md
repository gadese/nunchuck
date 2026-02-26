---
description: Failure conditions and recovery strategies for the extract-conclusions skill.
index:
  - Handling Failures
  - Artifact Validation
---

# Failures

## Handling Failures

### When Source Files Are Missing or Unreadable
- **Symptom**: Referenced notebooks or documents cannot be found or parsed
- **Action**: Report which files failed and why
- **Recovery**: Ask user to verify paths; proceed with available files if partial set

### When Notebooks Lack Clear Results
- **Symptom**: Notebook cells have no outputs, metrics are missing, or results are incomplete
- **Action**: Document what is available; note missing outputs explicitly
- **Recovery**: Add to "Limitations & Open Questions" with specific cells that lack results

### When Metrics Are Ambiguous or Inconsistent
- **Symptom**: Same metric reported with different values across cells, unclear units, or conflicting results
- **Action**: Report the inconsistency with exact source references for each value
- **Recovery**: Present both values and flag the discrepancy; do not silently pick one

### When Experimental Context Is Missing
- **Symptom**: No problem statement, motivation, or methodology documented in source
- **Action**: Extract what is available; note the context gap
- **Recovery**: Ask user for project context if critical to producing useful conclusions

### When Source Scope Is Too Broad
- **Symptom**: User provides many notebooks spanning unrelated experiments
- **Action**: Apply clarification protocol from 02_TRIGGERS.md
- **Recovery**: Ask user to narrow scope or group related experiments

### When Memory Bank Files Don't Exist
- **Symptom**: `llm_docs/memory/` files are missing
- **Action**: Proceed with extraction but note the absence
- **Recovery**: Create basic Memory Bank entries after completion

## Artifact Validation

Before completing conclusions:
- [ ] Output file created in `llm_docs/conclusions/`
- [ ] Filename follows format: `YYYY-MM-DD-HHMM-conclusions-<kebab-topic>.md`
- [ ] No frontmatter in the output document
- [ ] No raw code blocks from notebooks (references only)
- [ ] Every metric and finding has a source reference
- [ ] Confidence levels assigned to all major conclusions
- [ ] Limitations and open questions documented
- [ ] Memory Bank updated with key conclusions
