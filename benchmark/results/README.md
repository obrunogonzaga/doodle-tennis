# Resultados do benchmark

Cada linha representa uma execução independente a partir da mesma tag de baseline. Os resultados só são publicados depois que todas as execuções da rodada terminarem e forem pontuadas.

| ID | Baseline | Código entregue | Relatório | Modelo | Nota /100 | Tempo | Custo |
| --- | --- | --- | --- | --- | ---: | ---: | ---: |
| _Nenhuma execução avaliada ainda_ | | | | | | | |

## Estrutura de uma execução

```text
benchmark/results/run-001/
├── metadata.json
├── report.md
├── build.log                # se ajudar a explicar o resultado
└── screenshots/            # capturas feitas pelo avaliador
    ├── inicio.png
    ├── troca.png
    └── resultado.png
```

O código completo fica na branch `runs/run-001`, iniciada na tag `benchmark-v1`. O relatório aponta para o commit final dessa branch. O modelo e a nota só são divulgados depois da avaliação cega, quando possível.
