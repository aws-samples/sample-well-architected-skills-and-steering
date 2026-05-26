# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0
# One-liner remote installer for Well-Architected Skills & Steering (Windows)
# Usage: irm https://raw.githubusercontent.com/aws-samples/sample-well-architected-skills-and-steering/main/bootstrap.ps1 | iex
# Then run: Install-WellArchitected -Tool claude-code -TargetDir C:\Projects\my-app
#
# Or as a true one-liner:
# & ([scriptblock]::Create((irm https://raw.githubusercontent.com/aws-samples/sample-well-architected-skills-and-steering/main/bootstrap.ps1))) -Tool claude-code -TargetDir .\my-project
# Defaults to --tool auto with --force in current directory (auto-detects installed AI tools)

param(
    [string[]]$Tool = @("auto"),
    [string]$TargetDir = ".",
    [switch]$Force = $true,
    [switch]$Global,
    [switch]$Symlink
)

$ErrorActionPreference = "Stop"
$repoUrl = "https://github.com/aws-samples/sample-well-architected-skills-and-steering/archive/refs/heads/main.zip"
$tmpDir = Join-Path ([System.IO.Path]::GetTempPath()) "wa-skills-install-$([guid]::NewGuid().ToString('N').Substring(0,8))"

try {
    Write-Host "Downloading Well-Architected Skills & Steering..."
    $zipPath = "$tmpDir.zip"
    Invoke-WebRequest -Uri $repoUrl -OutFile $zipPath -UseBasicParsing

    Write-Host "Extracting..."
    Expand-Archive -Path $zipPath -DestinationPath $tmpDir -Force
    Remove-Item $zipPath

    $extractedDir = Get-ChildItem $tmpDir -Directory | Select-Object -First 1

    Write-Host "Running installer..."
    $installArgs = @{
        Tool      = $Tool
        TargetDir = $TargetDir
    }
    if ($Force) { $installArgs.Force = $true }
    if ($Global) { $installArgs.Global = $true }
    if ($Symlink) { $installArgs.Symlink = $true }

    & "$($extractedDir.FullName)\install.ps1" @installArgs
}
finally {
    if (Test-Path $tmpDir) { Remove-Item $tmpDir -Recurse -Force }
    if (Test-Path "$tmpDir.zip") { Remove-Item "$tmpDir.zip" -Force }
}
