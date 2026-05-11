import typer

app = typer.Typer(help="arxiv-rag: ingest papers, query the index, run evals.")


@app.command()
def ingest(ids: list[str] = typer.Argument(..., help="arXiv IDs, e.g. 2406.09843")) -> None:
    """Fetch arXiv PDFs, chunk, embed, and persist the index."""
    raise NotImplementedError


@app.command()
def query(question: str) -> None:
    """Ask a question against the persisted index."""
    raise NotImplementedError


@app.command()
def eval() -> None:
    """Run the eval harness against the current pipeline."""
    raise NotImplementedError


if __name__ == "__main__":
    app()
