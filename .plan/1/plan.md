# Plan: Nunchuck CLI Consolidation

## Objective

Transform nunchuck from a collection of scripts into a unified, globally-installable CLI tool that manages agent skills with automatic adapter generation.

## Success Criteria

1. CLI installable via `pip install` globally
2. Global skill store at `~/.nunchuck/skills/` auto-created on first use
3. All shell script functionality migrated to Python
4. Adapter generation integrated into CLI
5. Terminology standardized to "skills" (no "packs")
6. Cross-platform support (Unix + Windows)

## Sub-plan Index

- **A** - Core CLI Infrastructure
- **B** - Global Skill Store Implementation  
- **C** - Adapter Generation Migration
- **D** - Command Interface Updates
- **E** - Cross-Platform Support & Testing

## Review

**Date**: 2025-01-12
**Reviewer**: Agent

### Criteria Status

- [ ] 1. CLI installable via `pip install` globally — unmet (no evidence of pyproject.toml updates)
- [ ] 2. Global skill store at `~/.nunchuck/skills/` auto-created on first use — unmet (no Store class implementation)
- [ ] 3. All shell script functionality migrated to Python — unmet (shell scripts still exist)
- [ ] 4. Adapter generation integrated into CLI — unmet (no AdapterGenerator class)
- [ ] 5. Terminology standardized to "skills" (no "packs") — unmet (terminology not updated)
- [ ] 6. Cross-platform support (Unix + Windows) — unmet (pathlib not implemented)

### Strengths

- Comprehensive decomposition of work into logical sub-plans
- Clear task structure with Focus, Inputs, and Work sections
- All necessary components identified for CLI consolidation
- Good separation of concerns (infrastructure, store, adapters, interface, platform)

### Gaps

- No tasks have been executed (all Output sections empty)
- No concrete artifacts produced
- No evidence of any work performed
- Plan exists but implementation not started

### Recommendation

Plan is well-structured and ready for execution. Begin with sub-plan A (Core CLI Infrastructure) to establish the foundation, then proceed sequentially through B-E. Each task should be executed with concrete outputs documented before moving to the next.
