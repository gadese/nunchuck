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
