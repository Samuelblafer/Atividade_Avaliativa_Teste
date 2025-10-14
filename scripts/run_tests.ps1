# Script para executar testes, gerar cobertura e salvar evidências
param(
    [switch]$CreateVenv = $true
)

Set-StrictMode -Version Latest
Push-Location $PSScriptRoot\..\

if ($CreateVenv) {
    if (-Not (Test-Path -Path .\.venv)) {
        Write-Host "Criando venv .venv..."
        python -m venv .venv
    }
}

# Ativar venv
Write-Host "Ativando venv..."
& .\.venv\Scripts\Activate.ps1

# Instalar dependências
Write-Host "Instalando dependências..."
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt

# Criar pasta de evidências
$evid = Join-Path -Path (Get-Location) -ChildPath evidencias
if (-Not (Test-Path -Path $evid)) { New-Item -ItemType Directory -Path $evid | Out-Null }

# Rodar pytest com log e cobertura
$logFile = Join-Path $evid "pytest-output.txt"
$covHtml = Join-Path $evid "htmlcov"
Write-Host "Executando pytest... Saída em $logFile"
python -m pytest --cov=src --cov-report=html:$covHtml --maxfail=0 -q *>$logFile 2>&1

Write-Host "Relatórios gerados em: $evid"

Pop-Location
