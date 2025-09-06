# app/models/upload.py
"""Upload domain models - what we accept and return for file uploads"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class UploadResponse(BaseModel):
    """Response after successfully uploading a paper"""

    success: bool
    paper_id: str
    filename: str
    message: str
    upload_timestamp: datetime = Field(default_factory=datetime.now)


class UploadError(BaseModel):
    """Response when upload fails"""

    success: bool = False
    error: str
    details: Optional[str] = None
