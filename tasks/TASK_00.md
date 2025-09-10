# Prompt para Inicialização de Repositório com Metodologia de Desenvolvimento Assistido por IA

"Você é um Arquiteto de Sistemas de IA Sênior, especializado em desenvolvimento assistido por IA e em Python.

Sua tarefa é inicializar um novo repositório chamado `jira-bug-analysis-agent`. Este repositório será independente, contendo toda a sua própria configuração de IA, e não será parte de um Multi-Root Workspace centralizado. Ele já possui um arquivo `README.md` em branco.

Seu objetivo é implementar a metodologia completa de desenvolvimento assistido por IA neste novo repositório, incluindo a estrutura inicial do projeto, os arquivos de controle da estratégia de IA (PLAN.md, CODE_STATE.md, CHANGELOG.md), e um plano de implementação detalhado para o Agente de Análise de Bugs do Jira. Além disso, você configurará os arquivos de contexto para o Gemini e o GitHub Copilot *dentro deste repositório*.

**Ações a Serem Realizadas (Execute cada passo precisamente):**

---

**Parte I: Estruturação Inicial do Projeto e README.md**

1. **Crie a Estrutura de Diretórios Fundamental:**
    * Crie as seguintes pastas na raiz do projeto: `src/`, `tests/`, `docs/`, `scripts/`, `.github/`, `.gemini/`.
    * Dentro de `src/`, crie `src/main.py`.
    * Dentro de `tests/`, crie `tests/test_analysis_agent.py`.
    * Dentro de `scripts/`, crie `scripts/index_codebase.py`.

2. **Atualize o `README.md`:**
    * Substitua o conteúdo atual do `README.md` (assumido como em branco) pelo seguinte:

```markdown
# Projeto: Agente IA para Análise de Jira Issues e Código

## Visão Geral do Projeto

Este repositório contém a implementação de um Agente de IA projetado para automatizar a análise de issues do Jira e investigar a base de código para identificar a causa raiz de bugs. Ele utiliza uma arquitetura de dois agentes especializados: um **Agente de Análise** para interpretar issues do Jira e um **Agente de Investigação** para realizar buscas híbridas (semântica, lexical e histórica) no código-fonte.

A metodologia de desenvolvimento deste projeto é assistida por IA, utilizando arquivos de controle (`PLAN.md`, `CODE_STATE.md`, `CHANGELOG.md`) e configurações específicas para o GitHub Copilot e a Gemini CLI, todas contidas neste repositório.

## Estrutura do Projeto

-   `/src`: Contém o código-fonte principal do agente.
-   `/tests`: Contém os testes unitários e de integração.
-   `/docs`: Contém documentação adicional e guias.
-   `/scripts`: Contém scripts de automação, como o pipeline de indexação.
-   `PLAN.md`: O plano de desenvolvimento estratégico do projeto.
-   `CODE_STATE.md`: Um "snapshot" da arquitetura e estado atual do código.
-   `CHANGELOG.md`: O histórico de mudanças significativas e interações da IA.

## Próximos Passos Imediatos

Consulte o `PLAN.md` para as próximas tarefas e o `CODE_STATE.md` para a descrição detalhada do estado atual.
```

---

**Parte II: Arquivos de Controle da Estratégia de Desenvolvimento de IA**

1. **Crie e Popule `PLAN.md`:**
    * Crie o arquivo `PLAN.md` na raiz do projeto com o seguinte conteúdo:

