# synapse

## Purpose
Integrate intelligence into systems through retrieval, model calls, and workflow-level inference.

## Why it matters
Without a clear AI layer, intelligence gets bolted on ad hoc and becomes difficult to trace, evaluate, or reuse.

## Scope
This repo focuses on AI workflows, retrieval-aware service structure, and inference boundaries. It does not try to cover every model or vendor integration.

## System Role
`synapse` is the AI and ML systems layer for the ecosystem. It connects data, knowledge, and product workflows through practical intelligence features.

## System Connections
- Depends on: `flux` for prepared data and `lore` for grounded retrieval structure.
- Feeds into: product-facing intelligent features in `summit` and `orbit`.
- Interacts with: `lore`, `summit`, `flux`.

## Core Concepts
- retrieval flow
- inference boundaries
- prompt inputs
- model orchestration
- grounded responses

## Minimal Artifact
`service/main.py`, `service/models.py`, and `docs/architecture.md` form the starter AI service example.

## Notes
The emphasis is on AI that fits into system design, not standalone demos with no operational shape.

## Next Steps
Add provider adapters, evaluation hooks, and clearer retrieval interfaces.
