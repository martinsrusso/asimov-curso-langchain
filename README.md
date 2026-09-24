# ASIMOV — Curso LangChain 1.0 na Prática

Repositório central do curso **Aplicações Inteligentes com IA** (Asimov Academy).

O projeto é estruturado em múltiplos módulos que compartilham as mesmas bibliotecas, o mesmo ambiente virtual (`.venv`) e as mesmas variáveis de ambiente (`.env`).

---

## Estrutura do Repositório

```text
asimov-curso-langchain/
├── .env                  # Chaves de API locais compartilhadas (ignorado pelo git)
├── .env_exemplo          # Modelo para configuração das chaves de API
├── .gitignore            # Regras do Git para o repositório
├── .python-version       # Versão do Python utilizada no projeto (>=3.14)
├── langgraph.json        # Configuração do LangGraph Dev e mapeamento de grafos
├── pyproject.toml        # Configuração do projeto e dependências com uv
├── requirements.txt      # Dependências exportadas para compatibilidade com pip
├── uv.lock               # Lockfile gerado pelo uv para instalações reproduzíveis
├── .venv/                # Ambiente virtual Python compartilhado por todos os módulos
├── README.md             # Esta documentação
└── src/
    └── md_01/            # Módulo 01: Fundamentos do LangChain e Agentes
        ├── __init__.py
        ├── agent.py      # Agente inteligente com LangGraph e ferramentas
        └── main.ipynb    # Notebook interativo de exemplos e exercícios
```

---

## Módulos do Curso

| Módulo | Pasta | Descrição |
|---|---|---|
| **MD-01** | [`src/md_01/`](src/md_01) | Introdução ao LangChain com Google Gemini (`ChatPromptTemplate`, `ChatGoogleGenerativeAI`, `StrOutputParser`, LCEL, `RunnableLambda`) e criação de agentes com `langgraph`. |
| **MD-02** | `src/md_02/` | *(Em breve)* |

> **Padrão de nomenclatura**: Novos módulos devem ser adicionados sob `src/` seguindo a convenção `md_XX/` (ex: `src/md_02/`, `src/md_03/`), permitindo reutilizar o ambiente e pacotes já instalados.

---

## Como Configurar o Ambiente

### 1. Pré-requisitos
- Python `>=3.14`
- [uv](https://docs.astral.sh/uv/) (recomendado) ou `pip`

### 2. Instalação com `uv` (Recomendado)
Para criar e sincronizar o ambiente virtual compartilhado na raiz:

```powershell
uv sync
```

### 3. Instalação alternativa com `venv` + `pip`
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

### 4. Configuração das Variáveis de Ambiente
Copie o modelo de variáveis de ambiente na raiz do projeto:

```powershell
Copy-Item .env_exemplo .env
```

Abra o arquivo `.env` e configure suas chaves de API (ex: `GEMINI_API_KEY`, `TAVILY_API_KEY`, `OPENAI_API_KEY`, etc.).

---

## Executando os Notebooks

1. Abra a pasta do projeto `asimov-curso-langchain` no VS Code.
2. Navegue até o módulo desejado (por exemplo, `src/md_01/main.ipynb`).
3. No canto superior direito do notebook no VS Code, clique em **Select Kernel** -> **Python Environments...** e selecione o interpretador `.venv` da raiz.
4. Execute as células normalmente!

---

## Executando Agentes com LangGraph Dev (LangGraph Studio)

O projeto inclui suporte ao **LangGraph CLI** para rodar o servidor de desenvolvimento local e interagir com seus agentes através da interface web do **LangGraph Studio**.

### 1. Iniciar o servidor de desenvolvimento

**Opção A — Com `uv` (Recomendado, não requer ativar venv):**
```powershell
uv run langgraph dev
```

**Opção B — Ativando o ambiente virtual antes no PowerShell:**
```powershell
.\.venv\Scripts\Activate.ps1
langgraph dev
```

### 2. Acessar os serviços

Assim que o comando for iniciado, o terminal exibirá as URLs de acesso:
- **Studio UI (Interface visual interativa):** [https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024](https://smith.langchain.com/studio/?baseUrl=http://127.0.0.1:2024)
- **API Local:** `http://127.0.0.1:2024`
- **Documentação Swagger:** `http://127.0.0.1:2024/docs`

### 3. Configuração do `langgraph.json`

O arquivo [`langgraph.json`](langgraph.json) mapeia os agentes disponíveis para o servidor:

```json
{
  "dependencies": ["."],
  "graphs": {
    "agent": "src/md_01/agent.py:agente_asimov"
  },
  "env": ".env"
}
```
