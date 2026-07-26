from pathlib import Path
from pypdf import PdfReader
import traceback


class PDFLoader:
    """
    Loads PDF documents and extracts text page by page.
    """

    def load(self, file_path: str) -> dict:

        pdf_path = Path(file_path)

        if not pdf_path.exists():
            raise FileNotFoundError(
                f"PDF not found: {file_path}"
            )

        if pdf_path.suffix.lower() != ".pdf":
            raise ValueError(
                f"{file_path} is not a PDF file."
            )

        try:

            reader = PdfReader(str(pdf_path))

        except Exception as e:

            traceback.print_exc()

            raise RuntimeError(
                f"Unable to open PDF: {e}"
            )

        pages = []

        for page_number, page in enumerate(reader.pages, start=1):

            try:

                text = page.extract_text()

                if text is None:
                    text = ""

                text = text.strip()

            except Exception:

                traceback.print_exc()

                text = ""

            pages.append(
                {
                    "page": page_number,
                    "text": text
                }
            )

        if len(pages) == 0:
            raise RuntimeError(
                "The PDF contains no readable pages."
            )

        return {
            "file_name": pdf_path.name,
            "file_type": "pdf",
            "pages": pages
        }