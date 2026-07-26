from json_repair import repair_json


def repair(response: str) -> str:
    """
    Repairs malformed JSON returned by an LLM.
    """
    return repair_json(response)