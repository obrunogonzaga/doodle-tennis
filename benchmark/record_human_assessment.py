"""Collect a human playtest assessment in the organizer's main checkout."""

import json
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BENCHMARK = ROOT / "benchmark"
TASKS = (
    ("02", "Quadra e movimento", "Controles e limites perceptíveis"),
    ("03", "Bola e ponto", "Trajetória, quique e motivo do ponto claros"),
    ("04", "Rebatida", "Tempo de contato justo e feedback de acerto/erro"),
    ("05", "Adversário", "Trocas jogáveis e dificuldade inicial"),
    ("06", "Partida e telas", "Placar, pausa, resultado e reinício compreensíveis"),
    ("07", "Arte em camadas", "Fidelidade às três referências visuais"),
    ("08", "Integração visual", "Legibilidade e apresentação no desktop"),
)


def load_json(path: Path) -> dict:
    with path.open(encoding="utf-8") as stream:
        return json.load(stream)


def ask_number(question: str, minimum: int, maximum: int | None = None) -> int:
    while True:
        answer = input(question).strip()
        if answer.isdecimal():
            value = int(answer)
            if value >= minimum and (maximum is None or value <= maximum):
                return value
        if maximum is None:
            print(f"Digite um número inteiro maior ou igual a {minimum}.")
        else:
            print(f"Digite um número inteiro entre {minimum} e {maximum}.")


def ask_text(question: str, required: bool = True) -> str:
    while True:
        answer = input(question).strip()
        if answer or not required:
            return answer
        print("Registre uma observação concreta, inclusive quando a nota for zero.")


def ask_observation(question: str) -> str:
    while True:
        answer = input(question).strip().lower()
        if answer in ("s", "sim"):
            return "sim"
        if answer in ("n", "não", "nao"):
            return "não"
        if answer in ("-", "não observado", "nao observado"):
            return "não observado"
        print("Responda s, n ou - (não observado).")


def ask_confirmation(question: str) -> bool:
    while True:
        answer = input(question).strip().lower()
        if answer in ("s", "sim"):
            return True
        if answer in ("", "n", "não", "nao"):
            return False
        print("Responda s ou n.")


def markdown_cell(value: str) -> str:
    return value.replace("|", "\\|")


def prepare_folder(run_id: str, adding_sessions: bool = False) -> Path:
    branch = subprocess.run(
        ["git", "branch", "--show-current"],
        cwd=ROOT, check=True, capture_output=True, text=True,
    ).stdout.strip()
    if branch != "main":
        raise ValueError(
            f"A avaliação deve ficar no checkout do organizador ({ROOT}), na branch main; "
            f"branch atual: {branch or '(sem branch)'}"
        )

    folder = BENCHMARK / "results" / run_id
    if not folder.exists():
        if adding_sessions:
            raise ValueError("Esta run ainda não tem avaliação humana para receber sessões adicionais.")
        result = subprocess.run(
            [sys.executable, str(BENCHMARK / "prepare_result.py"), run_id],
            cwd=ROOT, capture_output=True, text=True,
        )
        if result.returncode:
            raise ValueError(result.stderr.strip() or result.stdout.strip())
        print(f"Pasta da run preparada: {folder}")

    metadata = load_json(folder / "metadata.json")
    scores = load_json(folder / "scores.json")
    weights = load_json(BENCHMARK / "WEIGHTS.json")
    expected_tasks = {task for task, weight in weights["human"].items() if weight > 0}
    if metadata.get("run_id") != run_id or scores.get("run_id") != run_id:
        raise ValueError("O ID da pasta não corresponde aos arquivos da avaliação.")
    if len({metadata.get("benchmark_tag"), scores.get("benchmark_tag"), weights["benchmark_tag"]}) != 1:
        raise ValueError("A tag da run não corresponde à rubrica atual.")
    if set(scores.get("human", {})) != expected_tasks or expected_tasks != {task for task, _, _ in TASKS}:
        raise ValueError("As tarefas humanas não correspondem à rubrica.")
    template = (BENCHMARK / "HUMAN_ASSESSMENT_TEMPLATE.md").read_text(encoding="utf-8")
    assessment = (folder / "human-assessment.md").read_text(encoding="utf-8")
    empty_assessment = template.replace("<run-id>", run_id)
    if adding_sessions:
        if not all(type(grade) is int and 0 <= grade <= 4 for grade in scores["human"].values()):
            raise ValueError("Esta run ainda não tem todas as notas humanas preenchidas.")
        if assessment == empty_assessment:
            raise ValueError("Esta run ainda não tem observações humanas preenchidas.")
    else:
        if any(grade is not None for grade in scores["human"].values()):
            raise ValueError("Esta run já tem notas humanas; use --add-sessions para registrar novos playtests.")
        if assessment != empty_assessment:
            raise ValueError("Esta run já tem observações humanas; não vou sobrescrevê-las.")
    return folder


def assessment_markdown(run_id: str, benchmark_tag: str, grades: dict, evidence: dict, sessions: list[dict]) -> str:
    lines = [
        f"# Avaliação humana — {run_id}",
        "",
        f"**Rubrica:** `{benchmark_tag}`<br>",
        "**Identidade do candidato:** oculta até fechar as notas",
        "",
        "Pontuação da experiência de jogo, registrada sem consultar a nota da IA.",
        "",
        "| Tarefa | Nota 0–4 | Evidência e falha observada |",
        "| --- | ---: | --- |",
    ]
    for task, label, _ in TASKS:
        lines.append(f"| {task} · {label} | {grades[task]} | {markdown_cell(evidence[task])} |")
    lines.extend([
        "",
        "## Sessões observadas",
        "",
        "| Sessão | Controles em até 30 s? | Partida concluída? | Explicou os pontos? | Observações |",
        "| --- | --- | --- | --- | --- |",
    ])
    for number, session in enumerate(sessions, start=1):
        lines.append(
            f"| {number} | {session['controls']} | {session['match']} | "
            f"{session['points']} | {markdown_cell(session['notes'])} |"
        )
    if len(sessions) < 3:
        lines.extend(["", "**Resultado provisório:** menos de três sessões observadas."])
    return "\n".join(lines) + "\n"


