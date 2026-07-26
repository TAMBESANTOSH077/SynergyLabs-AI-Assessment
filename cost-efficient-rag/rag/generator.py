import google.generativeai as genai

from app.config import GEMINI_API_KEY


class Generator:
    """
    Gemini LLM Generator
    """

    def __init__(self):

        if not GEMINI_API_KEY:
            raise ValueError(
                "GEMINI_API_KEY is missing. Please check your .env file."
            )

        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash"
        )

    def generate(self, prompt: str) -> str:

        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty.")

        try:

            response = self.model.generate_content(prompt)

            if response is None:
                return "No response generated."

            if hasattr(response, "text") and response.text:
                return response.text.strip()

            if (
                hasattr(response, "candidates")
                and response.candidates
                and response.candidates[0].content.parts
            ):
                return response.candidates[0].content.parts[0].text.strip()

            return "No response generated."

        except Exception as e:
            print("\n========== GEMINI ERROR ==========")
            print(str(e))
            print("==================================\n")
            raise