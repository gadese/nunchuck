$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$IncludeDir = Join-Path $ScriptDir "include"

function Show-Help {
@"
plan-discuss - Shape and stabilize intent into .plan/active.yaml

Usage:
  plan-discuss [--mark-ready]
  plan-discuss help
  plan-discuss validate

Deterministic behavior:
- Ensures .plan/active.yaml exists (creates it if missing)
- Prints current artifact status and any schema errors
- Optionally marks artifact ready (requires no open questions)
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

  $cli = Join-Path $IncludeDir "plan_discuss_cli.py"
  if (-not (Test-Path $cli)) {
    Write-Error "error: missing $cli"
    $errors++
  }

  if ($errors -gt 0) { exit 1 }

  Write-Output "ok: plan-discuss skill is runnable"
}

function Invoke-Run {
  param([string[]]$Arguments)
  & uv run --project $IncludeDir -- python (Join-Path $IncludeDir "plan_discuss_cli.py") @Arguments
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

