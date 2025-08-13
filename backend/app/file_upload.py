from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
from uuid import uuid4
from . import ai

router = APIRouter(prefix="/files", tags=["files"])
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
def upload_file(file: UploadFile = File(...)):
    ext = os.path.splitext(file.filename)[1].lower()
    if ext not in [".pdf", ".png", ".jpg", ".jpeg", ".txt"]:
        raise HTTPException(status_code=400, detail="Unsupported file type.")
    file_id = str(uuid4()) + ext
    file_path = os.path.join(UPLOAD_DIR, file_id)
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    # Extract text and embed
    try:
        text = ai.extract_text(file_path)
        embedding = ai.embed_text(text)
    except Exception as e:
        text = ""
        embedding = []
    return {"filename": file.filename, "file_id": file_id, "path": file_path, "extracted_text": text[:500]}  # Return first 500 chars
