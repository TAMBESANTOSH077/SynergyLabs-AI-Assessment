from pathlib import Path


class MarkdownLoader:

    def load(self, file_path: str):

        with open(file_path, "r", encoding="utf-8") as file:

            text = file.read()

        return {

            "file_name": Path(file_path).name,

            "file_type": "md",

            "text": text

        }