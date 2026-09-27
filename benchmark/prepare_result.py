"""Prepare local, unpublished evidence files for one benchmark run."""

import json
import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark"


def main() -> int:
    if len(sys.argv) != 2 or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,62}[a-z0-9]", sys.argv[1]):
        print("usage: python3 benchmark/prepare_result.py <run-id> (example: run-001)", file=sys.stderr)
        return 2

    run_id = sys.argv[1]
    branch = subprocess.run(
        ["git", "branch", "--show-current"], cwd=ROOT, check=True, capture_output=True, text=True
    ).stdout.strip()
    if branch != "main":
        print("prepare results in the organizer's main checkout", file=sys.stderr)
        return 1

    result_dir = BENCHMARK / "results" / run_id
    if result_dir.exists():
        print(f"result folder already exists: {result_dir}", file=sys.stderr)
        return 1

    baseline = subprocess.run(
        ["git", "rev-parse", "benchmark-v4^{}"],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    result_dir.mkdir(parents=True)
    (result_dir / "screenshots").mkdir()

    metadata = json.loads((BENCHMARK / "RUN_METADATA_TEMPLATE.json").read_text(encoding="utf-8"))
    evaluator_bytes = (BENCHMARK / "EVALUATOR_CONFIG.json").read_bytes()
    evaluator = json.loads(evaluator_bytes)
    if evaluator["benchmark_tag"] != metadata["benchmark_tag"]:
        raise ValueError("evaluator and result templates use different benchmark tags")
    evaluator_hash = hashlib.sha256(evaluator_bytes).hexdigest()
    for existing in (BENCHMARK / "results").glob("*/metadata.json"):
        previous = json.loads(existing.read_text(encoding="utf-8"))
        if previous.get("benchmark_tag") == metadata["benchmark_tag"]:
            if previous.get("ai_evaluator_config_sha256") != evaluator_hash:
                raise ValueError("AI evaluator configuration differs from an existing run")
    metadata.update(
        run_id=run_id,
        baseline_commit=baseline,
        candidate_branch=f"runs/{run_id}",
        ai_evaluator_model=evaluator["model"],
        ai_evaluator_version=evaluator["model_version"],
        ai_evaluator_reasoning_effort=evaluator["reasoning_effort"],
        ai_evaluator_config_sha256=evaluator_hash,
    )
    (result_dir / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    scores = json.loads((BENCHMARK / "SCORE_TEMPLATE.json").read_text(encoding="utf-8"))
    scores["run_id"] = run_id
    (result_dir / "scores.json").write_text(
        json.dumps(scores, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    for template, output in (
        ("RUN_REPORT_TEMPLATE.md", "report.md"),
        ("AI_ASSESSMENT_TEMPLATE.md", "ai-assessment.md"),
        ("HUMAN_ASSESSMENT_TEMPLATE.md", "human-assessment.md"),
    ):
        content = (BENCHMARK / template).read_text(encoding="utf-8")
        content = content.replace("<identificador anônimo>", run_id).replace("<run-id>", run_id)
        (result_dir / output).write_text(content, encoding="utf-8")

    print(result_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
