# Task D.ii: Update list command for dual scope

## Focus
Support both global and project listing

## Inputs
- Existing list command
- Global store from B
- Project configuration from D.i

## Work
1. Modify `nunchuck list` to show project skills by default
2. Add `--global` flag for global store listing
3. Show skill source (global/project) in output
4. Add filtering options for both scopes
5. Handle combined view with --all flag
6. Test all listing modes
