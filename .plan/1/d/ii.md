---
status: complete
---

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

## Output

The list command was already updated in Task B.iv:
- `nunchuck global- list --global` shows global store skills
- `nunchuck global- list` shows project skills with source detection
- Added --filter option for name-based filtering
- Formatted table output with proper alignment
- Source column shows "global" or "local"

## Handoff

Dual-scope listing is complete. The list command properly distinguishes between global and project skills with appropriate visual indicators. Proceed to Task D.iii to remove legacy commands.
