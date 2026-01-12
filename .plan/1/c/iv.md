# Task C.iv: Add adapter management commands

## Focus
Integrate adapter commands into CLI

## Inputs
- AdapterGenerator from C.iii
- Command dispatcher from A.iii
- Project skill configuration

## Work
1. Implement `nunchuck adapter` command group
2. Add `nunchuck adapter --clean` to remove adapters
3. Add `nunchuck adapter --list` to show status
4. Handle adapter regeneration on skill changes
5. Integrate with project skill list
6. Test adapter lifecycle management
