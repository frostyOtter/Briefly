# app/models/analysis.py
"""Analysis domain models - what we return from paper analysis"""

from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime


class PaperAnalysis(BaseModel):
    """Core analysis results from a scientific paper"""

    paper_id: str
    title: Optional[str] = None
    summary: Optional[str] = None
    key_findings: List[str] = Field(default_factory=list)
    methodology: Optional[str] = None
    research_questions: List[str] = Field(default_factory=list)


class AnalysisRequest(BaseModel):
    """Request to analyze a paper"""

    paper_id: str


class AnalysisResponse(BaseModel):
    """Response containing analysis results"""

    success: bool
    paper_id: str
    analysis: Optional[PaperAnalysis] = None
    processing_time_seconds: Optional[float] = None
    created_at: datetime = Field(default_factory=datetime.now)


class AnalysisError(BaseModel):
    """Response when analysis fails"""

    success: bool = False
    paper_id: str
    error: str
    details: Optional[str] = None
