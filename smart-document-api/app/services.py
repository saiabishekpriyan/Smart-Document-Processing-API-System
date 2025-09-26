# app/services.py
import io
import pypdf
from fastapi import UploadFile
from typing import List
from .models import DocumentSummary, ExtractedFact

# --- AI/NLP SETUP ---
# This executes once when the server starts
try:
    import spacy
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    print(f"Warning: Failed to load spaCy model: {e}")
    nlp = None

def _parse_pdf(file_content: bytes) -> str:
    """Extracts text from a PDF."""
    text = ""
    try:
        reader = pypdf.PdfReader(io.BytesIO(file_content))
        for page in reader.pages:
            text += page.extract_text() or ""
    except Exception:
        text = "PDF parsing failed."
    return text

def _apply_ai_extraction(text: str) -> List[ExtractedFact]:
    """Uses NLP/AI to extract structured data (NER and custom skills)."""
    facts = []
    
    # 1. SpaCy Named Entity Recognition (NER)
    if nlp:
        doc = nlp(text)
        for ent in doc.ents:
            facts.append(ExtractedFact(key=ent.label_, value=ent.text))
    
    # 2. Simple custom keyword extraction
    skills = ["Python", "FastAPI", "API", "NLP", "Git", "AI"]
    found_skills = set()
    for skill in skills:
        if skill.lower() in text.lower():
            found_skills.add(skill)
            
    if found_skills:
        facts.append(ExtractedFact(key="Skills_Found", value=", ".join(sorted(list(found_skills)))))

    return facts

# Main asynchronous entry point
async def process_document(file: UploadFile) -> DocumentSummary:
    
    # Use await for asynchronous file read (async/await requirement)
    file_content = await file.read() 
    
    doc_text = ""
    file_type = "Generic Text"
    filename = file.filename or "uploaded_file"
    
    # Determine file type and parse
    if filename.endswith(".pdf"):
        file_type = "PDF"
        doc_text = _parse_pdf(file_content)
        
    elif filename.endswith(".md"):
        file_type = "Markdown"
        doc_text = file_content.decode('utf-8', errors='ignore')
        
    else:
        doc_text = file_content.decode('utf-8', errors='ignore')
        
    # Apply AI/NLP for Extraction
    extracted_data = _apply_ai_extraction(doc_text)
    
    return DocumentSummary(
        original_filename=filename,
        document_type=file_type,
        extracted_data=extracted_data
    )