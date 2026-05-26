from fastapi import APIRouter, UploadFile, File
from app.services.parser_service import (
    extract_text_from_pdf,
    extract_text_from_docx
)
from app.services.embedding_service import generate_embedding
from app.services.chroma_service import store_resume
from app.services.ranking_service import rank_candidates
from app.services.llm_service import generate_summary
from app.models.schemas import JobDescriptionRequest

import shutil
import os

router = APIRouter(prefix="/resume", tags=["Resume"])

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    file_path = f"{UPLOAD_DIR}/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    if file.filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_path)
    else:
        text = extract_text_from_docx(file_path)

    embedding = generate_embedding(text)

    candidate_name = file.filename.split(".")[0]

    store_resume(candidate_name, text, embedding)

    return {
        "message": "Resume uploaded successfully",
        "candidate": candidate_name
    }

@router.post("/rank")
def rank_resume(request: JobDescriptionRequest):
    results = rank_candidates(request.job_description)

    response = []

    for idx, doc in enumerate(results["documents"][0]):
        summary = generate_summary(doc, request.job_description)

        response.append({
            "candidate": results["ids"][0][idx],
            "summary": summary
        })

    return response
