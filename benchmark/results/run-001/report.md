# Relatório de execução — run-001

## Condições

| Campo | Valor |
| --- | --- |
| Baseline Git (`benchmark-v4`) | `f25b8a2982064803fa87fd91f0da4533261db9e3` |
| Modelo e versão exata | A revelar após a rodada; versão não registrada |
| Configuração de reasoning | A revelar após a rodada |
| IA avaliadora, versão e reasoning | `gpt-6-sol`, versão interna não informada, `high` |
| Agente / configuração | Não informado |
| Ferramentas e acesso à rede | Node, npm, Vite e Chromium headless usados na avaliação técnica; condições da implementação não informadas |
| Tempo e orçamento permitidos | Não informados |
| Versão de Node e navegador | Não registradas |
| Início e fim | Não registrados |
| Tokens / custo, se disponíveis | Não informados |
| Commit final | `ac885f717d5c3e8673dffcc96741509cd7fe77be` |
| Branch da implementação | `runs/run-001` (ainda local) |
| Pasta de resultado | `benchmark/results/run-001/` |
| Status da avaliação: provisória ou final | **Provisória** |
| Sessões humanas observadas | 0 registradas |

## Verificação técnica

| Checagem | Resultado e evidência |
| --- | --- |
| Instalação em ambiente limpo | `npm ci` concluiu. |
| `npm run dev` e abertura no navegador | Vite iniciou; avaliador abriu o jogo no Chromium headless. |
| `npm run build` | Concluiu, com aviso de bundle acima de 500 kB. |
| Erros de console ou falhas bloqueantes | Nenhum erro de página ou HTTP observado. |

## Pontuação independente

| Tarefa | Humano 0–4 | Pontos humanos | IA 0–4 | Pontos IA | Evidência ou falha |
| --- | ---: | ---: | ---: | ---: | --- |
| 01 · Projeto | — | — | 4 | 10 | Instalação, build e execução concluídos. |
| 02 · Quadra e movimento | 2 | 4 | 4 | 2 | Movimento técnico validado; divergência humana pendente. |
| 03 · Bola e ponto | 2 | 5,5 | 4 | 4 | Trajetórias técnicas validadas; divergência humana pendente. |
| 04 · Rebatida | 3 | 9,75 | 4 | 2 | Contato e janela de rebatida validados. |
| 05 · Adversário | 2 | 4 | 4 | 2 | Devolução e erro controlado validados; divergência humana pendente. |
| 06 · Partida e telas | 2 | 5,5 | 4 | 4 | Placar, pausa e reinício validados; divergência humana pendente. |
| 07 · Arte em camadas | 3 | 5,25 | 4 | 3 | Elementos visuais separados e legíveis. |
| 08 · Integração visual | 4 | 12 | 4 | 3 | Telas e quadra legíveis em duas resoluções. |
| **Total** | | **46/70** | | **30/30** | **76/100, provisório** |

Detalhes por tarefa: [avaliação humana](./human-assessment.md), [avaliação da IA](./ai-assessment.md) e [cálculo da pontuação](./score-summary.json).

## Teste de jogo

- Controles compreendidos em até 30 segundos: não registrado em sessão observada.
- Partida concluída: a IA chegou à tela “JOGO” no navegador; sessão humana não registrada.
- Jogadores explicaram os resultados dos pontos: não registrado.
- Capturas da tela inicial, troca de bolas e resultado: [início](./screenshots/inicio.png), [troca](./screenshots/troca.png) e [resultado](./screenshots/resultado.png).
- Problemas observados: diferenças entre avaliação humana e técnica nas tarefas 02, 03, 05 e 06; ver revisão abaixo.

## Decisão

Build, testes e fluxo básico do jogo passaram na avaliação técnica. O total de 76/100 preserva as notas humanas originais e permanece provisório: faltam sessões humanas observadas e revisão das divergências abaixo. Falhas de rede e fora foram reproduzidas na simulação, mas não durante a sessão da IA no navegador. Tempo, custo e condições completas da implementação não foram registrados.

## Revisão de divergências pendente

As notas originais foram preservadas. A IA atribuiu 4 às tarefas técnicas 01–08; as notas humanas diferem em dois pontos nas tarefas 02, 03, 05 e 06. Antes de fechar o resultado, revisar as observações abaixo e repetir o teste de jogo pertinente:

- **02 (humano 2, IA 4):** a nota humana menciona pouca expressão dos personagens e ausência de controle da direção da bola. A tarefa 02 mede movimento lateral e limites; expressão visual pertence à tarefa 07. O PRD prevê assistência automática de direção, sem mira manual nesta versão.
- **03 (humano 2, IA 4):** a nota humana menciona ausência de controle da trajetória. A tarefa 03 mede clareza da trajetória, quique e motivo do ponto, e o PRD não exige controle manual da direção. Reavaliar se a bola e o fim dos pontos foram compreensíveis durante o jogo.
- **05 (humano 2, IA 4):** a nota humana menciona pouca variação de movimentos. Repetir várias trocas para distinguir a animação visual da qualidade do adversário, que deve devolver bolas, ter alcance limitado e ocasionalmente errar.
- **06 (humano 2, IA 4):** a nota humana menciona apenas um set. O PRD define uma partida curta até “jogo” e exclui sets completos. Reavaliar placar, pausa, resultado e reinício conforme a tarefa 06.

O resultado calculado é **provisório** também porque ainda não há sessões humanas observadas registradas. Nenhuma nota deve ser alterada sem preservar a pontuação original e justificar a revisão.
