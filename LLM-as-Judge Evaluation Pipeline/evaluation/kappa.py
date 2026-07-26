from sklearn.metrics import cohen_kappa_score


class Kappa:

    @staticmethod
    def compute(human, llm):

        return {
            "cohen_kappa": cohen_kappa_score(
                human,
                llm
            )
        }