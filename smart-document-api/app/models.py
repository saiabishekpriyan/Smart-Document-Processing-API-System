# app/models.py
from pydantic import BaseModel, Field
from typing import List

# Define the structure for a single extracted fact/entity
class ExtractedFact(BaseModel):
    key: str = Field(..., description="The type of information extracted (e.g., 'Project_Name', 'Skill').")
    value: str = Field(..., description="The value of the extracted information.")

# Define the structure for the API's successful response
class DocumentSummary(BaseModel):
    original_filename: str
    document_type: str
    extraction_status: str = "SUCCESS"
    extracted_data: List[ExtractedFact]