```markdown
# Plano de Desenvolvimento - Agente IA para Análise de Jira Issues e Código

## Visão Geral do Projeto

O objetivo deste projeto é desenvolver um agente de IA que automatize a análise e o diagnóstico de bugs reportados no Jira, correlacionando as descrições dos problemas com o código-fonte relevante. O sistema será composto por dois agentes colaborativos: o Agente de Análise (que processa as issues do Jira) e o Agente de Investigação (que vasculha o código).

## Fases de Desenvolvimento

### Fase 1: Fundação do Agente de Análise e Setup Inicial (TO DO)

-   [ ] Configurar o ambiente de desenvolvimento Python (venv, requirements.txt).
-   [ ] Implementar a conexão com a API REST do Jira (usando `jira-python`).
-   [ ] Desenvolver o módulo de extração e sumarização de dados da issue do Jira.
-   [ ] Implementar o Reconhecimento de Entidades Nomeadas (NER) personalizado para artefatos de software.
-   [ ] Implementar a classificação de categoria de bugs (UI/Backend/DB).
-   [ ] Gerar o Pacote de Consulta de Investigação (IQP) com resumo, termos lexicais e vetor semântico.

### Fase 2: Núcleo do Agente de Investigação (TO DO)

-   [ ] Configurar o pipeline RAG para indexação do código-fonte (AST-chunking, GraphCodeBERT).
-   [ ] Implementar o banco de dados vetorial local (ChromaDB/FAISS).
-   [ ] Desenvolver a estratégia de busca híbrida (semântica, lexical com ripgrep, histórica com Git).
-   [ ] Implementar a fusão e reclassificação avançada dos resultados da busca.
-   [ ] Gerar o relatório final de diagnóstico em Markdown.

### Fase 3: Integração e Refinamento (TO DO)

-   [ ] Integrar o Agente de Análise e o Agente de Investigação em um fluxo de trabalho completo.
-   [ ] Criar testes de integração de ponta a ponta.
-   [ ] Implementar um ciclo de feedback para melhoria contínua dos modelos de IA.
-   [ ] Desenvolver uma interface para interação do usuário (CLI ou web simples).

## Próximos Passos Imediatos

-   **Current Task:** Configurar o ambiente de desenvolvimento Python, incluindo a criação de um ambiente virtual e o arquivo `requirements.txt` inicial.
```

2. **Crie e Popule `CODE_STATE.md`:**
    * Crie o arquivo `CODE_STATE.md` na raiz do projeto com o seguinte conteúdo:

```markdown
# Estado Atual do Código - Agente IA para Análise de Jira Issues e Código

*Última atualização: [DATA_ATUAL_YYYY-MM-DD HH:MM]*

## Arquitetura Geral

Este projeto será arquitetado como um sistema de microsserviços baseados em agentes, com dois componentes principais em Python: um Agente de Análise para processamento de issues do Jira e um Agente de Investigação para busca e análise de código. A comunicação inicial será interna, com o objetivo de gerar um relatório de diagnóstico.

## Estrutura de Arquivos

-   `/src`: Contém o código-fonte principal.
    -   `main.py`: Ponto de entrada principal do sistema.
-   `/tests`: Contém os testes.
    -   `test_analysis_agent.py`: Arquivo de teste inicial para o Agente de Análise.
-   `/docs`: Pasta para documentação técnica e de design.
-   `/scripts`: Contém scripts de automação.
    -   `index_codebase.py`: Script placeholder para o pipeline de indexação de código.
-   `.github/`: Contém arquivos de configuração para GitHub Copilot e GitHub Actions.
-   `.gemini/`: Contém arquivos de configuração e contexto para a Gemini CLI.
-   `PLAN.md`: Plano de desenvolvimento do projeto.
-   `CODE_STATE.md`: Snapshot do estado atual do código e decisões arquitetônicas.
-   `CHANGELOG.md`: Registro de mudanças e interações do agente de IA.
-   `requirements.txt`: Dependências do Python.

## Componentes Principais (Estado Inicial)

### `src/main.py`

-   **Responsabilidade:** Ponto de entrada do sistema. Atualmente, um stub.
-   **Dependências:** Nenhuma explícita ainda.
-   **Como funciona:** (Placeholder) Será responsável por orquestrar a execução dos dois agentes.

## Próximos Passos Técnicos Sugeridos

-   Instalar as dependências Python iniciais (por exemplo, `jira-python`, `spacy`, `transformers`).
-   Começar a implementar a conexão com a API do Jira em `src/main.py`.
-   Definir o esquema inicial de dados para o Pacote de Consulta de Investigação (IQP).
```

