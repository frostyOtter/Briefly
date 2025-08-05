# Models for Upload Router
from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from fastapi import UploadFile, File
from enum import Enum

class UploadSource(str, Enum):
    FILE_UPLOAD = "file_upload"
    ARXIV_ID = "arxiv_id"

class UploadRequest(BaseModel):
    source: UploadSource
    description: Optional[str] = None

class ArxivUploadRequest(BaseModel):
    arxiv_id: str = Field(..., description="ArXiv paper ID (e.g., '2311.12345')")
    description: Optional[str] = None

class UploadResponse(BaseModel):
    document_id: str
    filename: str
    page_count: int
    status: str
    message: Optional[str] = None
