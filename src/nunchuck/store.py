"""Global skill store management."""

import json
import os
import platform
import shutil
import stat
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

import click
import yaml

from .frontmatter import read_frontmatter
from .validation import validate_target


class StoreError(Exception):
    """Store-related errors."""
    pass


class Store:
    """Manages the global nunchuck skill store."""
    
    def __init__(self, base_path: Optional[Path] = None):
        """Initialize store.
        
        Args:
            base_path: Custom base path for testing (defaults to ~/.nunchuck)
        """
        if base_path:
            self.base_path = base_path
        else:
            # Use platform-specific home directory
            home = Path.home()
            self.base_path = home / ".nunchuck"
        
        self.skills_dir = self.base_path / "skills"
        self.index_file = self.base_path / "index.json"
    
    def ensure_exists(self) -> None:
        """Create store directory structure if it doesn't exist."""
        try:
            # Create base directory
            self.base_path.mkdir(exist_ok=True, mode=0o755)
            
            # Create skills directory
            self.skills_dir.mkdir(exist_ok=True, mode=0o755)
            
            # Create empty index if it doesn't exist
            if not self.index_file.exists():
                self._save_index({"skills": {}, "version": "1.0"})
            
            # Set read-only on skills directory for others
            if platform.system() != "Windows":
                # Unix-like systems
                current_mode = self.skills_dir.stat().st_mode
                # Owner: rwx, Group: r-x, Other: r-x
                self.skills_dir.chmod(0o755)
            
        except OSError as e:
            raise StoreError(f"Failed to create store: {e}")
    
    def is_initialized(self) -> bool:
        """Check if store is properly initialized."""
        return (
            self.base_path.exists() and
            self.skills_dir.exists() and
            self.index_file.exists()
        )
    
    def _load_index(self) -> dict:
        """Load the skill index."""
        if not self.index_file.exists():
            return {"skills": {}, "version": "1.0"}
        
        try:
            with open(self.index_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError) as e:
            raise StoreError(f"Failed to load index: {e}")
    
    def _save_index(self, index: dict) -> None:
        """Save the skill index."""
        try:
            with open(self.index_file, "w", encoding="utf-8") as f:
                json.dump(index, f, indent=2, sort_keys=True)
        except OSError as e:
            raise StoreError(f"Failed to save index: {e}")
    
    def add_skill(self, source: str, name: Optional[str] = None) -> str:
        """Add a skill to the global store.
        
        Args:
            source: Path to skill directory or remote URL
            name: Optional custom name (defaults to directory name)
            
        Returns:
            The skill name in the store
        """
        self.ensure_exists()
        
        # Handle remote URLs
        if source.startswith(("http://", "https://", "git@")):
            source_path = self._clone_remote(source)
            cleanup_temp = True
        else:
            source_path = Path(source)
            cleanup_temp = False
        
        try:
            # Validate source
            if not source_path.exists():
                raise StoreError(f"Source path does not exist: {source}")
            
            skill_file = source_path / "SKILL.md"
            if not skill_file.exists():
                raise StoreError(f"Not a valid skill (missing SKILL.md): {source_path}")
            
            # Validate skill against spec
            code, report = validate_target(source_path)
            if code > 0:
                errors = [issue.get("message", "") for issue in report.get("results", [{}])[0].get("issues", []) if issue.get("severity") == "error"]
                raise StoreError(f"Skill validation failed:\n" + "\n".join(f"  - {e}" for e in errors))
            
            # Read skill metadata from SKILL.md
            try:
                fm = read_frontmatter(source_path / "SKILL.md")
                skill_name = name or fm.get("name") or source_path.name
                skill_version = fm.get("version", "0.0.0")
                skill_description = fm.get("description", "")
            except Exception as e:
                raise StoreError(f"Failed to read skill metadata: {e}")
            
            # Determine skill name
            skill_name = name or skill_name or source_path.name
            
            # Check for conflicts
            skill_path = self.skills_dir / skill_name
            if skill_path.exists():
                raise StoreError(f"Skill already exists: {skill_name}")
            
            # Copy skill to store
            shutil.copytree(source_path, skill_path)
            
            # Set read-only permissions on copied files
            self._make_readonly(skill_path)
            
            # Update index
            index = self._load_index()
            index["skills"][skill_name] = {
                "name": skill_name,
                "version": skill_version,
                "description": skill_description,
                "source": str(source),
                "added_at": str(Path.cwd()),
                "installed_at": str(Path.cwd()),
            }
            self._save_index(index)
            
            return skill_name
            
        except OSError as e:
            # Clean up on failure
            if skill_path.exists():
                shutil.rmtree(skill_path, ignore_errors=True)
            raise StoreError(f"Failed to copy skill: {e}")
        finally:
            # Clean up temporary directory if we cloned
            if cleanup_temp and source_path.parent.name.startswith("tmp"):
                shutil.rmtree(source_path.parent, ignore_errors=True)
    
    def _clone_remote(self, url: str) -> Path:
        """Clone a remote URL to a temporary directory."""
        try:
            # Create temporary directory
            temp_dir = Path(tempfile.mkdtemp(prefix="nunchuck-"))
            
            # Clone the repository
            result = subprocess.run(
                ["git", "clone", url, temp_dir / "skill"],
                capture_output=True,
                text=True,
                check=True
            )
            
            # Return the skill directory
            return temp_dir / "skill"
            
        except subprocess.CalledProcessError as e:
            raise StoreError(f"Failed to clone repository: {e.stderr}")
        except Exception as e:
            raise StoreError(f"Failed to clone remote URL: {e}")
    
    def _make_readonly(self, path: Path) -> None:
        """Make a path read-only (Unix-like systems only)."""
        if platform.system() == "Windows":
            return
        
        try:
            # Recursively make files read-only
            for root, dirs, files in os.walk(path):
                for d in dirs:
                    dir_path = Path(root) / d
                    # Owner: rwx, Group: r-x, Other: r-x
                    dir_path.chmod(0o755)
                for f in files:
                    file_path = Path(root) / f
                    # Owner: rw-, Group: r--, Other: r--
                    file_path.chmod(0o644)
        except OSError:
            # Non-critical, continue
            pass
    
    def remove_skill(self, name: str, force: bool = False) -> None:
        """Remove a skill from the global store."""
        if not self.is_initialized():
            raise StoreError("Store not initialized")
        
        skill_path = self.skills_dir / name
        if not skill_path.exists():
            raise StoreError(f"Skill not found: {name}")
        
        # Check for dependencies
        if not force:
            deps = self._check_dependencies(name)
            if deps:
                click.echo(f"Skill '{name}' is used by:")
                for dep in deps:
                    click.echo(f"  - {dep}")
                if not click.confirm("Remove anyway?"):
                    click.echo("Operation cancelled.")
                    return
        
        try:
            # Remove skill directory
            shutil.rmtree(skill_path)
            
            # Update index
            index = self._load_index()
            if name in index["skills"]:
                del index["skills"][name]
            self._save_index(index)
            
        except OSError as e:
            raise StoreError(f"Failed to remove skill: {e}")
    
    def _check_dependencies(self, skill_name: str) -> list[str]:
        """Check which projects use this skill."""
        dependencies = []
        
        # Check current directory
        if self._project_uses_skill(Path.cwd(), skill_name):
            dependencies.append("current project")
        
        # TODO: Check other known projects
        # This could scan ~/.nunchuck/projects/ or similar
        
        return dependencies
    
    def _project_uses_skill(self, project_path: Path, skill_name: str) -> bool:
        """Check if a project uses a specific skill."""
        # Check for various indicators
        indicators = [
            project_path / ".nunchuck" / "skills" / skill_name,
            project_path / "skills" / skill_name,
            project_path / f".nunchuck-{skill_name}",
        ]
        
        # Also check for skill references in config files
        config_files = [
            project_path / ".nunchuck.toml",
            project_path / "nunchuck.toml",
            project_path / ".nunchuck" / "config.yaml",
        ]
        
        for config in config_files:
            if config.exists():
                try:
                    content = config.read_text(encoding="utf-8")
                    if skill_name in content:
                        return True
                except Exception:
                    pass
        
        return any(indicator.exists() for indicator in indicators)
    
    def list_skills(self) -> dict:
        """List all skills in the store."""
        if not self.is_initialized():
            return {}
        
        index = self._load_index()
        return index.get("skills", {})
    
    def get_skill_path(self, name: str) -> Optional[Path]:
        """Get the path to a skill in the store."""
        skill_path = self.skills_dir / name
        return skill_path if skill_path.exists() else None
    
    def get_skill_info(self, name: str) -> Optional[dict]:
        """Get information about a skill."""
        skills = self.list_skills()
        return skills.get(name)
