from typing import Optional
from pydantic import BaseModel


class EvaluationRequest(BaseModel):

    question: str

    answer: str

    reference_answer: Optional[str] = None

    candidate_a: Optional[str] = None

    candidate_b: Optional[str] = None


class JudgeScore(BaseModel):

    correctness: float

    relevance: float

    completeness: float

    fluency: float

    overall: float

    confidence: float

    reasoning: str


class PairwiseResult(BaseModel):

    winner: str

    confidence: float

    reasoning: str