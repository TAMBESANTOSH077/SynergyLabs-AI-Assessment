import matplotlib.pyplot as plt


class Charts:

    @staticmethod
    def radar(result):

        labels = [
            "Correctness",
            "Relevance",
            "Completeness",
            "Fluency"
        ]

        values = [
            result["correctness"],
            result["relevance"],
            result["completeness"],
            result["fluency"]
        ]

        plt.figure(figsize=(6,4))

        plt.bar(labels, values)

        plt.ylim(0,10)

        plt.savefig(
            "reports/score_chart.png"
        )

        plt.close()