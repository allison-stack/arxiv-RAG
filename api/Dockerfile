FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir uv

COPY pyproject.toml ./
COPY arxiv_rag/ ./arxiv_rag/
COPY api/ ./api/

RUN uv pip install --system --no-cache ".[api]"

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
