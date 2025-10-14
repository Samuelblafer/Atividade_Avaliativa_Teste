# Projeto de Teste Automatizado - Atividade Avaliativa 2
# Projeto de Teste Automatizado - Atividade Avaliativa 2

Este repositório contém um pequeno projeto para a disciplina com testes unitários e funcionais automatizados usando pytest.

Estrutura básica:

- src/: código da aplicação (módulo `estoque`)
- tests/unit/: testes unitários focados em métodos internos
- tests/functional/: testes funcionais de cenário (nível de sistema)

Informações do aluno (entrega individual):

- Aluno: Samuel

Como rodar localmente (PowerShell):

```powershell
# (opcional) criar e ativar venv
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# instalar dependências de desenvolvimento
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt

# rodar todos os testes
python -m pytest -q

# ou rodar apenas os testes funcionais
python -m pytest tests/functional -q

# adicionar cobertura
python -m pytest --cov=src -q
```

Script auxiliar para gerar evidências (logs e relatório de cobertura):

```powershell
# Executar script que cria/usa venv, instala deps, gera logs e cobertura
.
\scripts\run_tests.ps1
```

Evidências: inclua screenshots ou vídeo da execução dos testes no repositório quando entregar. O script acima grava os resultados em `evidencias/`.

Boa prática: comite e envie o repositório para o GitHub; o workflow em `.github/workflows/python-tests.yml` executará os testes automaticamente em pushes/PRs.
