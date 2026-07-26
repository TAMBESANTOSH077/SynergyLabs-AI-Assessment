from embeddings.embedding_model import EmbeddingModel
import traceback


def get_embeddings(documents):
    """
    Generate embeddings for multiple documents.
    """

    try:

        if documents is None:
            raise ValueError("Documents cannot be None.")

        if not isinstance(documents, list):
            raise TypeError("Documents must be a list.")

        if len(documents) == 0:
            return []

        return EmbeddingModel.embed_documents(documents)

    except Exception as e:

        traceback.print_exc()

        raise RuntimeError(
            f"Failed to generate document embeddings: {e}"
        )


def get_query_embedding(query):
    """
    Generate embedding for a single query.
    """

    try:

        if query is None:
            raise ValueError("Query cannot be None.")

        if not isinstance(query, str):
            raise TypeError("Query must be a string.")

        query = query.strip()

        if not query:
            raise ValueError("Query cannot be empty.")

        return EmbeddingModel.embed_query(query)

    except Exception as e:

        traceback.print_exc()

        raise RuntimeError(
            f"Failed to generate query embedding: {e}"
        )