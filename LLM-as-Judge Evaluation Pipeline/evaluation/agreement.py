class Agreement:

    @staticmethod
    def percent(labels1, labels2):

        if len(labels1) != len(labels2):
            raise ValueError("Lengths differ.")

        matches = sum(a == b for a, b in zip(labels1, labels2))

        return matches / len(labels1)