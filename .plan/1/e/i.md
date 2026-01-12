# Task E.i: Ensure Windows compatibility

## Focus
Handle Windows-specific filesystem and permission issues

## Inputs
- Current Unix-focused implementation
- Windows filesystem constraints
- Python pathlib documentation

## Work
1. Replace Unix-specific path operations with pathlib
2. Handle Windows permission models
3. Ensure global store works on Windows (AppData)
4. Test symlink alternatives on Windows
5. Handle case-insensitive filesystem issues
6. Verify all commands work on Windows
