import json
from datetime import datetime


class ReportGenerator:

    @staticmethod
    def markdown(result: dict):

        md = f"""
# LLM-as-Judge Evaluation Report

Generated:
{datetime.now()}

---

## Overall Score

{result['overall']:.2f}

---

## Metrics

| Metric | Score |
|--------|------|
| Correctness | {result['correctness']:.2f} |
| Relevance | {result['relevance']:.2f} |
| Completeness | {result['completeness']:.2f} |
| Fluency | {result['fluency']:.2f} |

---

## Confidence

{result['confidence']:.2f}

---

## Reasoning

{result.get("reasoning","")}
"""

        return md

    @staticmethod
    def json(result):

        return json.dumps(
            result,
            indent=4
        )

    @staticmethod
    def html(result):

        return f"""
<html>
<head>
<title>LLM Evaluation Report</title>
</head>

<body>

<h1>Evaluation Report</h1>

<h2>Overall : {result['overall']:.2f}</h2>

<ul>

<li>Correctness : {result['correctness']}</li>

<li>Relevance : {result['relevance']}</li>

<li>Completeness : {result['completeness']}</li>

<li>Fluency : {result['fluency']}</li>

<li>Confidence : {result['confidence']}</li>

</ul>

<p>{result.get("reasoning","")}</p>

</body>
</html>
"""