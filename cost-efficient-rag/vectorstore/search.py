from vectorstore.chroma_db import ChromaDB
from embeddings.embedding_utils import get_query_embedding
import traceback


class VectorSearch:

    def __init__(self):

        self.collection = ChromaDB.get_collection()

        if self.collection is None:
            raise RuntimeError(
                "Failed to initialize ChromaDB collection."
            )

    def search(
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

            embedding = get_query_embedding(query)

            if embedding is None:
                raise RuntimeError(
                    "Query embedding generation failed."
                )

            results = self.collection.query(
                query_embeddings=[embedding],
                n_results=top_k,
                where=metadata if metadata else None
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
                f"Vector Search failed: {e}"
            )