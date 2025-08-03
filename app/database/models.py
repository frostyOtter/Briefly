from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from enum import Enum as PyEnum

Base = declarative_base()

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    page_count = Column(Integer)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    content = Column(Text)

class AnalysisStatus(PyEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    COMPLETED = "completed"
    FAILED = "failed"

class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"))
    status = Column(Enum(AnalysisStatus), default=AnalysisStatus.PENDING)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    results = Column(JSON, nullable=True)
    error_message = Column(Text, nullable=True)

class ModuleAnalysis(Base):
    __tablename__ = "module_analyses"
    id = Column(Integer, primary_key=True, index=True)
    analysis_id = Column(Integer, ForeignKey("analyses.id"))
    name = Column(String, index=True)
    inputs = Column(JSON)
    outputs = Column(JSON)
    purpose = Column(Text)
    role_in_system = Column(Text)
