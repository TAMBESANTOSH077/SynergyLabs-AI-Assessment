



import google.generativeai as genai

from app.config import GOOGLE_API_KEY, MODEL_NAME

from judge.prompts import POINTWISE_PROMPT

from parser.json_parser import JSONParser

from parser.validator import Validator


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)

class PointwiseJudge:

    def evaluate(self, question: str, answer: str):

        try:
            prompt = POINTWISE_PROMPT.format(
                question=question,
                answer=answer
            )

            response = model.generate_content(prompt)

            print("========== RAW RESPONSE ==========")
            print(response.text)

            parsed = JSONParser.parse(response.text)

            print("========== PARSED ==========")
            print(parsed)

            return Validator.validate_pointwise(parsed)

        except Exception as e:
            import traceback
            traceback.print_exc()
            return {"error": str(e)}