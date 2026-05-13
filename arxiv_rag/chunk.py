from dataclasses import dataclass
from langchain_text_splitters import RecursiveCharacterTextSplitter

@dataclass
class Chunk:
    id: str
    paper_id: str
    page: int
    text: str

def recursive_text_splitter(text: str, paper_id: str) -> list[Chunk]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=100
    )
    pieces = splitter.split_text(text)
    return [Chunk(id=f"{paper_id}-{i:04d}", paper_id=paper_id, page=0, text=t) for i, t in enumerate(pieces)]