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
