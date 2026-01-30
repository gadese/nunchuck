# Failures

## Handling Failures

### When Requirements are Ambiguous
- **Symptom**: Task description is unclear or has multiple interpretations
- **Action**: Apply clarification protocol from Phase 1
- **Recovery**: Ask focused questions before proposing designs

### When Research Document is Missing or Incomplete
- **Symptom**: Referenced research document doesn't exist or lacks key information
- **Action**: Request the research document path or ask for missing information
- **Recovery**: Cannot proceed without research foundation

### When Design Options are Unclear
- **Symptom**: Multiple viable approaches with no clear winner
- **Action**: Present all options with pros/cons to user
- **Recovery**: Get explicit user preference before proceeding

### When Files Referenced in Research Don't Exist
- **Symptom**: Research references files that are no longer present
- **Action**: Verify current codebase state and note discrepancies
- **Recovery**: Update plan to reflect actual file locations

### When User Provides Incorrect Information
- **Symptom**: User correction conflicts with actual code
- **Action**: Verify by reading the specific files mentioned
- **Recovery**: Present findings and ask for clarification

### When Plan Structure Needs Adjustment
- **Symptom**: User feedback indicates phasing is wrong
- **Action**: Revise structure based on feedback
- **Recovery**: Re-present structure for approval

### When Success Criteria are Unmeasurable
- **Symptom**: Criteria are too vague or subjective
- **Action**: Make criteria specific and testable
- **Recovery**: Include both automated and manual verification steps

### When Memory Bank Files Don't Exist
- **Symptom**: `llm_docs/memory/` files are missing
- **Action**: Proceed with planning but note the absence
- **Recovery**: Create basic Memory Bank entries after plan completion

## Artifact Validation

Before completing the plan:
- [ ] Output file created in `llm_docs/plans/`
- [ ] Filename follows format: `YYYY-MM-DD-HHMM-plan-<kebab-topic>.md`
- [ ] No frontmatter in document
- [ ] No code blocks included (references only)
- [ ] All file references include line ranges
- [ ] Success criteria are measurable
- [ ] Out-of-scope items explicitly listed
- [ ] Risks and mitigations documented
- [ ] Memory Bank updated with design decisions
- [ ] All ambiguities resolved (no open questions in final plan)
