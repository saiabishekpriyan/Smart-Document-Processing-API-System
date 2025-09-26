# Smart-Document-Processing-API-System
🚀 Project Overview
This project implements a high-performance backend API to process unstructured data from various documents (PDFs, Markdown, Text) and transform it into structured JSON data using AI/NLP techniques. It is designed to satisfy all the core requirements of a Python Developer (Internship) role, focusing on modern web development practices.

The system is built on FastAPI for a fast, asynchronous, and scalable service layer, leveraging Python's strengths in data processing and AI.

✨ Key Features & Technical Goals
Job Requirement	Project Component	Implementation Details
Solid Python Fundamentals	Entire Codebase, OOP Structure	Clean separation of concerns (API, Core Logic, Models) using Python classes and inheritance.
RESTful API with FastAPI	Main Backend Application	Defined endpoints for file upload and structured data extraction. Automatic Swagger documentation.
AI-Powered Systems	Core Extraction Logic	Integration with an NLP library (spaCy or NLTK) or an external/local LLM (e.g., via Ollama or OpenAI) for intelligent information extraction.
File Processing/Document Parsing	Document Handling Module	Logic to read and parse PDF (using pypdf/fitz) and Markdown documents.
JSON & Structured Data Modeling	Data Schemas	Extensive use of Pydantic to define clear request and response models, enforcing data integrity.
Bonus: Asynchronous Python	API Endpoints & I/O	Utilizes async/await throughout the FastAPI setup for non-blocking file I/O operations.
Bonus: Git, Debugging, Testing	Version Control & Quality	Standard Git workflow, includes pytest for unit/integration tests, and supports IDE debugging.

Export to Sheets
🛠️ Getting Started
Prerequisites
Python 3.10+

pip (Python package installer)

(Optional) Ollama running locally if using a local LLM for extraction.

Installation
Clone the repository:

Bash

git clone https://github.com/yourusername/smart-doc-processor.git
cd smart-doc-processor
Create and activate a virtual environment:

Bash

python -m venv venv
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate   # Windows
Install dependencies:

Bash

pip install -r requirements.txt
Note: If using a local LLM, you may need additional dependencies or configuration in app/core/extractor.py.

Running the API
Start the Uvicorn server:

Bash

uvicorn app.main:app --reload
The application will be accessible at http://127.0.0.1:8000.

Access Documentation:
The interactive API documentation (Swagger UI) is available at:
👉 http://127.0.0.1:8000/docs

⚙️ API Endpoints
1. POST /api/v1/document/process/
The primary endpoint for uploading and processing documents.

Parameter	Type	Description
file	File (Multipart)	The document to upload (.pdf, .md, .txt).

Export to Sheets
Success Response (200 OK):

JSON

{
  "filename": "annual_report.pdf",
  "document_type": "PDF",
  "structured_data": {
    "title": "Annual Report 2024",
    "key_metrics": [
      {"name": "Revenue", "value": "1.2B"},
      {"name": "Profit", "value": "150M"}
    ],
    "summary": "AI-generated summary of the document's content..."
  }
}
Error Response (400 Bad Request):

JSON

{
  "detail": "Unsupported document type or extraction failed."
}
📂 Project Structure
smart-doc-processor/
├── app/
│   ├── api/              # FastAPI Routers/Endpoints
│   │   └── document.py
│   ├── core/             # Core Business Logic (OOP)
│   │   ├── doc_parser.py   # Handles PDF/Markdown/Text reading
│   │   └── extractor.py    # Interfaces with AI/NLP model (spaCy/LLM)
│   ├── models/           # Pydantic Schemas for data validation
│   │   └── data_schema.py
│   └── main.py           # FastAPI Application Entry Point
├── tests/              # Unit and Integration Tests (using pytest)
├── .gitignore          
├── requirements.txt    # Project dependencies
└── README.md           # This file
🧪 Testing & Debugging
Running Tests
To ensure code reliability and cover all API paths and core extraction logic, run the test suite:

Bash

pytest
Debugging
The project is structured for easy debugging. Set breakpoints within the app/core/ service files using your IDE's built-in Python debugger to trace file parsing and AI extraction logic.

👤 Author & License
Author: [SaiAbishekPriyan S]

License: This project is available under the MIT License.