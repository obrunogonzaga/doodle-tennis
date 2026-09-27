"""Validate independent assessments and persist weighted scores locally."""

import json
import hashlib
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark"


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def main() -> int:
    if len(sys.argv) != 2 or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,62}[a-z0-9]", sys.argv[1]):
        print("usage: python3 benchmark/finalize_result.py <run-id>", file=sys.stderr)
        return 2

    run_id = sys.argv[1]
    result_dir = BENCHMARK / "results" / run_id
    try:
        metadata = load_json(result_dir / "metadata.json")
        scores = load_json(result_dir / "scores.json")
        evaluator_bytes = (BENCHMARK / "EVALUATOR_CONFIG.json").read_bytes()
        evaluator = json.loads(evaluator_bytes)
        baseline = subprocess.run(
            ["git", "rev-parse", "benchmark-v3^{}"],
            cwd=ROOT, check=True, capture_output=True, text=True,
        ).stdout.strip()

        if metadata["run_id"] != run_id or scores["run_id"] != run_id:
            raise ValueError("run ID differs between folder, metadata and scores")
        if len({metadata["benchmark_tag"], scores["benchmark_tag"], evaluator["benchmark_tag"]}) != 1:
            raise ValueError("benchmark tags differ")
        if metadata["baseline_commit"] != baseline:
            raise ValueError("baseline commit differs from benchmark-v3")
        if metadata["candidate_branch"] != f"runs/{run_id}":
            raise ValueError("candidate branch does not match run ID")
        if not re.fullmatch(r"[0-9a-f]{40}", metadata.get("candidate_commit") or ""):
            raise ValueError("candidate_commit must be the full 40-character commit SHA")
        if metadata["ai_evaluator_model"] != evaluator["model"]:
            raise ValueError("AI evaluator model differs from fixed round configuration")
        if metadata["ai_evaluator_reasoning_effort"] != evaluator["reasoning_effort"]:
            raise ValueError("AI evaluator reasoning differs from fixed round configuration")
        if evaluator["model_version"] is not None:
            if metadata["ai_evaluator_version"] != evaluator["model_version"]:
                raise ValueError("AI evaluator version differs from fixed round configuration")
        if metadata["ai_evaluator_config_sha256"] != hashlib.sha256(evaluator_bytes).hexdigest():
            raise ValueError("AI evaluator configuration changed during the round")
        sessions = metadata.get("human_playtest_sessions")
        if type(sessions) is not int or sessions < 0:
            raise ValueError("human_playtest_sessions must be a nonnegative integer")

        frozen_weights = subprocess.run(
            ["git", "show", "benchmark-v3:benchmark/WEIGHTS.json"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout
        if (BENCHMARK / "WEIGHTS.json").read_bytes() != frozen_weights:
            raise ValueError("local weights differ from the frozen benchmark-v3 tag")

        for template_name, output_name in (
            ("AI_ASSESSMENT_TEMPLATE.md", "ai-assessment.md"),
            ("HUMAN_ASSESSMENT_TEMPLATE.md", "human-assessment.md"),
        ):
            template = (BENCHMARK / template_name).read_text(encoding="utf-8")
            template = template.replace("<run-id>", run_id)
            assessment = (result_dir / output_name).read_text(encoding="utf-8")
            if assessment == template:
                raise ValueError(f"{output_name} is still the empty template")

        result = subprocess.run(
            [sys.executable, str(BENCHMARK / "score.py"), str(result_dir / "scores.json")],
            cwd=ROOT, capture_output=True, text=True,
        )
        if result.returncode != 0:
            raise ValueError(result.stderr.strip())
        summary = json.loads(result.stdout)

        (result_dir / "score-summary.json").write_text(
            json.dumps(summary, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        metadata.update(
            human_score_out_of_70=summary["human_out_of_70"],
            ai_score_out_of_30=summary["ai_out_of_30"],
            score_out_of_100=summary["total_out_of_100"],
            evaluation_status="final" if sessions >= 3 else "provisional",
            status="evaluated",
        )
        (result_dir / "metadata.json").write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"{run_id}: {summary['total_out_of_100']}/100 recorded locally")
        return 0
    except (OSError, KeyError, TypeError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f"finalize error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
