# Usage: .\run.ps1
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$MimicRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..")

& (Join-Path $MimicRoot "scripts\eject.sh") @args
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
