# prueba-ci

A minimal FastAPI example with pytest tests and a GitHub Actions workflow.

## Run the API

```bash
python -m pip install -r requirements.txt
python app.py
```

The API is available at `http://127.0.0.1:8000`. It has a greeting endpoint at `/` and a health endpoint at `/health`.

## Run the tests

```bash
python -m pytest
```
