from pydantic import BaseModel


class ChatRequest(BaseModel):
    tenant_id: str
    question: str
