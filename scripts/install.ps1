#
# nunchuck.ps1 - Install nunchuck CLI on Windows
#
# Usage: .\install.ps1 [dev|user|uv]
#   dev:  Install in development mode (editable) using pip
#   user: Install for current user only using pip (default)
#   uv:   Install using uv (fastest, recommended for development)
#

param(
    [ValidateSet("dev", "user", "uv")]
    [string]$Mode = "uv"
)

# Colors for output
$Colors = @{
    Red = "Red"
    Green = "Green"
    Yellow = "Yellow"
}

Write-Host "Installing nunchuck CLI..." -ForegroundColor $Colors.Green

# Check if uv is installed (for uv mode)
if ($Mode -eq "uv") {
    try {
        uv --version | Out-Null
        Write-Host "Found uv" -ForegroundColor $Colors.Green
    } catch {
        Write-Host "uv not found. Installing uv..." -ForegroundColor $Colors.Yellow
        # Install uv using PowerShell installer
        irm https://astral.sh/uv/install.ps1 | iex
        
        # Try to find uv in PATH
        try {
            uv --version | Out-Null
            Write-Host "uv installed successfully" -ForegroundColor $Colors.Green
        } catch {
            Write-Host "Please add uv to your PATH and restart PowerShell" -ForegroundColor $Colors.Yellow
            Write-Host "Or use: pip install uv" -ForegroundColor $Colors.Yellow
            exit 1
        }
    }
}

# Check if Python is installed
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Found Python: $pythonVersion" -ForegroundColor $Colors.Green
} catch {
    Write-Host "Error: Python is not installed" -ForegroundColor $Colors.Red
    Write-Host "Please install Python 3.10 or later from https://python.org"
    exit 1
}

# Check Python version
try {
    $versionOutput = python -c "import sys; print('.'.join(map(str, sys.version_info[:2])))"
    $versionParts = $versionOutput.Split('.')
    $major = [int]$versionParts[0]
    $minor = [int]$versionParts[1]
    
    if ($major -lt 3 -or ($major -eq 3 -and $minor -lt 10)) {
        Write-Host "Error: Python 3.10 or later is required (found $versionOutput)" -ForegroundColor $Colors.Red
        exit 1
    }
} catch {
    Write-Host "Error: Could not determine Python version" -ForegroundColor $Colors.Red
    exit 1
}

# Check if pip is installed
try {
    pip --version | Out-Null
    Write-Host "Found pip" -ForegroundColor $Colors.Green
} catch {
    Write-Host "Error: pip is not installed" -ForegroundColor $Colors.Red
    Write-Host "Please install pip: https://pip.pypa.io/en/stable/installation/"
    exit 1
}

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
# Go up one level to get to repo root (scripts -> repo root)
$RepoRoot = Split-Path -Parent $ScriptDir

# Change to repo root
Set-Location $RepoRoot

# Install dependencies
Write-Host "Installing dependencies..." -ForegroundColor $Colors.Yellow
pip install --upgrade pip setuptools wheel

# Install nunchuck
switch ($Mode) {
    "uv" {
        Write-Host "Installing with uv..." -ForegroundColor $Colors.Yellow
        uv pip install -e .
    }
    "dev" {
        Write-Host "Installing in development mode..." -ForegroundColor $Colors.Yellow
        pip install -e .
    }
    "user" {
        Write-Host "Installing for current user..." -ForegroundColor $Colors.Yellow
        pip install --user .
    }
}

# Verify installation
Write-Host "Verifying installation..." -ForegroundColor $Colors.Yellow
try {
    $nunchuckVersion = nunchuck --version
    Write-Host "✓ nunchuck command is available" -ForegroundColor $Colors.Green
    Write-Host $nunchuckVersion
} catch {
    Write-Host "Warning: nunchuck command not found in PATH" -ForegroundColor $Colors.Yellow
    Write-Host "You may need to add %APPDATA%\Python\Python3*\Scripts to your PATH"
    Write-Host "Or use Python launcher: py -m nunchuck --help"
}

# Copy skills to ~/.nunchuck
$NunchuckDir = if ($env:NUNCHUCK_DIR) { $env:NUNCHUCK_DIR } else { "$env:USERPROFILE\.nunchuck" }
$SkillsSrc = Join-Path $RepoRoot "skills"

if (Test-Path $SkillsSrc) {
    Write-Host "Installing skills to $NunchuckDir..." -ForegroundColor $Colors.Yellow
    $SkillsDest = Join-Path $NunchuckDir "skills"
    
    # Create destination directory
    if (-not (Test-Path $SkillsDest)) {
        New-Item -ItemType Directory -Path $SkillsDest -Force | Out-Null
    }
    
    # Copy each skill directory
    $skillCount = 0
    Get-ChildItem -Path $SkillsSrc -Directory | ForEach-Object {
        $skillName = $_.Name
        $destPath = Join-Path $SkillsDest $skillName
        
        if (Test-Path $destPath) {
            Write-Host "  Updating $skillName..."
            Remove-Item -Path $destPath -Recurse -Force
        } else {
            Write-Host "  Installing $skillName..."
        }
        
        Copy-Item -Path $_.FullName -Destination $destPath -Recurse
        $skillCount++
    }
    
    Write-Host "✓ Installed $skillCount skills to $NunchuckDir" -ForegroundColor $Colors.Green
} else {
    Write-Host "No skills directory found in repository" -ForegroundColor $Colors.Yellow
}

Write-Host "Installation complete!" -ForegroundColor $Colors.Green
Write-Host ""
Write-Host "Usage:"
Write-Host "  nunchuck list            List available skills"
Write-Host "  nunchuck use <skill>     Copy skill to current project"
Write-Host "  nunchuck validate <path> Validate a skill"
Write-Host "  nunchuck adapter         Generate IDE adapters"
Write-Host ""
Write-Host "Skills are installed to: $NunchuckDir\skills"
