# Models for Visualization Router
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from enum import Enum


class DiagramType(str, Enum):
    FLOWCHART = "flowchart"
    SEQUENCE = "sequence"


class VisualizationRequest(BaseModel):
    analysis_id: str
    diagram_type: DiagramType
    include_details: bool = True
    theme: Optional[str] = "default"


class CustomVisualizationRequest(BaseModel):
    analysis_id: str
    diagram_type: DiagramType
    modules_to_include: Optional[List[str]] = None
    highlight_modules: Optional[List[str]] = None
    theme: Optional[str] = "default"
    direction: Optional[Literal["TB", "BT", "LR", "RL"]] = "TB"  # For flowcharts


class VisualizationResponse(BaseModel):
    analysis_id: str
    diagram_type: DiagramType
    mermaid_code: str
    svg_data: Optional[str] = None  # Base64 encoded SVG if pre-rendered
