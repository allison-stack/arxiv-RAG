import typer
from pathlib import Path
from arxiv_rag.ingest import download_paper, extract_text, save_text
from arxiv_rag.generate import answer

app = typer.Typer(help="arxiv-rag: ingest papers, query the index, run evals.")


@app.command()
def ingest(ids: list[str] = typer.Argument(..., help="arXiv IDs, e.g. 2406.09843")) -> None:
    """Fetch arXiv PDFs, chunk, embed, and persist the index."""
    for arxiv_id in ids:
        typer.echo(f"Downloading {arxiv_id}...")
        pdf_path = download_paper(arxiv_id)
        text = extract_text(pdf_path)
        save_text(arxiv_id, text)


@app.command()
def query(question: str) -> None:
    """Ask a question against the persisted index."""
    txt_files = list(Path("data/raw").glob("*.txt"))
    if not txt_files:
        typer.echo("No papers ingested yet. Run arxiv-rag ingest <id> first")
        raise typer.Exit(1)
    parts = []
    for path in txt_files:
        parts.append(f"\n\n--- {path.name} ---\n\n{path.read_text()}")
    context = "\n\n".join(parts)[:6000]
    typer.echo(answer(question, context))


@app.command()
def eval() -> None:
    """Run the eval harness against the current pipeline."""
    raise NotImplementedError


if __name__ == "__main__":
    app()
