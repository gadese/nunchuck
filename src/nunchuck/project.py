"""Project skill management."""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from .store import Store, StoreError


class ProjectError(Exception):
    """Project-related errors."""
    pass


class Project:
    """Manages skills for a project."""
    
    def __init__(self, root: Path):
        """Initialize project manager.
        
        Args:
            root: Project root directory
        """
        self.root = root
        self.nunchuck_dir = root / ".nunchuck"
        self.skills_dir = self.nunchuck_dir / "skills"
        self.config_file = self.nunchuck_dir / "skills.yaml"
    
    def ensure_exists(self) -> None:
        """Create project structure if it doesn't exist."""
        try:
            self.nunchuck_dir.mkdir(exist_ok=True)
            self.skills_dir.mkdir(exist_ok=True)
            
            if not self.config_file.exists():
                self._save_config({"skills": {}, "version": "1.0"})
        except OSError as e:
            raise ProjectError(f"Failed to create project structure: {e}")
    
    def is_initialized(self) -> bool:
        """Check if project is initialized."""
        return (
            self.nunchuck_dir.exists() and
            self.skills_dir.exists() and
            self.config_file.exists()
        )
    
    def _load_config(self) -> Dict:
        """Load project configuration."""
        if not self.config_file.exists():
            return {"skills": {}, "version": "1.0"}
        
        try:
            with open(self.config_file, "r", encoding="utf-8") as f:
                return yaml.safe_load(f) or {"skills": {}, "version": "1.0"}
        except Exception as e:
            raise ProjectError(f"Failed to load config: {e}")
    
    def _save_config(self, config: Dict) -> None:
        """Save project configuration."""
        try:
            with open(self.config_file, "w", encoding="utf-8") as f:
                yaml.dump(config, f, default_flow_style=False)
        except Exception as e:
            raise ProjectError(f"Failed to save config: {e}")
    
    def use_skill(self, skill_name: str, store: Store) -> None:
        """Use a skill in the project.
        
        Args:
            skill_name: Name of skill to use
            store: Global skill store
        """
        self.ensure_exists()
        
        # Get skill from global store
        skill_path = store.get_skill_path(skill_name)
        if not skill_path:
            raise ProjectError(f"Skill not found in global store: {skill_name}")
        
        # Check if already used
        project_skill_path = self.skills_dir / skill_name
        if project_skill_path.exists():
            raise ProjectError(f"Skill already in use: {skill_name}")
        
        # Create reference (symlink if possible, otherwise copy)
        try:
            if os.name == "nt":  # Windows
                # Use junction on Windows
                import subprocess
                subprocess.run(
                    ["mklink", "/J", str(project_skill_path), str(skill_path)],
                    shell=True,
                    check=True,
                    capture_output=True
                )
            else:
                # Use symlink on Unix
                project_skill_path.symlink_to(skill_path, target_is_directory=True)
        except Exception:
            # Fallback to copy
            import shutil
            shutil.copytree(skill_path, project_skill_path)
        
        # Update config
        config = self._load_config()
        skill_info = store.get_skill_info(skill_name)
        config["skills"][skill_name] = {
            "source": "global",
            "version": skill_info.get("version", "0.0.0") if skill_info else "0.0.0",
            "added_at": str(Path.cwd()),
        }
        self._save_config(config)
    
    def drop_skill(self, skill_name: str) -> None:
        """Remove a skill from the project.
        
        Args:
            skill_name: Name of skill to drop
        """
        if not self.is_initialized():
            raise ProjectError("Project not initialized")
        
        project_skill_path = self.skills_dir / skill_name
        if not project_skill_path.exists():
            raise ProjectError(f"Skill not in use: {skill_name}")
        
        # Remove skill reference
        if project_skill_path.is_symlink():
            project_skill_path.unlink()
        elif project_skill_path.is_dir():
            import shutil
            shutil.rmtree(project_skill_path)
        
        # Update config
        config = self._load_config()
        if skill_name in config["skills"]:
            del config["skills"][skill_name]
        self._save_config(config)
    
    def list_skills(self) -> Dict:
        """List skills used in the project."""
        if not self.is_initialized():
            return {}
        
        config = self._load_config()
        return config.get("skills", {})
    
    def get_skill_path(self, skill_name: str) -> Optional[Path]:
        """Get the path to a skill in the project."""
        skill_path = self.skills_dir / skill_name
        return skill_path if skill_path.exists() else None
