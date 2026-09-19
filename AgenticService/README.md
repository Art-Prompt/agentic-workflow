# agentic-workflow

## Dev Setup

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

Command for running the server (run from the repo root, with the venv activated):

```powershell
    $env:PYTHONPATH = "."
    python -m uvicorn AgenticService.app.main:app --reload
```

`PYTHONPATH` must be set because `--reload` spawns a subprocess that doesn't inherit the interpreter's `sys.path`, only `PYTHONPATH`.
