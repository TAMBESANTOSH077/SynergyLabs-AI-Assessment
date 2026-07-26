class SelfEnhancement:

    @staticmethod
    def detect(model_a, model_b, winner):

        return {
            "self_enhancement":
                winner == model_a
        }