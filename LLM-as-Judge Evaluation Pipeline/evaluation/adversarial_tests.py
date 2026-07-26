import json


class AdversarialSuite:

    def __init__(self, file_path):

        with open(file_path, "r", encoding="utf-8") as f:

            self.tests = json.load(f)

    def get_all(self):

        return self.tests