*(Substitua `[DATA_ATUAL_YYYY-MM-DD HH:MM]` pela data e hora atuais)*

3. **Crie e Popule `CHANGELOG.md`:**
    * Crie o arquivo `CHANGELOG.md` na raiz do projeto com o seguinte conteúdo:

```markdown
# Histórico de Mudanças - Agente IA para Análise de Jira Issues e Código

## [DATA_ATUAL_YYYY-MM-DD HH:MM] - v0.1.0

-   **Ação:** Inicialização do repositório e implementação da metodologia de desenvolvimento assistido por IA.
-   **Descrição:** O projeto `jira-bug-analysis-agent` foi bootstrapado. A estrutura de diretórios inicial foi criada. Os arquivos de controle de IA (`PLAN.md`, `CODE_STATE.md`, `CHANGELOG.md`) foram gerados e preenchidos com o plano inicial e o estado do projeto. Os arquivos de configuração de contexto para Gemini CLI e GitHub Copilot foram estabelecidos dentro do próprio repositório.
-   **Arquivos Afetados:** `README.md`, `PLAN.md`, `CODE_STATE.md`, `CHANGELOG.md`, `.github/`, `.gemini/`, `/src`, `/tests`, `/docs`, `/scripts`.
-   **Prompt Usado:** (Este prompt foi executado via Gemini CLI para inicializar o projeto.)
```

*(Substitua `[DATA_ATUAL_YYYY-MM-DD HH:MM]` pela data e hora atuais)*

---

**Parte III: Arquivos de Contexto Específicos da Gemini CLI**

1. **Crie e Popule `.gemini/GEMINI.md`:**
    * Crie o arquivo `.gemini/GEMINI.md` dentro da pasta `.gemini/` com o seguinte conteúdo:

```markdown
# Contexto Global Gemini - Agente IA para Análise de Jira Issues e Código

## Visão Geral do Projeto

Este é o repositório para o agente de IA que analisa issues do Jira e o código-fonte. O projeto é construído em Python e visa automatizar a detecção da causa raiz de bugs.

## Arquitetura Geral do Agente

O sistema é dividido em dois agentes Python distintos:
1.  **Agente de Análise:** Responsável por interagir com a API do Jira, extrair e sumarizar informações das issues, e gerar um 'Pacote de Consulta de Investigação' (IQP).
2.  **Agente de Investigação:** Recebe o IQP e executa uma busca multimodal (semântica, lexical e histórica) no código-fonte, utilizando um pipeline RAG avançado.

A busca no código utilizará um banco de dados vetorial local (ChromaDB/FAISS) e modelos de embedding específicos para código (GraphCodeBERT).

## Stack de Tecnologia Preferida

-   **Linguagem Principal:** Python 3.9+
-   **Bibliotecas Chave:** `jira-python`, `spacy`, `transformers`, `chromadb` (ou `faiss-cpu`), `GitPython`, `ripgrep` (via subprocess).
-   **Framework de Testes:** Pytest

## Padrões de Codificação e Guia de Estilo

-   Siga as diretrizes do **PEP 8** para o código Python.
-   Utilize **docstrings** detalhadas (formato Sphinx ou Google) para todas as funções, classes e módulos.
-   Prefira **type hints** (dicas de tipo) sempre que possível para clareza e segurança.
-   Mantenha o código modular e com alta coesão, baixa acoplagem.
-   Priorize o tratamento robusto de erros e a logagem clara.

## Protocolos de Execução Controlada (Gated Execution)

Sua função principal é me auxiliar no desenvolvimento deste agente. É CRÍTICO que você siga os protocolos de execução.

<PROTOCOL:PLAN>
### MODO DE PLANEJAMENTO ATIVADO
### Sua única função neste modo é investigar e formular um plano passo a passo.
### Você NÃO DEVE escrever, modificar ou executar nenhum código no sistema de arquivos.
### Use as ferramentas de leitura de arquivos e pesquisa para analisar o estado atual do projeto.
### Apresente o plano em formato Markdown para minha aprovação.
</PROTOCOL:PLAN>

<PROTOCOL:IMPLEMENT>
### MODO DE IMPLEMENTAÇÃO ATIVADO
### Este modo só é ativado após a aprovação de um plano por mim.
### Agora você está autorizado a usar as ferramentas WriteFile, Edit e Shell para implementar o plano aprovado.
### Siga o plano aprovado com precisão. Não desvie sem minha confirmação explícita.
</PROTOCOL:IMPLEMENT>
```

