import google.generativeai as genai

from app.config import GOOGLE_API_KEY, MODEL_NAME

from judge.prompts import PAIRWISE_PROMPT

from parser.json_parser import JSONParser

from parser.validator import Validator


genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(MODEL_NAME)


class PairwiseJudge:

    def evaluate(
        self,
        question,
        answer_a,
        answer_b
    ):

        prompt = PAIRWISE_PROMPT.format(
            question=question,
            answer_a=answer_a,
            answer_b=answer_b
        )

        response = model.generate_content(prompt)

        parsed = JSONParser.parse(response.text)

        return Validator.validate_pairwise(parsed)