# agentic-workflow

## Dev Setup

All commands below are run from inside the `AgenticService` folder:

```bash
    cd AgenticService
```

### Set up python virtual environment

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
    python -m uvicorn app.main:app --reload
```
