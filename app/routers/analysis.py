from fastapi import APIRouter, Body
from app.services.analysis_service import analyze_paper

router = APIRouter(prefix="/analysis", tags=["analysis"])


@router.post("/")
def analyze_text(text: str = Body(..., embed=True)):
    return analyze_paper(text)
