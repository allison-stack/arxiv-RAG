import httpx
from pathlib import Path
import pymupdf
from arxiv_rag.chunk import Chunk, recursive_text_splitter

RAW_DIR = Path("data/raw")

def chunk_paper(pdf_path: Path, paper_id: str) -> list[Chunk]:
    chunks = []
    count = 0
    with pymupdf.open(pdf_path) as doc:
        for page_num, page in enumerate(doc, start=1):
            page_text = page.get_text()
            for piece in recursive_text_splitter(page_text):
                chunks.append(Chunk(id=f"{paper_id}-p{count:04d}", paper_id=paper_id, page=page_num, text=piece))
                count += 1
        return chunks

def download_paper(arxiv_id: str) -> Path:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    file_path = RAW_DIR / f"{arxiv_id}.pdf"
    if file_path.exists():
        return file_path
    response = httpx.get(f"https://arxiv.org/pdf/{arxiv_id}.pdf", follow_redirects=True)
    response.raise_for_status()
    data = response.content
    file_path.write_bytes(data)
    return file_path

def extract_text(pdf_path: Path) -> str:
    parts = []
    with pymupdf.open(pdf_path) as doc:
        for page in doc:
            text = page.get_text()
            parts.append(text)
    return "\n\n".join(parts)

def extract_pages(pdf_path: Path) -> list[str]:
    with pymupdf.open(pdf_path) as doc:
        return [page.get_text() for page in doc]
    
def save_text(arxiv_id: str, text: str) -> Path:
    file_path = RAW_DIR / f"{arxiv_id}.txt"
    file_path.write_text(text)
    return file_path