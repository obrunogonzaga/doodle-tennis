# Resultados do benchmark

Cada linha representa uma execução independente a partir da mesma tag de baseline. Os resultados só são publicados depois que todas as execuções da rodada terminarem e forem pontuadas.

| ID | Baseline | Código entregue | Relatório | Modelo | Reasoning | Humano /70 | IA /30 | Total /100 | Status | Tempo | Custo |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | --- | ---: | ---: |
| _Nenhuma execução avaliada ainda_ | | | | | | | | | | | |

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

O código completo fica na branch `runs/run-001`, iniciada na tag `benchmark-v3`. O relatório aponta para o commit final dessa branch. O modelo e a nota só são divulgados depois da avaliação cega, quando possível. O [fluxo de avaliação](../RESULT_WORKFLOW.md) explica como preparar a pasta, registrar as duas notas e calcular o resultado.
