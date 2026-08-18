from fastapi import APIRouter, UploadFile, File
import shutil
import os

from rag.reader import extract_text
from rag.chunker import chunk_text
from rag.embedder import store_embeddings

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text(file_path)

    chunks = chunk_text(text)

    count = store_embeddings(chunks, file.filename)

    return {
        "message": "PDF uploaded and processed successfully",
        "filename": file.filename,
        "chunks_stored": count
    }