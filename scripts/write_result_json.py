"""Convert pytest-json-report output into Classroom50 result.json.

The generated result.json is intentionally simple and Gradescope-like:
- score: points earned
- max_score: maximum points
- output: short summary
- tests: one entry per pytest test
"""

from __future__ import annotations

import json
from pathlib import Path

MAX_SCORE = 1.0
REPORT_PATH = Path("pytest-report.json")
RESULT_PATH = Path("result.json")


def status_for(outcome: str) -> str:
    return "passed" if outcome == "passed" else "failed"


def main() -> None:
    if not REPORT_PATH.exists():
        RESULT_PATH.write_text(
            json.dumps(
                {
                    "score": 0.0,
                    "max_score": MAX_SCORE,
                    "output": "pytest did not produce pytest-report.json. The tests may not have run.",
                    "tests": [],
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return

    report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    tests = report.get("tests", [])
    total = len(tests)
    passed = sum(1 for test in tests if test.get("outcome") == "passed")
    score = round(MAX_SCORE * passed / total, 4) if total else 0.0
    per_test_max = round(MAX_SCORE / total, 4) if total else 0.0

    result_tests = []
    for test in tests:
        outcome = test.get("outcome", "failed")
        message_parts = []
        call = test.get("call") or {}
        if call.get("crash"):
            crash = call["crash"]
            message_parts.append(f"{crash.get('path', '')}:{crash.get('lineno', '')} {crash.get('message', '')}".strip())
        if test.get("longrepr"):
            message_parts.append(str(test["longrepr"])[:1200])
        result_tests.append(
            {
                "name": test.get("nodeid", "pytest test"),
                "score": per_test_max if outcome == "passed" else 0.0,
                "max_score": per_test_max,
                "status": status_for(outcome),
                "output": "\n".join(part for part in message_parts if part) or outcome,
            }
        )

    result = {
        "score": score,
        "max_score": MAX_SCORE,
        "output": f"{passed} of {total} pytest tests passed.",
        "tests": result_tests,
    }
    RESULT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
