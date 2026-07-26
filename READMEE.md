# 🚀 SynergyLabs AI Assessment

> A collection of AI engineering projects demonstrating **Retrieval-Augmented Generation (RAG)** and **LLM Evaluation Pipelines** using modern Generative AI technologies.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?logo=streamlit)
![Google Gemini](https://img.shields.io/badge/Google-Gemini-blue?logo=google)
![OpenAI](https://img.shields.io/badge/OpenAI-API-black?logo=openai)
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-purple)

---

## 📖 Overview

This repository contains solutions for two AI engineering problems:

### 📌 Problem 1 — Cost-Efficient RAG System

A Retrieval-Augmented Generation (RAG) application that retrieves relevant information from PDF documents using semantic search and generates grounded responses with Google Gemini.

### 📌 Problem 2 — LLM-as-Judge Evaluation Pipeline

An AI evaluation framework that automatically evaluates Large Language Model (LLM) responses using pointwise and pairwise judging with structured JSON outputs.

---

# 📂 Repository Structure

```text
SynergyLabs-AI-Assessment/
│
├── Problem-1-Cost-Efficient-RAG/
├── Problem-2-LLM-as-Judge/
├── docs/
├── demo/
├── assets/
├── README.md
├── LICENSE
└── .gitignore
```

---

# 📌 Problem 1: Cost-Efficient RAG System

## Overview

The Cost-Efficient RAG System answers user questions based on uploaded PDF documents using semantic retrieval and Google's Gemini model.

### Features

- PDF Upload & Processing
- Semantic Search
- Vector Database (ChromaDB)
- Embedding Generation
- Source Citations
- FastAPI REST APIs
- Modular Architecture

### Tech Stack

- Python
- FastAPI
- LangChain
- ChromaDB
- Sentence Transformers
- Google Gemini 2.5 Flash
- Docker

📁 **Location**

```text
Problem-1-Cost-Efficient-RAG/
```

---

# 📌 Problem 2: LLM-as-Judge Evaluation Pipeline

## Overview

An evaluation framework that uses an LLM to score AI-generated responses using structured evaluation metrics.

### Features

- Pointwise Evaluation
- Pairwise Evaluation
- JSON Validation
- Bias Detection
- Streamlit Dashboard
- Report Generation

### Tech Stack

- Python
- FastAPI
- Streamlit
- Google Gemini
- OpenAI
- Pydantic
- JSON Repair

📁 **Location**

```text
Problem-2-LLM-as-Judge/
```

---

# 🛠 Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- ChromaDB
- Google Gemini
- OpenAI
- Docker
- Pydantic
- JSON Repair

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/TAMBESANTOSH077/SynergyLabs-AI-Assessment.git

cd SynergyLabs-AI-Assessment
```

---

## Problem 1

```bash
cd Problem-1-Cost-Efficient-RAG

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

## Problem 2

```bash
cd Problem-2-LLM-as-Judge

pip install -r requirements.txt

uvicorn app.main:app --reload

streamlit run streamlit_app.py
```

---

# 📸 Demo

Demo screenshots and outputs are available in:

```text
demo/
```

---

# 📄 Documentation

Project reports, architecture diagrams, and implementation details are available in:

```text
docs/
```

---

# 📈 Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Large Language Models (LLMs)
- Prompt Engineering
- FastAPI Development
- Streamlit Applications
- ChromaDB
- Vector Search
- REST APIs
- AI Evaluation
- Docker
- Python

---

# 🚀 Future Enhancements

### Cost-Efficient RAG

- Multi-document Retrieval
- Hybrid Search
- OCR Support
- Authentication
- Conversation Memory
- Multi-modal RAG

### LLM-as-Judge

- Multi-model Benchmarking
- Human Feedback Integration
- Explainable AI Metrics
- Leaderboards
- Batch Evaluation
- Dashboard Analytics

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Santosh Tambe**

- GitHub: https://github.com/TAMBESANTOSH077
- LinkedIn: *(Add your LinkedIn profile here)*

---

⭐ If you found this repository helpful, consider giving it a star!
