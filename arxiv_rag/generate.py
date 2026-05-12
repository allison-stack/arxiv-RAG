import httpx
from arxiv_rag.config import settings

def answer(question: str, context: str) -> str:
    prompt = f"Answer the question using only the provided context. If the answer isn't there, say you don't know.\n\nContext:\n{context}\n\nQuestion: {question}"
    payload = {
        "model": settings.llm_model,
        "prompt": prompt,
        "stream": False
    }
    response = httpx.post(f"{settings.ollama_host}/api/generate", json=payload, timeout=60.0)
    response.raise_for_status()
    data = response.json()
    if "response" not in data:
        raise RuntimeError(f"Ollama returned no response: {data}")
    return data["response"]