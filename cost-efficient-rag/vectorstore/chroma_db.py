import os
import traceback
import chromadb

from app.config import CHROMA_DB_PATH


class ChromaDB:
    """
    Singleton ChromaDB connection.
    """

    _client = None
    _collection = None

    @classmethod
    def get_collection(cls):

        try:

            if cls._client is None:

                os.makedirs(CHROMA_DB_PATH, exist_ok=True)

                cls._client = chromadb.PersistentClient(
                    path=CHROMA_DB_PATH
                )

            if cls._collection is None:

                cls._collection = cls._client.get_or_create_collection(
                    name="rag_chunks",
                    metadata={
                        "hnsw:space": "cosine"
                    }
                )

            return cls._collection

        except Exception as e:

            traceback.print_exc()

            raise RuntimeError(
                f"Failed to initialize ChromaDB: {e}"
            )

    @classmethod
    def reset_collection(cls):
        """
        Deletes and recreates the collection.
        Useful during testing.
        """

        try:

            client = chromadb.PersistentClient(
                path=CHROMA_DB_PATH
            )

            try:
                client.delete_collection("rag_chunks")
            except Exception:
                pass

            cls._collection = client.get_or_create_collection(
                name="rag_chunks",
                metadata={
                    "hnsw:space": "cosine"
                }
            )

            cls._client = client

            return cls._collection

        except Exception as e:

            traceback.print_exc()

            raise RuntimeError(
                f"Failed to reset ChromaDB: {e}"
            )