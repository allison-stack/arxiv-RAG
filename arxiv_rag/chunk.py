from dataclasses import dataclass
from langchain_text_splitters import RecursiveCharacterTextSplitter

@dataclass
class Chunk:
    id: str
    paper_id: str
    page: int
    text: str

def recursive_text_splitter(text: str) -> list[Chunk]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=900,
        chunk_overlap=100
    )
    return splitter.split_text(text)