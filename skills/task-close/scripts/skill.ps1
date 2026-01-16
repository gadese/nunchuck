$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

$ConfigPath = Join-Path $ScriptDir ".config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
}

function Show-Help {
    @"
task-close - Close a task

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  task-close <id> --reason {completed|abandoned}
  task-close help
  task-close validate

Updates .tasks/<id>.md frontmatter:
- sets state=closed
- sets close_reason
- sets closed_at and updated_at
- recomputes intent_hash
If the closed task is currently active, clears .tasks/.active.
"@
}

function Invoke-Validate {
    $errors = 0

    if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
        Write-Error "error: uv not found. Install from https://docs.astral.sh/uv/"
        $errors++
    }

    $pyproject = Join-Path $IncludeDir "pyproject.toml"
    if (-not (Test-Path $pyproject)) {
        Write-Error "error: missing $pyproject"
        $errors++
    }

    $cli = Join-Path $IncludeDir "task_close_cli.py"
    if (-not (Test-Path $cli)) {
        Write-Error "error: missing $cli"
        $errors++
    }

    if ($errors -gt 0) {
        exit 1
    }

    Write-Output "ok: task-close skill is runnable"
}

function Invoke-Run {
    param([string[]]$Arguments)

    Push-Location $IncludeDir
    try {
        & uv run python task_close_cli.py @Arguments
    } finally {
        Pop-Location
    }
}

$command = if ($args.Count -gt 0) { $args[0] } else { "help" }

switch ($command) {
    "help" { Show-Help }
    "validate" { Invoke-Validate }
    default { Invoke-Run -Arguments $args }
}
