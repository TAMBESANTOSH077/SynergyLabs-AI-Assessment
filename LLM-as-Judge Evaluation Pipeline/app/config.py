from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = os.getenv(
    "MODEL_NAME",
    "gemini-2.5-flash"
)

TEMPERATURE = float(
    os.getenv("TEMPERATURE", "0")
)

MAX_TOKENS = int(
    os.getenv("MAX_TOKENS", "1024")
)