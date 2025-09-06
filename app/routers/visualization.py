from fastapi import APIRouter, Body
from app.services.visualization_service import (
    generate_flowchart,
    generate_sequence_diagram,
)

router = APIRouter(prefix="/visualize", tags=["visualize"])


@router.post("/flowchart")
def flowchart(modules: list = Body(...)):
    return {"mermaid": generate_flowchart(modules)}


@router.post("/sequence")
def sequence(modules: list = Body(...)):
    return {"mermaid": generate_sequence_diagram(modules)}
