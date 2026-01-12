---
status: complete
---

# Task B.ii: Implement skill addition logic

## Focus
Add skills to global store from local paths or remote URLs

## Inputs
- Store class from B.i
- Existing install logic
- Skill validation from A.iv

## Work
1. Implement `nunchuck add <path>` command
2. Support local directory paths
3. Add remote URL support (git clone functionality)
4. Validate skill before adding
5. Create skill metadata index
6. Handle duplicate skill names
7. Test with various skill sources

## Output

- Enhanced `Store.add_skill()` method:
  - Accepts both local paths and remote URLs
  - Validates skills against Agent Skills spec before adding
  - Clones remote repositories using git
  - Cleans up temporary directories after cloning
  - Handles duplicate skill names with clear error messages
- Updated CLI integration:
  - Removed path validation to allow remote URLs
  - `--remote` flag kept for compatibility
  - `--name` option for custom skill names
  - Proper error reporting for validation failures
- Successfully tested:
  - Adding local skills with validation (doctor skill passed)
  - Adding skills with custom names
  - Validation failures show detailed errors (prompt skill missing pipelines)
  - Dry-run mode works for remote URLs
  - Skill metadata properly stored in index

## Handoff

Skill addition logic is fully implemented with local and remote support, validation, and proper error handling. The store now validates skills before adding them and provides clear feedback on failures. Proceed to Task B.iii to implement skill removal logic with dependency awareness.
