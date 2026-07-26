from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
import traceback

from ingestion.ingest_pipeline import IngestionPipeline
from rag.rag_pipeline import RAGPipeline
from api.request_models import QueryRequest
from api.response_models import QueryResponse

router = APIRouter()

pipeline = IngestionPipeline()
rag = RAGPipeline()


# ==========================
# Health Check
# ==========================

@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "Cost Efficient RAG API"
    }


# ==========================
# Upload PDF
# ==========================

@router.post("/ingest")
async def ingest(file: UploadFile = File(...)):

    try:

        if not file.filename:
            raise HTTPException(status_code=400, detail="No file selected.")

        if not file.filename.lower().endswith(".pdf"):
            raise HTTPException(status_code=400, detail="Only PDF files are allowed.")

        os.makedirs("data/raw_documents", exist_ok=True)

        file_path = os.path.join(
            "data",
            "raw_documents",
            file.filename
        )

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        chunks = pipeline.ingest(file_path)

        return {
            "success": True,
            "document": file.filename,
            "chunks": len(chunks),
            "message": "Document indexed successfully."
        }

    except HTTPException:
        raise

    except Exception:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail="Document ingestion failed."
        )


# ==========================
# Ask Question
# ==========================

@router.post(
    "/query",
    response_model=QueryResponse
)
async def query(request: QueryRequest):

    try:

        if not request.query.strip():
            raise HTTPException(
                status_code=400,
                detail="Question cannot be empty."
            )

        result = rag.ask(
            question=request.query,
            top_k=request.top_k
        )

        if result is None:

            raise HTTPException(
                status_code=500,
                detail="RAG returned None."
            )

        return result

    except HTTPException:
        raise

    except Exception:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail="Internal Server Error. Check terminal for traceback."
        )