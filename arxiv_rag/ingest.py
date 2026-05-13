import httpx
from pathlib import Path
import pymupdf
from arxiv_rag.chunk import recursive_text_splitter

RAW_DIR = Path("data/raw")

@dataclass
class Chunk:
    id: str
    paper_id: str
    page: int
    text: str

def chunk_paper(doc, paper_id: str) -> list[Chunk]:
    chunks = []
    for page_num, page in enumerate(doc):
        for i, text in enumerate(recursive_text_splitter(page.get_text())):
            chunks.append(Chunk(id=f"{paper_id}-p{page_num}-c{i}", paper_id=paper_id, page=page_num, text=text))
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