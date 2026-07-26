from judge.pairwise import PairwiseJudge


class PositionBias:

    def check(
        self,
        question,
        answer_a,
        answer_b
    ):

        judge = PairwiseJudge()

        first = judge.evaluate(
            question,
            answer_a,
            answer_b
        )

        second = judge.evaluate(
            question,
            answer_b,
            answer_a
        )

        return {
            "first": first,
            "second": second,
            "bias_detected":
                first.winner == second.winner
        }