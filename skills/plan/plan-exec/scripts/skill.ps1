$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

$ConfigPath = Join-Path $ScriptDir ".config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
}

function Show-Help {
    @"
plan-exec - Execute tasks in the active plan directory

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  plan-exec
  plan-exec help
  plan-exec validate

Deterministic behavior:
- Validates `.plan/active/` schemas/invariants
- If terminal (all tasks complete/deferred), archives to `.plan/archive/<id>/`
- Otherwise prints the current `in_progress` task path
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

    $cli = Join-Path $IncludeDir "plan_exec_cli.py"
    if (-not (Test-Path $cli)) {
        Write-Error "error: missing $cli"
        $errors++
    }

    if ($errors -gt 0) {
        exit 1
    }

    Write-Output "ok: plan-exec skill is runnable"
}

function Invoke-Run {
    param([string[]]$Arguments)

    & uv run --project $IncludeDir -- python (Join-Path $IncludeDir "plan_exec_cli.py") @Arguments
}

if ($args.Count -eq 0) {
    Invoke-Run -Arguments @()
    exit 0
}

$command = $args[0]
switch ($command) {
    "help" { Show-Help }
    "validate" { Invoke-Validate }
    default { Invoke-Run -Arguments $args }
}
