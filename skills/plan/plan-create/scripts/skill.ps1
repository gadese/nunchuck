$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

$ConfigPath = Join-Path $ScriptDir ".config.ps1"
if (Test-Path $ConfigPath) {
    . $ConfigPath
}

function Show-Help {
    @"
plan-create - Create a new plan skeleton in .plan/<N>/

Commands:
  help      Show this help message
  validate  Verify the skill is runnable (read-only)

Usage:
  plan-create [N] [--title TITLE] [--force]
  plan-create help
  plan-create validate

Creates:
  .plan/<N>/plan.md
  .plan/<N>/a/index.md
  .plan/<N>/a/i.md

If N is omitted, uses the next available plan number.
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

    Push-Location $IncludeDir
    try {
        & uv run python plan_create_cli.py @Arguments
    } finally {
        Pop-Location
    }
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
