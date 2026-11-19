# 🚀 SynergyLabs AI Assessment

This repository contains solutions for two AI Engineering problems using **Python**, **FastAPI**, **Streamlit**, **Google Gemini**, **OpenAI**, and **ChromaDB**.

## 📂 Projects

### 📌 Problem 1 – Cost-Efficient RAG

A Retrieval-Augmented Generation (RAG) system that answers questions from PDF documents using semantic search and Google Gemini.

**Key Features**
- PDF Upload & Processing
- Semantic Search
- ChromaDB Vector Database
- Citation-Based Responses
- FastAPI REST APIs

📁 Folder: `cost-efficient-rag`

---

### 📌 Problem 2 – LLM-as-Judge Evaluation Pipeline

An evaluation framework that scores AI-generated responses using Large Language Models.

**Key Features**
- Pointwise Evaluation
- Pairwise Evaluation
- JSON Validation
- Bias Detection
- Streamlit Dashboard

📁 Folder: `LLM-as-Judge Evaluation Pipeline`

---

## 🛠️ Tech Stack

- Python
- FastAPI
- Streamlit
- LangChain
- ChromaDB
- Google Gemini
- OpenAI
- Docker

---

## 📁 Repository Structure

```text
SynergyLabs-AI-Assessment/
│
├── cost-efficient-rag/
├── LLM-as-Judge Evaluation Pipeline/
├── docs/
├── demo/
└── README.md
```

---

## 🚀 Getting Started

### Clone the Repository

```bash
git clone https://github.com/TAMBESANTOSH077/SynergyLabs-AI-Assessment.git
cd SynergyLabs-AI-Assessment
```

### Run Problem 1

```bash
cd cost-efficient-rag
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Run Problem 2

```bash
cd "LLM-as-Judge Evaluation Pipeline"
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run streamlit_app.py
```

---

## 📄 Documentation

Project reports and architecture diagrams are available in the `docs/` folder.

## 📸 Demo

Screenshots and demo images are available in the `demo/` folder.

---

## 👨‍💻 Author

**Santosh Tambe**

GitHub: https://github.com/TAMBESANTOSH077

---

⭐ If you found this repository useful, consider giving it a star!
