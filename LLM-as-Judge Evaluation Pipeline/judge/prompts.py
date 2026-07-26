POINTWISE_PROMPT = """
You are an impartial AI evaluator.

Evaluate the candidate answer.

Question:
{question}

Candidate Answer:
{answer}

Return ONLY valid JSON.

{
    "correctness":0-10,
    "relevance":0-10,
    "completeness":0-10,
    "fluency":0-10,
    "overall":0-10,
    "confidence":0-1,
    "reasoning":"..."
}
"""


PAIRWISE_PROMPT = """
You are an impartial judge.

Question:
{question}

Answer A:
{answer_a}

Answer B:
{answer_b}

Return ONLY JSON.

{
"winner":"A/B/TIE",
"confidence":0-1,
"reasoning":"..."
}
"""