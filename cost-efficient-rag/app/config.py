from dotenv import load_dotenv
import os

load_dotenv()

# ==========================
# API Keys
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

# ==========================
# Vector Database
# ==========================

CHROMA_DB_PATH = os.getenv(
    "CHROMA_DB_PATH",
    "data/vector_store"
)

# ==========================
# Embedding Model
# ==========================

EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "all-MiniLM-L6-v2"
)

# ==========================
# Chunk Settings
# ==========================

CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", "500")
)

CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", "50")
)

# ==========================
# Retrieval
# ==========================

TOP_K = int(
    os.getenv("TOP_K", "5")
)