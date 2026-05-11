# Architecture

> Stub. Replace with a one-paragraph overview, a diagram, and component descriptions once the pipeline is wired up.

## Components

- **Ingest** — fetch arXiv PDFs by ID, extract text (PyMuPDF), recursive chunking.
- **Embed** — sentence-transformers (`all-MiniLM-L6-v2` to start).
- **Index** — FAISS for dense, BM25 for sparse, both persisted to `data/index/`.
- **Retrieve** — hybrid search with Reciprocal Rank Fusion.
- **Rerank** — cross-encoder (`ms-marco-MiniLM-L-6-v2`).
- **Generate** — pluggable LLM (Ollama for dev, hosted for prod). Grounded prompt with refusal on missing context.
- **Telemetry** — Langfuse traces, token + cost tracking.

## Request flow

```
question → embed → hybrid retrieve (k=20) → rerank (k=4) → prompt → LLM → answer + sources
                                                                      ↓
                                                          faithfulness check
```

## Decisions

See `docs/decisions/` for ADRs.
