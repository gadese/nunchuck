---
status: complete
---

# Task B.i: Create global store directory structure

## Focus
Establish ~/.nunchuck/skills/ as read-only global store

## Inputs
- Existing installer.py logic
- Filesystem permission requirements
- Cross-platform path handling

## Work
1. Create Store class to manage ~/.nunchuck/skills/
2. Implement auto-creation on first access
3. Set appropriate read-only permissions for skill directories
4. Add store initialization check in CLI bootstrap
5. Handle cross-platform path differences
6. Test store creation on Unix and Windows

## Output

- Created `src/nunchuck/store.py` with Store class:
  - Manages ~/.nunchuck/skills/ directory structure
  - Auto-creates store on first access
  - Handles skill addition, removal, and listing
  - Sets read-only permissions on Unix-like systems
  - Cross-platform path handling (uses Path.home())
- Integrated Store into CLI:
  - `global- add` command adds skills to store
  - `global- remove` command removes skills with confirmation
  - `global- list --global` lists stored skills
  - Store auto-initializes on CLI bootstrap
- Successfully tested:
  - Store creation at ~/.nunchuck/skills/
  - Adding skills from local paths
  - Listing skills with metadata
  - Removing skills with confirmation
  - Dry-run mode works correctly

## Handoff

Global store directory structure is fully implemented with proper permissions and cross-platform support. The Store class provides a clean API for skill management and is integrated into the CLI commands. Proceed to Task B.ii to implement skill addition logic with remote URL support.
