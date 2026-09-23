# agentic-workflow

## Local Dev Setup

### Set up Agentic Service Backend

Go into AgenticService folder and run the following commands:

```bash
    python -m venv .venv
```

Activate the virtual environment

```bash
    .venv\Scripts\Activate
```

Install dependencies

```bash
    pip install -r requirements.txt
```

Command for saving newly added dependencies:

```bash
    pip freeze > requirements.txt
```

Create a .env file in the AgenticService folder with the following variables:
JIRA_BASE_URL
JIRA_EMAIL
JIRA_API_TOKEN
OLLAMA_MODEL

Have Ollama running locally with the following command, use the
same name of model as you put in the .env for OLLAMA_MODEL variable.

Example: Using llama3.1:8b

```bash
    ollama run llama3.1:8b
```

Command for running the server:

```bash
    uvicorn app.main:app --reload
```

### Set up the UI

Go into UI folder and run:

```bash
    npm install
    npm run dev
```
