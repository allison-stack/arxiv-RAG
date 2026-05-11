# arxiv-rag

Ask questions across recent arXiv papers and get grounded, citation-backed answers.

A production-shaped RAG pipeline: PDF ingestion → hybrid retrieval (BM25 + dense) → cross-encoder reranking → grounded generation, wrapped in a FastAPI service with a Next.js chat UI.

## Status

Scaffold only. See `docs/architecture.md` for the planned architecture and the build phases in the project notes.

## Quickstart

```bash
make dev      # install deps, set up the env
make test     # run the test suite
make eval     # run the eval harness
make serve    # start the API locally
```

## Layout

- `arxiv_rag/` — the core library (ingest, embed, index, retrieve, rerank, generate)
- `api/` — FastAPI service
- `web/` — Next.js chat UI
- `evals/` — gold set + eval runner + metrics
- `tests/` — unit + integration tests
- `infra/` — Docker Compose, deployment configs
- `docs/` — architecture, eval methodology, ADRs

## License

MIT