2. **Crie a Estrutura e Comando `/git:review.toml`:**
    * Crie a pasta `.gemini/commands/git/` (se não existir).
    * Crie o arquivo `.gemini/commands/git/review.toml` com o seguinte conteúdo:

```toml
description="Atua como um revisor de código sênior, analisando um diff e fornecendo feedback."
prompt = """
Você é um engenheiro de software sênior com experiência em revisão de código. Analise o seguinte diff de código fornecido.
Seu feedback deve ser conciso e acionável. Verifique os seguintes pontos:
1.  **Violações do Guia de Estilo:** Verifique se há inconsistências com as melhores práticas comuns do projeto (consultando o GEMINI.md ou .github/copilot-instructions.md se necessário).
2.  **Bugs em Potencial:** Identifique possíveis erros lógicos, condições de corrida ou tratamento inadequado de erros.
3.  **Documentação:** Aponte a falta de comentários ou docstrings para lógicas complexas.
4.  **Sugestões de Melhoria:** Proponha refatorações que possam melhorar a legibilidade, desempenho ou manutenibilidade.

Apresente sua revisão em formato markdown.

Diff a ser revisado:
{{args}}
"""
```

---

**Parte IV: Arquivos de Contexto Específicos do GitHub Copilot**

1. **Crie e Popule `.github/copilot-instructions.md`:**
    * Crie o arquivo `.github/copilot-instructions.md` dentro da pasta `.github/` com o seguinte conteúdo:

```markdown
# Instruções do GitHub Copilot para o Projeto Jira Bug Analysis Agent

## Sobre Este Projeto

Este projeto é um agente de IA em Python para análise automatizada de issues do Jira e busca de bugs no código-fonte. O objetivo é fornecer diagnósticos precisos e recomendações para desenvolvedores.

## Princípios Orientadores para o Copilot

-   **Priorize a Documentação Interna:** Ao ser questionado sobre o "como" ou "por que" algo funciona neste projeto, sua fonte primária deve ser os arquivos Markdown (`.md`) dentro deste repositório (incluindo `PLAN.md`, `CODE_STATE.md`, `README.md` e a pasta `/docs`). Se a resposta for encontrada na documentação, afirme isso e forneça um resumo, citando o arquivo de origem sempre que possível. Evite suposições.
-   **Estilo de Comunicação:** Seja claro, conciso e profissional. Assuma que o usuário é um desenvolvedor familiarizado com Python e conceitos de IA, mas não com as especificidades deste projeto.
-   **Segurança:** Mantenha a confidencialidade dos detalhes da arquitetura e do código.

## Terminologia do Projeto

-   **Agente de Análise:** O componente responsável por processar issues do Jira.
-   **Agente de Investigação:** O componente responsável por buscar no código-fonte.
-   **IQP (Investigation Query Package):** Pacote de consulta estruturado gerado pelo Agente de Análise para o Agente de Investigação.
-   **RAG (Retrieval Augmented Generation):** Metodologia de recuperação e geração aumentada.
-   **AST-Chunking:** Divisão de código baseada em Árvore de Sintaxe Abstrata.

## Padrões de Geração de Código

-   **Linguagem:** Python 3.9+.
-   **Modularidade:** Mantenha as funções e classes focadas em uma única responsabilidade.
-   **Tratamento de Erros:** Use blocos `try-except` para lidar com exceções de forma explícita e elegante.
-   **Extensibilidade:** Desenvolva componentes de forma que possam ser facilmente estendidos ou substituídos.
-   **Logging:** Use o módulo `logging` padrão do Python para mensagens informativas.

## Padrões de Teste

-   **Framework:** Utilize `pytest` para todos os testes unitários e de integração.
-   **Cobertura:** Busque alta cobertura de testes, especialmente para lógica de negócios crítica.
-   **Tipos de Casos de Teste:** Inclua testes para casos de sucesso, casos de borda, entradas inválidas e cenários de erro.
```

