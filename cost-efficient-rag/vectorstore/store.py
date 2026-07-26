from vectorstore.chroma_db import ChromaDB
import traceback


class VectorStore:
    """
    Handles storing and retrieving vectors from ChromaDB.
    """

    def __init__(self):

        self.collection = ChromaDB.get_collection()

        if self.collection is None:
            raise RuntimeError("Failed to initialize ChromaDB collection.")

    def add_documents(
        self,
        ids,
        embeddings,
        documents,
        metadatas
    ):

        try:

            if not ids:
                raise ValueError("IDs cannot be empty.")

            if not embeddings:
                raise ValueError("Embeddings cannot be empty.")

            if not documents:
                raise ValueError("Documents cannot be empty.")

            if not metadatas:
                raise ValueError("Metadata cannot be empty.")

            if not (
                len(ids)
                == len(embeddings)
                == len(documents)
                == len(metadatas)
            ):
                raise ValueError(
                    "ids, embeddings, documents and metadatas must have the same length."
                )

            self.collection.upsert(
                ids=ids,
                embeddings=embeddings,
                documents=documents,
                metadatas=metadatas
            )

            return True

        except Exception as e:

            traceback.print_exc()

            raise RuntimeError(
                f"Failed to store documents: {e}"
            )

    def similarity_search(
        self,
        query_embedding,
        top_k=5
    ):

        try:

            if query_embedding is None:
                raise ValueError("Query embedding cannot be None.")

            if top_k <= 0:
                top_k = 5

            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
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
                f"Similarity search failed: {e}"
            )