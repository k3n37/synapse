from fastapi import FastAPI

from service.models import ChatRequest

app = FastAPI(title="ai-platform")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "ai-platform"}


@app.post("/chat")
def chat(payload: ChatRequest) -> dict[str, object]:
    return {
        "tenant_id": payload.tenant_id,
        "answer": f"Stubbed grounded response for: {payload.question}",
        "citations": ["doc_001#chunk_04"],
    }
