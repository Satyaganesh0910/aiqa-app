from fastapi import APIRouter, HTTPException, Body
from . import ai

router = APIRouter(prefix="/chat", tags=["chat"])

@router.post("/ask")
def ask_question(question: str = Body(...), file_ids: list = Body(...)):
    # TODO: Retrieve user files and their extracted text/embeddings
    # For now, just return a dummy answer
    relevant_content = ai.retrieve_relevant_chunks(question, file_ids)
    answer = f"AI answer based on: {relevant_content}"
    return {"question": question, "answer": answer}

