import numpy as np


class ScoreClustering:

    @staticmethod
    def detect(scores):

        std = np.std(scores)

        return {
            "std": float(std),
            "clustered": std < 0.5
        }