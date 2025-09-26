# app/main.py
from fastapi import FastAPI, UploadFile, File, HTTPException
from .models import DocumentSummary
from .services import process_document

# Initialize the FastAPI application
app = FastAPI(title="Smart Document Processor API")

@app.get("/", tags=["Health"])
def read_root():
    # Simple health check, matches the image output you shared
    return {"message": "API is running. Access /docs for the Swagger UI."}

# Define the main API endpoint (RESTful API, File Upload)
@app.post("/extract-data/", response_model=DocumentSummary, tags=["Document Processing"])
async def extract_data_from_document(file: UploadFile = File(..., description="A document file (PDF, Markdown, or TXT) to process.")):
    if not file.filename:
         raise HTTPException(status_code=400, detail="No file provided")
    
    # Call the asynchronous service function
    summary = await process_document(file)
    return summary