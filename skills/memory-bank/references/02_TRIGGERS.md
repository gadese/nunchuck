# Triggers

## When to Read Memory Bank

Read relevant Memory Bank files in these situations:

### 1. At the Start of Every Session
- **Files to read**: `memory-index.md`, `activeContext.md`
- **Purpose**: Understand where work left off and current focus

### 2. Before Starting Implementation
- **Files to read**: `projectbrief.md`, `systemPatterns.md`, `techContext.md`
- **Purpose**: Understand requirements, patterns, and technical context

### 3. When User Mentions Context
- **Triggers**: User says "context", "where we left off", "what were we doing"
- **Files to read**: `activeContext.md`, `progress.md`
- **Purpose**: Provide continuity from previous sessions

### 4. When Making Architectural Decisions
- **Files to read**: `systemPatterns.md`, `productContext.md`
- **Purpose**: Ensure consistency with established patterns and rationale

### 5. When Encountering Unfamiliar Code
- **Files to read**: `techContext.md`, `systemPatterns.md`
- **Purpose**: Understand technical context and architectural patterns

### 6. Before Implementation Work
- **Files to read**: `codeInventory.md`
- **Purpose**: Understand existing classes, interfaces, and functions before adding or modifying code

## When to Update Memory Bank

Update Memory Bank files in these situations:

### 1. After Significant Work (activeContext.md)
Update after:
- Completing a phase of work
- Discovering important information
- Making key decisions
- Encountering blockers
- Changing direction

### 2. Feature Completion (progress.md)
Update when:
- Completing features or tasks
- Starting new features
- Marking items as blocked

### 3. Architectural Changes (systemPatterns.md)
Update when:
- Establishing new architectural patterns
- Making significant design decisions
- Refactoring major components

### 4. Technical Changes (techContext.md)
Update when:
- Adding new dependencies
- Changing API contracts
- Modifying database schema
- Updating environment configuration

### 5. Feature Clarification (productContext.md)
Update when:
- Clarifying feature requirements
- Understanding new business logic
- Documenting user stories

### 6. Requirement Changes (projectbrief.md)
Update when:
- Project requirements change
- Definition of done is clarified
- Success criteria are modified

### 7. At End of Work Sessions
- **Files to update**: `activeContext.md`, `progress.md`
- **Purpose**: Capture current state for next session

### 8. When Context Changes Significantly
- **Files to update**: Multiple files as appropriate
- **Purpose**: Maintain accurate project state

### 9. On Every Memory Bank Update (changeLog.md)
- **Files to update**: `changeLog.md`
- **Purpose**: Maintain chronological record of all Memory Bank changes

### 10. After Adding/Removing/Renaming Code Elements (codeInventory.md)
Update when:
- Adding, removing, or renaming classes or interfaces
- Adding, removing, or renaming public functions
- Review at end of major implementation phases

### 11. When Creating Archives (changeLog-index.md)
- **Files to update**: `changeLog-index.md`
- **Purpose**: Index new archive files with date ranges and topics covered
