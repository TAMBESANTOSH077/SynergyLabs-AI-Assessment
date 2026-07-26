import json
from parser.repair import repair


class JSONParser:

    @staticmethod
    def parse(text: str):

        try:
            return json.loads(text)

        except Exception:

            repaired = repair(text)

            return json.loads(repaired)