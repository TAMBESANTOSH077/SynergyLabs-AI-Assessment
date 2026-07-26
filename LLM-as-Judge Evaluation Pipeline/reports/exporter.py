import json
import pandas as pd


class Exporter:

    @staticmethod
    def csv(result):

        df = pd.DataFrame([result])

        df.to_csv(
            "reports/result.csv",
            index=False
        )

    @staticmethod
    def excel(result):

        df = pd.DataFrame([result])

        df.to_excel(
            "reports/result.xlsx",
            index=False
        )

    @staticmethod
    def json(result):

        with open(
            "reports/result.json",
            "w"
        ) as f:

            json.dump(
                result,
                f,
                indent=4
            )