"""Calculate the benchmark v4 human and AI weighted scores."""

import json
import sys
from pathlib import Path


def read_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def grades_for(source: dict, role: str, weights: dict) -> dict:
    grades = source.get(role)
    expected = {task for task, weight in weights.items() if weight > 0}
    if not isinstance(grades, dict) or set(grades) != expected:
        raise ValueError(f"{role}: expected grades for {', '.join(sorted(expected))}")
    for task, grade in grades.items():
        if type(grade) is not int or not 0 <= grade <= 4:
            raise ValueError(f"{role} task {task}: grade must be an integer from 0 to 4")
    return grades


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: python3 benchmark/score.py <scores.json>", file=sys.stderr)
        return 2

    try:
        scores = read_json(Path(sys.argv[1]))
        weights = read_json(Path(__file__).with_name("WEIGHTS.json"))
        if scores.get("benchmark_tag") != weights["benchmark_tag"]:
            raise ValueError("score input and weights use different benchmark tags")
        if sum(weights["human"].values()) != 70 or sum(weights["ai"].values()) != 30:
            raise ValueError("weights must total 70 human points and 30 AI points")
        human = grades_for(scores, "human", weights["human"])
        ai = grades_for(scores, "ai", weights["ai"])

        per_task = {}
        for task in sorted(weights["human"]):
            human_points = weights["human"][task] * human.get(task, 0) / 4
            ai_points = weights["ai"][task] * ai.get(task, 0) / 4
            per_task[task] = {
                "human": human_points,
                "ai": ai_points,
                "total": human_points + ai_points,
            }

        human_total = sum(item["human"] for item in per_task.values())
        ai_total = sum(item["ai"] for item in per_task.values())
        result = {
            "run_id": scores["run_id"],
            "benchmark_tag": scores["benchmark_tag"],
            "human_out_of_70": human_total,
            "ai_out_of_30": ai_total,
            "total_out_of_100": human_total + ai_total,
            "per_task": per_task,
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
        return 0
    except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
        print(f"score error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
