from fastapi import APIRouter
from pydantic import BaseModel

from rag.retriever import retrieve_context
from rag.generator import generate_answer

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
async def chat(request: ChatRequest):

    context = retrieve_context(request.question)

    answer = generate_answer(
        context,
        request.question
    )

    return {
        "question": request.question,
        "answer": answer
    }