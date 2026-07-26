from parser.json_parser import JSONParser


def test_valid_json():
    text = '{"score": 9}'
    result = JSONParser.parse(text)
    assert result["score"] == 9


def test_repair_json():
    text = '{score:9}'
    result = JSONParser.parse(text)
    assert result["score"] == 9