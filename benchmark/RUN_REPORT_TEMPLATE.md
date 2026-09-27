# Relatório de execução — <identificador anônimo>

## Condições

| Campo | Valor |
| --- | --- |
| Baseline Git (`benchmark-v4`) | |
| Modelo e versão exata | |
| Configuração de reasoning | |
| IA avaliadora, versão e reasoning | |
| Agente / configuração | |
| Ferramentas e acesso à rede | |
| Tempo e orçamento permitidos | |
| Versão de Node e navegador | |
| Início e fim | |
| Tokens / custo, se disponíveis | |
| Commit final | |
| Branch da implementação | |
| Pasta de resultado | |
| Status da avaliação: provisória ou final | |
| Sessões humanas observadas | |

## Verificação técnica

| Checagem | Resultado e evidência |
| --- | --- |
| Instalação em ambiente limpo | |
| `npm run dev` e abertura no navegador | |
| `npm run build` | |
| Erros de console ou falhas bloqueantes | |

## Pontuação independente

| Tarefa | Humano 0–4 | Pontos humanos | IA 0–4 | Pontos IA | Evidência ou falha |
| --- | ---: | ---: | ---: | ---: | --- |
| 01 · Projeto | — | — | | /10 | |
| 02 · Quadra e movimento | | /8 | | /2 | |
| 03 · Bola e ponto | | /11 | | /4 | |
| 04 · Rebatida | | /13 | | /2 | |
| 05 · Adversário | | /8 | | /2 | |
| 06 · Partida e telas | | /11 | | /4 | |
| 07 · Arte em camadas | | /7 | | /3 | |
| 08 · Integração visual | | /12 | | /3 | |
| **Total** | | **/70** | | **/30** | **/100** |

Preencher `scores.json` com as duas avaliações independentes e gerar `score-summary.json` com `python3 benchmark/finalize_result.py <run-id>`. Registrar se a nota é provisória por falta das três sessões humanas.

## Teste de jogo

- Controles compreendidos em até 30 segundos:
- Partida concluída:
- Jogadores explicaram os resultados dos pontos:
- Capturas da tela inicial, troca de bolas e resultado:
- Problemas observados:

## Decisão

Resumo do que funcionou, limitações, ajustes sugeridos, diferenças entre notas humana e da IA e eventual diferença nas condições desta execução. Registrar ambas as pontuações antes de qualquer correção no código do candidato e antes de revelar o modelo.
