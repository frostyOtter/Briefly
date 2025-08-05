from sqlalchemy.orm import Session
from .models import Document, Analysis, ModuleAnalysis

def create_document(db: Session, filename: str, page_count: int, content: str):
    db_document = Document(filename=filename, page_count=page_count, content=content)
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    return db_document

def get_document_by_id(db: Session, document_id: int):
    return db.query(Document).filter(Document.id == document_id).first()

def create_analysis(db: Session, document_id: int):
    db_analysis = Analysis(document_id=document_id)
    db.add(db_analysis)
    db.commit()
    db.refresh(db_analysis)
    return db_analysis

def update_analysis_status(db: Session, analysis_id: int, status: str, results: dict = None, error_message: str = None):
    analysis = db.query(Analysis).filter(Analysis.id == analysis_id).first()
    if analysis:
        analysis.status = status
        analysis.results = results
        analysis.error_message = error_message
        db.commit()
        db.refresh(analysis)
    return analysis

def create_module_analysis(db: Session, analysis_id: int, module_data: dict):
    db_module = ModuleAnalysis(
        analysis_id=analysis_id,
        name=module_data['name'],
        inputs=module_data['inputs'],
        outputs=module_data['outputs'],
        purpose=module_data['purpose'],
        role_in_system=module_data['role_in_system']
    )
    db.add(db_module)
    db.commit()
    db.refresh(db_module)
    return db_module
