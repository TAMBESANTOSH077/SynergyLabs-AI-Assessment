from pathlib import Path
import traceback

from ingestion.pdf_loader import PDFLoader
from ingestion.html_loader import HTMLLoader
from ingestion.markdown_loader import MarkdownLoader
from ingestion.chunker import Chunker
from ingestion.chunk_hash import generate_chunk_hash

from embeddings.embedding_utils import get_embeddings
from vectorstore.store import VectorStore


class IngestionPipeline:

    def __init__(self):

        self.pdf_loader = PDFLoader()
        self.html_loader = HTMLLoader()
        self.md_loader = MarkdownLoader()

        self.chunker = Chunker()

        self.vector_store = VectorStore()

    def ingest(self, file_path):

        try:

            file_path = Path(file_path)

            if not file_path.exists():
                raise FileNotFoundError(
                    f"{file_path} does not exist."
                )

            suffix = file_path.suffix.lower()

            if suffix == ".pdf":

                document = self.pdf_loader.load(str(file_path))

                text = "\n".join(
                    page.get("text", "")
                    for page in document["pages"]
                    if page.get("text")
                )

                file_type = "pdf"

            elif suffix == ".html":

                document = self.html_loader.load(str(file_path))

                text = document.get("text", "")

                file_type = "html"

            elif suffix == ".md":

                document = self.md_loader.load(str(file_path))

                text = document.get("text", "")

                file_type = "md"

            else:
                raise ValueError(
                    f"Unsupported file type: {suffix}"
                )

            if not text.strip():
                raise ValueError(
                    "Document contains no readable text."
                )

            chunks = self.chunker.split(text)

            if not chunks:
                raise ValueError(
                    "No chunks generated."
                )

            ids = []
            documents = []
            metadatas = []

            for index, chunk in enumerate(chunks):

                chunk_id = generate_chunk_hash(
                    document["file_name"],
                    index,
                    chunk
                )

                ids.append(chunk_id)

                documents.append(chunk)

                metadatas.append(
                    {
                        "source": document["file_name"],
                        "chunk": index,
                        "file_type": file_type
                    }
                )

            embeddings = get_embeddings(documents)

            self.vector_store.add_documents(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas
            )

            return chunks

        except Exception as e:

            traceback.print_exc()

            raise RuntimeError(
                f"Ingestion failed: {e}"
            )