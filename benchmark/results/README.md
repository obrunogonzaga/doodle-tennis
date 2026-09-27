# Resultados do benchmark

Cada linha representa uma execução independente a partir da mesma tag de baseline. Os resultados só são publicados depois que todas as execuções da rodada terminarem e forem pontuadas.

| ID | Baseline | Código entregue | Relatório | Modelo | Reasoning | Humano /70 | IA /30 | Total /100 | Status | Tempo | Custo |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: | ---: |
| `run-001` | `benchmark-v4` | `ac885f7` (`runs/run-001`) | [Relatório](./run-001/report.md) | A revelar | A revelar | 46 | 30 | **76** | Provisório | Não informado | Não informado |

A `run-001` tem menos de três sessões humanas observadas e divergências entre as avaliações ainda pendentes. O código candidato permanece na branch local; o commit está identificado nos [metadados](./run-001/metadata.json). A identidade do modelo candidato será revelada após a rodada.

## Estrutura de uma execução

```text
benchmark/results/run-001/
├── metadata.json
├── scores.json              # notas humanas e da IA, antes da ponderação
├── score-summary.json       # cálculo gerado por benchmark/finalize_result.py
├── ai-assessment.md         # notas e evidências da IA técnica
├── human-assessment.md      # notas e sessões humanas
├── report.md
├── build.txt                # trecho de log limpo, se relevante
└── screenshots/            # capturas feitas pelo avaliador
    ├── inicio.png
    ├── troca.png
    └── resultado.png
```

O código completo fica na branch `runs/run-001`, iniciada na tag `benchmark-v4`. O relatório aponta para o commit final dessa branch. O modelo e a nota só são divulgados depois da avaliação cega, quando possível. O [fluxo de avaliação](../RESULT_WORKFLOW.md) explica como preparar a pasta, registrar as duas notas e calcular o resultado.
