# Atividade Avaliativa - Testes e API de Estoque

Este repositório contém uma implementação simples de gerenciamento de estoque em `src/estoque.py`, testes unitários e funcionais, e agora inclui uma pequena API web (Flask) com testes de sistema HTTP.

Resumo das alterações adicionadas para atender ao requisito do professor:

- `src/app.py`: pequena API Flask com endpoints para adicionar, remover e verificar produtos.
- `tests/system/test_estoque_system.py`: testes de sistema que exercitam a API via HTTP usando `requests`.
- `src/__init__.py`: torna `src` um pacote importável durante a execução dos testes.
- `tests/conftest.py`: ajusta `sys.path` para garantir que `src` seja importado corretamente pelo `pytest`.
- Atualização em `requirements-dev.txt`: adição de `Flask` e `requests` para executar os testes de sistema.

Como executar (PowerShell)

1. Criar e ativar ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

2. Instalar dependências de desenvolvimento:

```powershell
pip install -r requirements-dev.txt
```

3. Rodar a suíte de testes completa (unitários, funcionais, sistema):

```powershell
pytest -q
```

Observações sobre os testes de sistema

- Os testes de sistema iniciam o servidor Flask em background (porta `5001`) e executam requisições HTTP contra os endpoints.
- Caso precise executar a API manualmente para demonstração ao professor, rode:

```powershell
python -m src.app
# ou
python src\app.py
```

Testes de Interface (UI) com Playwright

- Adicionei uma interface web simples em `src/templates/index.html` e `src/static/app.js` para demonstrar a aplicação no navegador.
- Os testes de UI estão em `tests/system_ui/test_ui_playwright.py` e usam Playwright para abrir o navegador, interagir com a UI e verificar o comportamento.

Como executar os testes de UI (requer instalação do Playwright e dos navegadores):

1. Instale dependências:

```powershell
pip install -r requirements-dev.txt
```

2. Instale os navegadores do Playwright (apenas uma vez):

```powershell
python -m playwright install
```

3. Execute os testes (Playwright + pytest):

```powershell
pytest tests/system_ui -q
```

Observação: o download dos navegadores pode ser grande. Se o ambiente não permitir baixar os navegadores, execute somente os testes de API (os quais já estão presentes e passam).

Testes UI com Selenium

- Se o professor preferir Selenium (WebDriver), adicionei testes em `tests/system_ui_selenium/test_ui_selenium.py`.
- Esses testes usam `webdriver-manager` para baixar automaticamente o driver do Chrome (requer que o Google Chrome esteja instalado no sistema e que a rede permita o download do driver).

Como executar os testes Selenium:

1. Instale dependências:

```powershell
pip install -r requirements-dev.txt
```

2. Rode os testes Selenium (usa ChromeDriver via webdriver-manager):

```powershell
pytest tests/system_ui_selenium -q
```

Observações:
- O `webdriver-manager` baixa e instala o `chromedriver` automaticamente. O Chrome deve estar presente no computador do avaliador.
- Caso a instituição exija outro navegador (Firefox), eu posso adaptar o teste para `GeckoDriver`/Firefox.

Arquivos principais

- `src/estoque.py`: lógica do estoque (adicionar, remover, verificar) e exceção `ErroEstoque`.
- `src/app.py`: API Flask com rotas `POST /produto`, `DELETE /produto`, `GET /produto/<nome>`.
- `tests/unit/*`: testes unitários para a lógica interna.
- `tests/functional/*`: testes funcionais que exercitam a classe `Estoque`.
- `tests/system/*`: novos testes de sistema HTTP.

Contato

Se o professor quiser executar os testes ou ver a aplicação rodando e houver qualquer problema com dependências ou permissão de push, posso ajudar a ajustar ou fornecer um ambiente alternativo (por exemplo um link para Repl.it ou GitHub Codespaces).
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
