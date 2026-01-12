#
# nunchuck.ps1 - Install nunchuck CLI on Windows
#
# Usage: .\nunchuck.ps1 [dev|user]
#   dev:  Install in development mode (editable)
#   user: Install for current user only (default)
#

param(
    [ValidateSet("dev", "user")]
    [string]$Mode = "user"
)

# Colors for output
$Colors = @{
    Red = "Red"
    Green = "Green"
    Yellow = "Yellow"
}

Write-Host "Installing nunchuck CLI..." -ForegroundColor $Colors.Green

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

Write-Host "Installation complete!" -ForegroundColor $Colors.Green
Write-Host ""
Write-Host "Usage:"
Write-Host "  nunchuck --help          Show help"
Write-Host "  nunchuck install <repo>  Install skills to central directory"
Write-Host "  nunchuck list            List available skills"
Write-Host "  nunchuck use <skill>     Use skill in current directory"
Write-Host "  nunchuck adapter generate  Generate IDE adapters"
Write-Host "  nunchuck validate <path>      Validate a skill"
