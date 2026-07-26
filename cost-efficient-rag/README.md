# Cost Efficient RAG

## Overview

Cost Efficient RAG is a Retrieval-Augmented Generation system that enables users to query documents using Large Language Models while minimizing inference cost.

The system supports PDF, Markdown, and HTML documents and uses semantic search with ChromaDB before generating responses using Google Gemini.

---

## Features

- PDF, Markdown & HTML ingestion
- Intelligent text chunking
- SentenceTransformer embeddings
- ChromaDB vector database
- Google Gemini integration
- Source citation
- Evaluation metrics
- FastAPI REST API

---

## Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- Sentence Transformers
- Google Gemini
- HuggingFace
- NumPy
- Pydantic

---

## Folder Structure

```text
app/
api/
ingestion/
embeddings/
vectorstore/
rag/
evaluation/
tests/
docs/
```

---

## Installation

```bash
git clone <your-github-url>

cd cost-efficient-rag

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| POST | /ingest | Upload Documents |
| POST | /query | Ask Questions |

---

## Evaluation

- Latency Measurement
- Retrieval Metrics
- Answer Metrics

---

## Future Improvements

- Multi-document RAG
- Hybrid Search
- Redis Cache
- Authentication
- Streaming Responses

---

## Author

Santosh Tambe