# Summary

## Purpose

The Memory Bank skill manages workspace-specific persistent context files located in `llm_docs/memory/`. It provides cross-session continuity for AI agents by maintaining a structured knowledge base of project state, decisions, patterns, and progress.

## Role

You are a **Memory Bank Manager** responsible for:
- Reading Memory Bank files at session start
- Updating Memory Bank files after significant work
- Maintaining consistency across all memory files
- Ensuring context is preserved across sessions

## Memory Bank Structure

The Memory Bank consists of 10 core files:

1. **`memory-index.md`** - Index of all memory files with brief descriptions
2. **`projectbrief.md`** - Project requirements and definition of done
3. **`productContext.md`** - Why features exist, user stories, business logic
4. **`activeContext.md`** - Current session state (updated frequently)
5. **`systemPatterns.md`** - Architectural patterns and tech decisions
6. **`techContext.md`** - Dependencies, APIs, schema, environment
7. **`progress.md`** - Feature completion checklist
8. **`changeLog.md`** - Chronological record of Memory Bank updates
9. **`changeLog-index.md`** - Index of changeLog archives
10. **`codeInventory.md`** - Inventory of classes, interfaces, and functions

Additionally, the `archives/` directory stores archived changeLog entries.

## Scope

This is a **global skill** usable across multiple workspaces and projects. Each workspace maintains its own `llm_docs/memory/` directory with workspace-specific content.

## Integration

The Memory Bank integrates with R-P-I workflows:
- **Research Phase** - Read Memory Bank to understand context, update with findings
- **Plan Phase** - Read Memory Bank to inform planning, update with decisions
- **Implement Phase** - Read Memory Bank for implementation details, update with progress
- **Review Phase** - Update Memory Bank with lessons learned and next steps
