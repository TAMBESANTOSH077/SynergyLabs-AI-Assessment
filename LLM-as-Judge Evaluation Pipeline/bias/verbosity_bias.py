class VerbosityBias:

    @staticmethod
    def detect(answer_a, answer_b):

        len_a = len(answer_a.split())

        len_b = len(answer_b.split())

        return {
            "length_a": len_a,
            "length_b": len_b,
            "difference": abs(len_a - len_b)
        }