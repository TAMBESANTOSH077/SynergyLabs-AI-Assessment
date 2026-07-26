# 🧑‍⚖️ LLM-as-Judge Evaluation Pipeline

A production-ready **LLM-as-Judge Evaluation Framework** built with **FastAPI** that evaluates Large Language Model (LLM) responses using multiple judging strategies, bias analysis, structured parsing, evaluation metrics, and automated reporting.

The framework supports **Pointwise**, **Pairwise**, **Reference-Based**, and **Reference-Free** evaluation while providing JSON validation, bias detection, agreement metrics, experiment logging, and report generation.

---

# ✨ Features

- ✅ Pointwise Evaluation
- ✅ Pairwise Evaluation
- ✅ Reference-Based Evaluation
- ✅ Reference-Free Evaluation
- ✅ Structured JSON Output Parsing
- ✅ Automatic JSON Repair
- ✅ Pydantic Validation
- ✅ Position Bias Detection
- ✅ Verbosity Bias Detection
- ✅ Self Enhancement Bias
- ✅ Sycophancy Detection
- ✅ Score Clustering Detection
- ✅ Agreement Metrics
- ✅ Cohen's Kappa
- ✅ Batch Evaluation
- ✅ Report Generation
- ✅ Charts & Visualizations
- ✅ Logging System
- ✅ REST API using FastAPI
- ✅ Docker Support
- ✅ GitHub Actions CI
- ✅ Unit & API Testing

---

# 🏗️ Architecture

```
                    Client
                      │
                      ▼
                FastAPI API
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
 Pointwise Judge             Pairwise Judge
         │                         │
         └────────────┬────────────┘
                      ▼
            Prompt Construction
                      ▼
           LLM Provider Layer
        (Gemini / OpenAI / etc.)
                      ▼
          JSON Repair & Parser
                      ▼
          Pydantic Validation
                      ▼
             Bias Detection
                      ▼
          Evaluation Metrics
                      ▼
           Report Generation
                      ▼
        JSON | HTML | CSV | Excel
```

---

# 📂 Project Structure

```
llm-as-judge/
│
├── app/
│   ├── main.py
│   ├── config.py
│   └── logger.py
│
├── providers/
│
├── judge/
│
├── parser/
│
├── bias/
│
├── evaluation/
│
├── reports/
│
├── cache/
│
├── datasets/
│
├── experiments/
│
├── logs/
│
├── test_suites/
│
├── tests/
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/llm-as-judge.git

cd llm-as-judge
```

Create virtual environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ⚙️ Environment Variables

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY

OPENAI_API_KEY=

MODEL_NAME=gemini-2.5-flash

TEMPERATURE=0

MAX_TOKENS=1024
```

---

# ▶️ Running the Application

```bash
uvicorn app.main:app --reload
```

Application

```
http://127.0.0.1:8000
```

Swagger Documentation

```
http://127.0.0.1:8000/docs
```

---

# 📌 API Endpoints

## Health

```
GET /health
```

---

## Pointwise Evaluation

```
POST /evaluate
```

Request

```json
{
  "question":"What is AI?",
  "answer":"Artificial Intelligence is..."
}
```

---

## Pairwise Evaluation

```
POST /pairwise
```

Request

```json
{
  "question":"Explain Python",
  "candidate_a":"Python is a programming language.",
  "candidate_b":"Python is a snake."
}
```

---

## Batch Evaluation

```
POST /batch
```

---

## Generate Report

```
POST /report
```

---

# 📊 Evaluation Strategies

## Pointwise

Evaluates a single answer based on

- Correctness
- Relevance
- Completeness
- Fluency

---

## Pairwise

Compares two candidate responses and selects the better one.

---

## Reference-Based

Uses a gold reference answer for comparison.

---

## Reference-Free

Evaluates answers without requiring a reference.

---

# 📈 Bias Detection

The framework detects several evaluation biases.

- Position Bias
- Verbosity Bias
- Self Enhancement Bias
- Sycophancy
- Score Clustering

---

# 📊 Metrics

Supported metrics

- Accuracy
- Precision
- Recall
- F1 Score
- Cohen's Kappa
- Agreement Percentage

---

# 📁 Logs

The framework automatically stores

```
logs/

prompts/

raw_responses/

parsed_results/

metrics/

reports/

errors/
```

---

# 🧪 Test Suites

Included benchmark datasets

- QA
- Coding
- Mathematics
- Hallucination
- Adversarial
- Pairwise
- Gold Labels

---

# ✅ Running Tests

```bash
pytest
```

Coverage

```bash
pytest --cov=.
```

---

# 📊 Generated Reports

The framework exports

- Markdown
- HTML
- JSON
- CSV
- Excel

---

# 🐳 Docker

Build

```bash
docker compose up --build
```

---

# 🔧 Tech Stack

- Python
- FastAPI
- Google Gemini
- OpenAI
- Pydantic
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Plotly
- ReportLab
- Pytest
- Docker

---

# 📌 Future Improvements

- LangSmith Integration
- LiteLLM Support
- MLflow Experiment Tracking
- OpenTelemetry Tracing
- Streamlit Dashboard
- Human Evaluation Interface
- Multi-Judge Consensus
- Prompt Versioning
- Model Benchmark Leaderboard

---

# 👨‍💻 Author

**Santosh Tambe**

AI Engineer | Python Developer | Generative AI | FastAPI | LangChain | LLM Applications

GitHub:
https://github.com/TAMBESANTOSH077

LinkedIn:
https://linkedin.com/in/your-profile

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.