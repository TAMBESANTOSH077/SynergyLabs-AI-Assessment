from sentence_transformers import SentenceTransformer
from app.config import EMBEDDING_MODEL
import traceback


class EmbeddingModel:

    _model = None

    @classmethod
    def get_model(cls):

        if cls._model is None:

            try:
                print(f"Loading Embedding Model: {EMBEDDING_MODEL}")

                cls._model = SentenceTransformer(
                    EMBEDDING_MODEL,
                    device="cpu"
                )

            except Exception as e:
                traceback.print_exc()
                raise RuntimeError(
                    f"Failed to load embedding model: {e}"
                )

        return cls._model

    @classmethod
    def embed_documents(cls, documents):

        if not documents:
            return []

        try:

            model = cls.get_model()

            embeddings = model.encode(
                documents,
                normalize_embeddings=True,
                show_progress_bar=False,
                convert_to_numpy=True
            )

            return embeddings.tolist()

        except Exception as e:
            traceback.print_exc()
            raise RuntimeError(
                f"Embedding generation failed: {e}"
            )

    @classmethod
    def embed_query(cls, query):

        if not query or not query.strip():
            raise ValueError("Query cannot be empty.")

        try:

            model = cls.get_model()

            embedding = model.encode(
                query,
                normalize_embeddings=True,
                convert_to_numpy=True
            )

            return embedding.tolist()

        except Exception as e:
            traceback.print_exc()
            raise RuntimeError(
                f"Query embedding failed: {e}"
            )