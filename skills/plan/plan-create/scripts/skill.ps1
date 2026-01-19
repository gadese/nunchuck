$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

$ConfigPath = Join-Path $ScriptDir ".config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
}

function Show-Help {
    @"
plan-create - Compile .plan/active.yaml into .plan/active/

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  plan-create [--force]
  plan-create help
  plan-create validate

Creates/overwrites:
  .plan/active/plan.md
  .plan/active/<letter>/index.md
  .plan/active/<letter>/<roman>.md

Precondition:
  .plan/active.yaml exists and is status: ready (use plan-discuss).
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

    $cli = Join-Path $IncludeDir "plan_create_cli.py"
    if (-not (Test-Path $cli)) {
        Write-Error "error: missing $cli"
        $errors++
    }

    if ($errors -gt 0) {
        exit 1
    }

    Write-Output "ok: plan-create skill is runnable"
}

function Invoke-Run {
    param([string[]]$Arguments)

    & uv run --project $IncludeDir -- python (Join-Path $IncludeDir "plan_create_cli.py") @Arguments
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
