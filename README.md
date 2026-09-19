# agentic-workflow

## Dev Setup

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
