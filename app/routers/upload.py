from loguru import logger
from fastapi import APIRouter, UploadFile, File, HTTPException

from app.utils.read_files import extract_text_from_pdf

router = APIRouter(prefix="/upload", tags=["upload"])


@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if file.filename and not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files supported")
    content = await file.read()
    text = extract_text_from_pdf(content)
    return {"text": text[:1000]}  # Return first 1000 chars for testing
