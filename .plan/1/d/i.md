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
