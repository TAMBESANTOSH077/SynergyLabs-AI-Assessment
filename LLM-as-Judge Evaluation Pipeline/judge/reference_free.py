from judge.pointwise import PointwiseJudge


class ReferenceFreeJudge:

    def evaluate(
        self,
        question,
        answer
    ):

        return PointwiseJudge().evaluate(
            question,
            answer
        )