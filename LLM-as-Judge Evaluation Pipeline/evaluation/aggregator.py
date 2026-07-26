from typing import List
from judge.schemas import JudgeScore


class Aggregator:

    @staticmethod
    def average(scores: List[JudgeScore]):

        if not scores:
            raise ValueError("No scores provided.")

        n = len(scores)

        return {
            "correctness": sum(s.correctness for s in scores) / n,
            "relevance": sum(s.relevance for s in scores) / n,
            "completeness": sum(s.completeness for s in scores) / n,
            "fluency": sum(s.fluency for s in scores) / n,
            "overall": sum(s.overall for s in scores) / n,
            "confidence": sum(s.confidence for s in scores) / n,
        }