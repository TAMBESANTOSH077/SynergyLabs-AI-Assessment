from unittest.mock import patch
from judge.pointwise import PointwiseJudge


@patch("judge.pointwise.model.generate_content")
def test_pointwise(mock_generate):
    mock_generate.return_value.text = """
    {
        "correctness":10,
        "relevance":10,
        "completeness":9,
        "fluency":9,
        "overall":9.5,
        "confidence":0.95,
        "reasoning":"Excellent"
    }
    """

    result = PointwiseJudge().evaluate(
        "What is AI?",
        "Artificial Intelligence"
    )

    assert result.overall == 9.5