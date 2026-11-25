# prueba-ci

A minimal FastAPI example with pytest tests and a GitHub Actions workflow.

## Set up the environment

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then sync the project dependencies:

```bash
uv sync
```

This creates a virtual environment and installs the locked project and development dependencies.

## Run the API

```bash
uv run python app.py
```

The API is available at `http://127.0.0.1:8000`. It has a greeting endpoint at `/` and a health endpoint at `/health`.

## Run the tests

```bash
uv run pytest
```

`requirements.txt` remains available for users who prefer pip.
