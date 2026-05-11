# Evals

First-class eval harness for the RAG pipeline.

## Layout

- `goldset.jsonl` — versioned `{question, expected_answer, source_paper}` triples.
- `run.py` — CLI: `python -m evals.run --model llama3.2:3b`.
- `metrics.py` — faithfulness, context precision/recall, latency p50/p95, $/query.
- `report.py` — writes a markdown table for the README.
- `results/` — per-run JSON, gitignored except baselines.

## Conventions

- Add a new question by appending one JSON object per line to `goldset.jsonl`.
- Never delete questions — mark them deprecated in-place so historical runs stay comparable.
- CI fails a PR if any metric regresses >5% vs. the `main` baseline.