2. **Crie e Popule Arquivos de Instrução Escopados:**
    * Crie a pasta `.github/instructions/` (se não existir).
    * Crie o arquivo `.github/instructions/docs-rules.instructions.md` com o seguinte conteúdo:

```markdown
---
applyTo: "**/*.md"
description: "Regras de estilo e formatação para toda a documentação Markdown neste projeto."
---

### Diretrizes para Documentação

-   **Estilo:** Siga um estilo claro, objetivo e técnico.
-   **Diagramas:** Utilize a sintaxe do Mermaid.js para todos os diagramas (fluxogramas, diagramas de sequência, etc.). Não use ASCII art.
-   **Links:** Sempre use links relativos para referenciar outros documentos dentro do workspace.
-   **Metadados:** Todos os novos documentos devem incluir um timestamp "Última Atualização".
```

    *   Crie o arquivo `.github/instructions/code-rules.instructions.md` com o seguinte conteúdo:

```markdown
---
applyTo: "**/*.py"
description: "Padrões de codificação e melhores práticas para código Python neste projeto."
---

### Diretrizes para Python

-   **Estilo:** Adira estritamente ao **PEP 8**.
-   **Comentários/Docstrings:** Todas as funções, classes e métodos exportados publicamente devem ter docstrings completas. Use comentários inline para explicar lógicas complexas que não são óbvias.
-   **Tipagem:** Evite o uso de `Any` de forma irrestrita. Use type hints para clareza e segurança, recorrendo a `Union` ou `Optional` quando apropriado.
-   **Imutabilidade:** Prefira estruturas de dados imutáveis quando fizer sentido para evitar efeitos colaterais inesperados.
```

3. **Crie a Biblioteca de Prompts Reutilizáveis:**
    * Crie a pasta `.github/prompts/` (se não existir).
    * Crie o arquivo `.github/prompts/review-code.prompt.md` com o seguinte conteúdo:

```markdown
---
description: "Realiza uma revisão de código de nível sênior no código selecionado, com base nos padrões do projeto."
---
@workspace

Você é um arquiteto de software sênior. Revise o código Python selecionado (`{{selection}}`) para o projeto 'Jira Bug Analysis Agent'.
Sua revisão deve focar nos seguintes aspectos, conforme definido em `copilot-instructions.md` e `code-rules.instructions.md`:
1.  **Padrões de Codificação (PEP 8, Docstrings, Type Hints):** Identifique quaisquer violações.
2.  **Bugs em Potencial:** Sugira melhorias para tratamento de erros, condições de corrida ou lógica falha.
3.  **Modularidade e Design:** Avalie a clareza, coesão e acoplamento do código.
4.  **Sugestões de Melhoria:** Proponha refatorações para otimizar desempenho ou manutenibilidade.

Apresente seu feedback em formato Markdown, com exemplos de código quando apropriado.
```

    *   Crie o arquivo `.github/prompts/analyze-issue.prompt.md` com o seguinte conteúdo:

```markdown
---
description: "Analisa o texto de uma issue do Jira e extrai informações estruturadas para o Agente de Análise."
---
@workspace

Você é o Agente de Análise. Sua tarefa é processar o seguinte texto de uma issue do Jira e extrair informações cruciais para o Pacote de Consulta de Investigação (IQP).

**Texto da Issue do Jira:**
{{selection}}

**Siga estes passos:**
1.  **Sumarização Abstrativa:** Crie um `core_problem_summary` conciso (resumo do problema central) que capture a essência do bug.
2.  **Extração de Entidades Técnicas (NER):** Identifique e liste `lexical_query_terms` como nomes de funções, classes, caminhos de arquivo, códigos de erro (ex: HTTP 500) e mensagens de log literais.
3.  **Classificação de Categoria:** Classifique o `bug_category` em uma das seguintes categorias: `UI/Frontend`, `Backend/API`, `Database`, `Performance`, `Security`, `Build/Deployment`, `Outro`.

Apresente as informações em um formato JSON claro, como um protótipo para o IQP, sem o `semantic_query_vector` nesta etapa.
```

    *   Crie o arquivo `.github/prompts/plan-feature.prompt.md` com o seguinte conteúdo:

