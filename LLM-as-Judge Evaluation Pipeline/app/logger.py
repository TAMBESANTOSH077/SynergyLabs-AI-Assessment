# app/logger.py

import json
import os
from datetime import datetime

os.makedirs("logs/prompts", exist_ok=True)
os.makedirs("logs/raw_responses", exist_ok=True)
os.makedirs("logs/parsed_results", exist_ok=True)


class JudgeLogger:

    @staticmethod
    def save(folder, data):

        filename = datetime.now().strftime(
            "%Y%m%d_%H%M%S_%f.json"
        )

        with open(
            f"logs/{folder}/{filename}",
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )