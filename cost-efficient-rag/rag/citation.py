import traceback


class CitationFormatter:
    """
    Formats retrieved document metadata into clean citations.
    """

    def format(self, metadatas):

        try:

            if not metadatas:
                return []

            if not isinstance(metadatas, list):
                raise TypeError(
                    "Metadata must be a list."
                )

            citations = []
            seen = set()

            for item in metadatas:

                if not isinstance(item, dict):
                    continue

                source = item.get("source", "Unknown")
                chunk = item.get("chunk", 0)
                file_type = item.get("file_type", "unknown")
                page = item.get("page")

                key = (source, chunk)

                if key in seen:
                    continue

                seen.add(key)

                citation = {
                    "source": source,
                    "chunk": chunk,
                    "file_type": file_type
                }

                if page is not None:
                    citation["page"] = page

                citations.append(citation)

            return citations

        except Exception as e:

            traceback.print_exc()

            raise RuntimeError(
                f"Citation formatting failed: {e}"
            )