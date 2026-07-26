from pathlib import Path
from bs4 import BeautifulSoup


class HTMLLoader:

    def load(self, file_path: str):

        with open(file_path, "r", encoding="utf-8") as file:
            html = file.read()

        soup = BeautifulSoup(html, "html.parser")

        text = soup.get_text(separator="\n")

        return {

            "file_name": Path(file_path).name,

            "file_type": "html",

            "text": text

        }