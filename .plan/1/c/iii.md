# Task C.iii: Implement auto-detection logic

## Focus
Detect IDE and generate appropriate adapters

## Inputs
- AdapterGenerator from C.i and C.ii
- Project directory structure
- IDE configuration file patterns

## Work
1. Implement IDE detection (check .windsurf/, .cursor/)
2. Create `nunchuck adapter` auto-detect command
3. Handle multiple IDEs in same project
4. Add explicit flags (--windsurf, --cursor)
5. Manage adapter updates and conflicts
6. Test auto-detection scenarios
