from fastapi import FastAPI

from arxiv_rag import __version__

app = FastAPI(title="arxiv-rag", version=__version__)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "version": __version__}
