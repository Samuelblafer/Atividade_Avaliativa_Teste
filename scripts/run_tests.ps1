<#
Script para preparar ambiente e executar testes.

Uso típico (PowerShell):
  .\run_tests.ps1

# Parâmetros (switches):
#  -CreateVenv                 : cria um venv em `.venv` se passado
#  -RunApiTests                : executa testes unitários/funcionais/API se passado
#  -RunPlaywrightTests         : executa testes UI com Playwright se passado
#  -RunSeleniumTests          : executa testes UI com Selenium se passado
#  -InstallPlaywrightBrowsers  : executa `playwright install` se passado
#>

param(
    [switch]$CreateVenv,
    [switch]$RunApiTests,
    [switch]$RunPlaywrightTests,
    [switch]$RunSeleniumTests,
    [switch]$InstallPlaywrightBrowsers
)

Set-StrictMode -Version Latest
Push-Location $PSScriptRoot\..\

# Normalize defaults: avoid switch default values in the param block
# If the user didn't pass a CreateVenv switch, default to creating the venv.
if (-not $PSBoundParameters.ContainsKey('CreateVenv')) { $CreateVenv = $true }

# If no Run* switches were provided, default to running all test suites
if (-not ($PSBoundParameters.ContainsKey('RunApiTests') -or $PSBoundParameters.ContainsKey('RunPlaywrightTests') -or $PSBoundParameters.ContainsKey('RunSeleniumTests'))) {
    $RunApiTests = $true
    $RunPlaywrightTests = $true
    $RunSeleniumTests = $true
}

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

if ($InstallPlaywrightBrowsers) {
    Write-Host "Instalando navegadores do Playwright..."
    python -m playwright install
}

# Criar pasta de evidências
$evid = Join-Path -Path (Get-Location) -ChildPath evidencias
if (-Not (Test-Path -Path $evid)) { New-Item -ItemType Directory -Path $evid | Out-Null }

function Run-PytestSuite {
    param(
        [string]$Name,
        [string]$Pattern,
        [string]$ExtraArgs = ''
    )
    $log = Join-Path $evid ("pytest-{0}.txt" -f $Name)
    Write-Host "Executando suíte: $Name -> padrão: $Pattern"
    try {
        python -m pytest $Pattern $ExtraArgs -q *>$log 2>&1
        Write-Host "Saída de $Name em: $log"
    } catch {
        Write-Host "Erro ao executar $Name. Ver log: $log"
    }
}

if ($RunApiTests) {
    # Executa testes unitários, funcionais e de API, com cobertura
    $covHtml = Join-Path $evid "htmlcov"
    $logApi = Join-Path $evid "pytest-api.txt"
    Write-Host "Executando testes API/unit/functional com cobertura..."
    python -m pytest tests/unit tests/functional tests/system --cov=src --cov-report=html:$covHtml -q *>$logApi 2>&1
    Write-Host "Relatório de cobertura (HTML) em: $covHtml"
}

if ($RunPlaywrightTests) {
    Write-Host "Executando testes Playwright (UI)..."
    # se necessário, instalar navegadores automaticamente
    if (-Not $InstallPlaywrightBrowsers) {
        Write-Host "Nota: se você ainda não instalou navegadores do Playwright, rode: python -m playwright install"
    }
    Run-PytestSuite -Name "playwright" -Pattern "tests/system_ui"
}

if ($RunSeleniumTests) {
    Write-Host "Executando testes Selenium (UI)..."
    Run-PytestSuite -Name "selenium" -Pattern "tests/system_ui_selenium"
}

Write-Host "Execução concluída. Logs e relatórios em: $evid"

Pop-Location
