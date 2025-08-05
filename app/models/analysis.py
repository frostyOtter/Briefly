# Models for Analysis Router
from pydantic import BaseModel, Field
from typing import List, Dict, Optional
from enum import Enum
from datetime import datetime

class AnalysisStatus(str, Enum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class ModuleAnalysis(BaseModel):
    name: str
    inputs: Dict[str, str]  # Input name -> description (incl. data types/formats)
    outputs: Dict[str, str]  # Output name -> description
    purpose: str
    role_in_system: str

class PaperAnalysisRequest(BaseModel):
    document_id: str
    analysis_options: Optional[Dict[str, bool]] = Field(
        default_factory=lambda: {
            "problem_identification": True,
            "module_analysis": True,
            "generate_visualizations": True
        }
    )

class PaperAnalysisResponse(BaseModel):
    analysis_id: str
    document_id: str
    status: AnalysisStatus
    created_at: datetime
    updated_at: Optional[datetime] = None
    
class AnalysisResult(BaseModel):
    analysis_id: str
    document_id: str
    paper_title: Optional[str] = None
    problem_statement: Optional[str] = None
    module_count: Optional[int] = None
    modules: Optional[List[ModuleAnalysis]] = None
    status: AnalysisStatus
    error_message: Optional[str] = None
    created_at: datetime
    completed_at: Optional[datetime] = None

class AnalysisHistoryItem(BaseModel):
    analysis_id: str
    document_id: str
    paper_title: Optional[str] = None
    status: AnalysisStatus
    created_at: datetime
    completed_at: Optional[datetime] = None
