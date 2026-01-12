---
status: complete
---

# Task D.i: Implement project skill commands (use/drop)

## Focus
Replace install/uninstall with use/drop

## Inputs
- Existing install/uninstall logic
- Project configuration structure
- Global store from B

## Work
1. Implement `nunchuck use <name>` command
2. Create project skill manifest (.nunchuck/skills.yaml)
3. Add skill reference creation (symlink or reference)
4. Implement `nunchuck drop <name>` command
5. Update project configuration on use/drop
6. Test with various project states

## Output

- Created `src/nunchuck/project.py` with Project class:
  - Manages .nunchuck/skills.yaml configuration
  - Creates symlinks (Unix) or junctions (Windows) to global skills
  - Falls back to copy if linking fails
  - Tracks skill metadata in project config
- Implemented CLI commands:
  - `nunchuck project use <name>` adds skill to project
  - `nunchuck project drop <name>` removes skill from project
  - Both commands handle confirmation and dry-run mode
- Successfully tested:
  - Project structure creation (.nunchuck/skills.yaml)
  - Skill usage creates symlink to global store
  - Skill drop removes symlink and updates config
  - Configuration properly tracks skills

## Handoff

Project skill commands (use/drop) are fully implemented, replacing the old install/uninstall paradigm. Skills are now referenced from the global store rather than copied into projects. Proceed to Task D.ii to update command help and terminology.
