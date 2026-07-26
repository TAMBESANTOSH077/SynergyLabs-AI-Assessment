from vectorstore.search import VectorSearch
import traceback


class Retriever:
    """
    Retrieves the most relevant chunks from the vector database.
    """

    def __init__(self):
        self.search_engine = VectorSearch()

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        metadata: dict | None = None
    ):

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        if top_k <= 0:
            top_k = 5

        try:

            results = self.search_engine.search(
                query=query.strip(),
                top_k=top_k,
                metadata=metadata
            )

            if not results:
                return {
                    "documents": [[]],
                    "metadatas": [[]],
                    "distances": [[]]
                }

            results.setdefault("documents", [[]])
            results.setdefault("metadatas", [[]])
            results.setdefault("distances", [[]])

            return results

        except Exception as e:

            traceback.print_exc()

            raise RuntimeError(
                f"Retriever failed: {str(e)}"
            )