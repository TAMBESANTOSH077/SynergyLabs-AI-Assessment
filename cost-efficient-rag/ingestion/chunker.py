from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.config import CHUNK_SIZE, CHUNK_OVERLAP


class Chunker:

    def __init__(self):

        if CHUNK_OVERLAP >= CHUNK_SIZE:
            raise ValueError(
                "CHUNK_OVERLAP must be smaller than CHUNK_SIZE."
            )

        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                ""
            ]
        )

    def split(self, text: str):

        if not text:
            return []

        return self.splitter.split_text(text)