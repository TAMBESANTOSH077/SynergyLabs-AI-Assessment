from judge.schemas import JudgeScore, PairwiseResult


class Validator:

    @staticmethod
    def validate_pointwise(data):

        return JudgeScore(**data)

    @staticmethod
    def validate_pairwise(data):

        return PairwiseResult(**data)