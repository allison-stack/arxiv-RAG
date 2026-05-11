.PHONY: dev test lint eval serve build clean

dev:
	uv sync --all-extras

test:
	uv run pytest

lint:
	uv run ruff check .
	uv run ruff format --check .

format:
	uv run ruff format .
	uv run ruff check --fix .

eval:
	uv run python -m evals.run

serve:
	uv run uvicorn api.main:app --reload --port 8000

build:
	docker compose -f infra/docker-compose.yml build

up:
	docker compose -f infra/docker-compose.yml up

clean:
	rm -rf .pytest_cache .ruff_cache **/__pycache__ dist build *.egg-info
