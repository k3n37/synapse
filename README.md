# synapse

Starter AI service architecture for ingestion, embeddings, retrieval, and LLM orchestration.

## Purpose

Create a focused foundation for building practical AI features that integrate with product systems instead of living as isolated demos.

## Role in the ecosystem

- AI runtime behind `orbit`
- Consumer of `flux`
- Upstream to `ai-knowledge-system`

## Status

Level 2 starter repo with a small FastAPI service shape and architecture docs.

## Tech stack

- Python
- FastAPI
- Pydantic

## Structure

```text
synapse/
├── docs/
│   └── architecture.md
├── service/
│   ├── main.py
│   └── models.py
├── .editorconfig
├── .gitignore
├── README.md
├── ROADMAP.md
└── requirements.txt
```

## Getting started

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn service.main:app --reload
```

## Related repositories

- `flux`
- `ai-knowledge-system`
- `orbit`

## Future direction

Add retrieval adapters, evaluation hooks, and provider abstractions without making the repo depend on every AI library under the sun.
