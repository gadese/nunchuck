# Task A.i: Set up Python package structure

## Focus
Configure pyproject.toml for global installation and dependency management

## Inputs
- Current pyproject.toml
- src/nunchuck/ directory structure
- Existing CLI entry point

## Work
1. Update pyproject.toml with global installation configuration
2. Ensure src/nunchuck/cli.py is properly configured as entry point
3. Add required dependencies (PyYAML, click, etc.)
4. Test local installation with `pip install -e .`
5. Verify `nunchuck` command is available after install
