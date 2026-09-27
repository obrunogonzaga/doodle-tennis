# Resultados do benchmark

Cada linha representa uma execução independente a partir da mesma tag de baseline. Os resultados só são publicados depois que todas as execuções da rodada terminarem e forem pontuadas.

| ID | Baseline | Código entregue | Relatório | Modelo | Reasoning | Humano /70 | IA /30 | Total /100 | Tempo | Custo |
| --- | --- | --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| _Nenhuma execução avaliada ainda_ | | | | | | | | | | |

## Estrutura de uma execução

```text
benchmark/results/run-001/
├── metadata.json
├── scores.json              # notas humanas e da IA, antes da ponderação
├── score-summary.json       # cálculo gerado por benchmark/score.py
├── report.md
├── build.log                # se ajudar a explicar o resultado
└── screenshots/            # capturas feitas pelo avaliador
    ├── inicio.png
    ├── troca.png
    └── resultado.png
```

O código completo fica na branch `runs/run-001`, iniciada na tag `benchmark-v2`. O relatório aponta para o commit final dessa branch. O modelo e a nota só são divulgados depois da avaliação cega, quando possível. A nota é calculada com `python3 benchmark/score.py benchmark/results/run-001/scores.json` após humano e IA registrarem suas avaliações independentes.
