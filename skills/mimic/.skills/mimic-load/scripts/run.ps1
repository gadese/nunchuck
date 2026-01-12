# Usage: .\run.ps1 <persona>
$ErrorActionPreference = "Stop"

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$MimicRoot = Resolve-Path (Join-Path $ScriptDir "..\..\..")

& (Join-Path $MimicRoot "scripts\load.sh") @args
if ($LASTEXITCODE -ne 0) { exit $LASTEXITCODE }
