from judge.pointwise import PointwiseJudge


class ReferenceBasedJudge:

    def evaluate(
        self,
        question,
        reference_answer,
        candidate_answer
    ):

        combined = f"""
Reference Answer:
{reference_answer}

Candidate Answer:
{candidate_answer}
"""

        return PointwiseJudge().evaluate(
            question,
            combined
        )