```markdown
---
description: "Gera um plano de implementação detalhado para uma nova funcionalidade no projeto, seguindo a metodologia de fases."
variables:
  name: feature_description
  description: "A descrição da funcionalidade a ser implementada."
---
@workspace

Você é um Arquiteto de Sistemas de IA Sênior. Preciso de um plano de implementação para a seguinte funcionalidade: "{{feature_description}}".

Com base na arquitetura e nos padrões definidos neste projeto (consultando `PLAN.md`, `CODE_STATE.md` e `copilot-instructions.md`), por favor, gere um plano de implementação detalhado em formato Markdown, seguindo a estrutura de fases:

1.  **Visão Geral da Funcionalidade:** Um breve resumo da funcionalidade.
2.  **Fases da Implementação:** Divida a funcionalidade em fases lógicas (ex: Design, Implementação Core, Testes, Documentação).
3.  **Tarefas Detalhadas por Fase:** Para cada fase, liste as tarefas específicas a serem realizadas, com caixas de seleção `[ ]`.
4.  **Componentes Afetados/Novos:** Identifique os módulos e arquivos existentes que serão modificados e os novos que serão criados.
5.  **Critérios de Aceitação:** Defina como o sucesso da implementação será medido.

Lembre-se de aderir aos **Protocolos de Execução Controlada** definidos em `.gemini/GEMINI.md`. Este é um prompt de **planejamento**, portanto, **NÃO GERE CÓDIGO** nesta resposta.
```

    *   Crie o arquivo `.github/prompts/generate-tests.prompt.md` com o seguinte conteúdo:

```markdown
---
description: "Gera testes unitários para o código Python selecionado usando Pytest, cobrindo cenários importantes."
---
@workspace

Você é um Engenheiro de Testes de Software Sênior. Sua tarefa é gerar testes unitários abrangentes para o seguinte código Python selecionado (`{{selection}}`), utilizando o framework `pytest`.

**Diretrizes:**
1.  Inclua casos de teste para entradas válidas, entradas inválidas e casos extremos.
2.  Use mocks quando apropriado para isolar as unidades de código.
3.  Garanta que os testes sejam legíveis, organizados e sigam os padrões de teste do projeto definidos em `.github/copilot-instructions.md`.
4.  Apresente o código dos testes em um bloco de código Python.
```
---

**Parte V: Documente e Crie um Guia de utilização dos Prompts Reutilizáveis**
1. **Crie uma seção no `README.md`:**
    * Para cada prompt criado na Parte IV, adicione uma breve descrição no `README.md` explicando seu propósito e quando usá-lo.
    * Adicione a seguinte seção ao final do `README.md`, onde XXX e YYY são substituídos pelos nomes e descrições reais dos prompts criados:

```markdown
## Guia de Utilização dos Prompts Reutilizáveis

Este repositório contém uma série de prompts reutilizáveis que podem ser utilizados para diferentes tarefas de desenvolvimento assistido por IA. Abaixo está uma lista dos prompts disponíveis e suas descrições:

1. **Prompt XXX**
   - Descrição: XXX
   - Localização: XXX

2. **Prompt YYY**
   - Descrição: YYY
   - Localização: YYY

... e assim por diante ...
```

---

**Confirmação Final:**

Após executar todas essas etapas, confirme que a tarefa foi concluída com a mensagem: "Inicialização do repositório `jira-bug-analysis-agent` e setup completo da metodologia de desenvolvimento assistido por IA concluídos com sucesso. Todos os arquivos de contexto e controle foram criados e populados."

---
