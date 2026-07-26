from fastapi import FastAPI
from judge.schemas import EvaluationRequest
from judge.pointwise import PointwiseJudge
from judge.pairwise import PairwiseJudge


app = FastAPI(
    title="LLM-as-Judge",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "LLM-as-Judge API Running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }

pointwise = PointwiseJudge()
pairwise = PairwiseJudge()


@app.post("/evaluate")
def evaluate(req: EvaluationRequest):

    return pointwise.evaluate(
        req.question,
        req.answer
    )


@app.post("/pairwise")
def compare(req: EvaluationRequest):

    return pairwise.evaluate(
        req.question,
        req.candidate_a,
        req.candidate_b
    )