def collect_sessions(start_number: int, count: int) -> list[dict]:
    sessions = []
    for number in range(start_number, start_number + count):
        print(f"\nSessão {number} — responda s, n ou - (não observado).")
        sessions.append({
            "controls": ask_observation("  Entendeu os controles em até 30 segundos? "),
            "match": ask_observation("  Concluiu a partida? "),
            "points": ask_observation("  Explicou por que os pontos terminaram? "),
            "notes": ask_text("  Observações (Enter se nenhuma): ", required=False),
        })
    return sessions


def append_sessions(folder: Path) -> int:
    metadata = load_json(folder / "metadata.json")
    previous_count = metadata["human_playtest_sessions"]
    if type(previous_count) is not int or previous_count < 0:
        raise ValueError("Número anterior de sessões inválido em metadata.json.")
    path = folder / "human-assessment.md"
    lines = path.read_text(encoding="utf-8").splitlines()
    separator = "| --- | --- | --- | --- | --- |"
    if separator not in lines:
        raise ValueError("Tabela de sessões não encontrada em human-assessment.md.")
    insert_at = lines.index(separator) + 1
    end = insert_at
    while end < len(lines) and lines[end].startswith("| "):
        end += 1
    if end - insert_at != previous_count:
        raise ValueError("A tabela de sessões e metadata.json têm contagens diferentes.")

    count = ask_number("Quantas novas sessões observadas deseja registrar? ", 1)
    sessions = collect_sessions(previous_count + 1, count)
    new_count = previous_count + count
    print(f"\nTotal de sessões observadas: {new_count}")
    if not ask_confirmation("Salvar sessões adicionais? [s/N]: "):
        print("Nenhuma sessão nova foi salva.")
        return 0

    rows = []
    for number, session in enumerate(sessions, start=previous_count + 1):
        rows.append(
            f"| {number} | {session['controls']} | {session['match']} | "
            f"{session['points']} | {markdown_cell(session['notes'])} |"
        )
    lines[end:end] = rows
    if new_count >= 3:
        lines = [line for line in lines if line != "**Resultado provisório:** menos de três sessões observadas."]
    metadata["human_playtest_sessions"] = new_count
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    (folder / "metadata.json").write_text(
        json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(f"Sessões registradas em {folder}; notas humanas preservadas.")
    return 0


def main() -> int:
    if (
        len(sys.argv) not in (2, 3)
        or not re.fullmatch(r"[a-z0-9][a-z0-9-]{1,62}[a-z0-9]", sys.argv[1])
        or (len(sys.argv) == 3 and sys.argv[2] != "--add-sessions")
    ):
        print("Uso: python3 benchmark/record_human_assessment.py <run-id> [--add-sessions]", file=sys.stderr)
        return 2
    run_id = sys.argv[1]
    try:
        adding_sessions = len(sys.argv) == 3
        folder = prepare_folder(run_id, adding_sessions=adding_sessions)
        if adding_sessions:
            return append_sessions(folder)
        rubric = load_json(BENCHMARK / "WEIGHTS.json")
        weights = rubric["human"]
        grades = {}
        evidence = {}
        print("\nAvaliação humana: 0=ausente, 1=tentativa, 2=parcial, 3=funcional com falha menor, 4=atende.")
        print("Não consulte as notas da IA durante este preenchimento.\n")
        for task, label, criterion in TASKS:
            print(f"{task} · {label} — {criterion} (peso {weights[task]})")
            grades[task] = ask_number("  Nota [0–4]: ", 0, 4)
            evidence[task] = ask_text("  Evidência ou falha observada: ")
            print()

        count = ask_number(
            "Sessões observadas com pessoas que não desenvolveram o jogo (0 se ainda não houve): ", 0
        )
        sessions = collect_sessions(1, count)

        total = sum(weights[task] * grade / 4 for task, grade in grades.items())
        print(f"\nSubtotal humano: {total:g}/70")
        print("Resultado provisório: faltam sessões observadas." if count < 3 else "Três ou mais sessões registradas.")
        if not ask_confirmation("Salvar avaliação? [s/N]: "):
            print("Notas não salvas. A pasta preparada, se nova, continua com os modelos vazios.")
            return 0

        scores = load_json(folder / "scores.json")
        metadata = load_json(folder / "metadata.json")
        scores["human"] = grades
        metadata["human_playtest_sessions"] = count
        (folder / "human-assessment.md").write_text(
            assessment_markdown(run_id, rubric["benchmark_tag"], grades, evidence, sessions), encoding="utf-8"
        )
        (folder / "scores.json").write_text(
            json.dumps(scores, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        (folder / "metadata.json").write_text(
            json.dumps(metadata, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )
        print(f"Avaliação humana salva em {folder}")
        return 0
    except (EOFError, KeyboardInterrupt):
        print("\nEntrevista interrompida; notas não salvas.", file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError, subprocess.CalledProcessError) as error:
        print(f"Erro ao registrar avaliação humana: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
