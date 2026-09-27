# Benchmark de implementação — Doodle Tênis

## Objetivo

Comparar como diferentes modelos implementam **o mesmo jogo**, a partir do mesmo PRD, das mesmas três referências visuais e das mesmas tarefas. Este documento define a entrada, as condições de execução e a forma de avaliar. O benchmark mede a entrega do protótipo inteiro, não a resolução isolada de uma issue.

## Fonte de verdade

- [PRD](./PRD.md) e [conjunto de referências visuais](./references/README.md), composto pela imagem conceitual, quadra vazia e prancha de personagens/interface.
- Tarefas versionadas em [`benchmark/tasks`](./benchmark/tasks/). As tarefas 01–08 são o escopo de implementação; a 09 descreve a validação feita pelo avaliador.
- [Prompt comum](./benchmark/PROMPT.md), [rubrica híbrida](./benchmark/EVALUATION.md), [prompt da IA avaliadora](./benchmark/AI_EVALUATOR_PROMPT.md) e [modelo de relatório](./benchmark/RUN_REPORT_TEMPLATE.md).
- [Fluxo de registro e publicação](./benchmark/RESULT_WORKFLOW.md) para iniciar o avaliador, guardar evidências e calcular notas.
- **Baseline atual:** tag Git `benchmark-v4`. Usar o commit apontado pela tag, nunca a ponta mutável de `main` nem o texto atual das issues como entrada canônica. `benchmark-v1`, `benchmark-v2` e `benchmark-v3` permanecem como registros históricos.

As issues do GitHub continuam úteis para discussão e acompanhamento, mas podem mudar depois de uma rodada. Em caso de divergência, prevalecem os arquivos da tag usada na rodada.

## Organização e persistência dos resultados

O repositório tem dois tipos de saída, guardados separadamente:

1. **Código do jogo:** cada candidato trabalha numa cópia isolada da tag `benchmark-v4`. Depois que todas as execuções da rodada terminarem, publicar a versão final em uma branch `runs/run-001`, `runs/run-002` etc. Cada branch contém o código completo daquele candidato e seu commit final; nenhuma implementação entra em `main` durante a comparação.
2. **Avaliação:** guardar em `benchmark/results/run-001/`, `benchmark/results/run-002/` etc. na branch `main`. Cada pasta contém `metadata.json`, `scores.json`, `report.md` e, quando produzidas, capturas em `screenshots/`. O [índice de resultados](./benchmark/results/README.md) liga a pasta ao commit de código. Usar os modelos de [metadados](./benchmark/RUN_METADATA_TEMPLATE.json), [notas](./benchmark/SCORE_TEMPLATE.json) e [relatório](./benchmark/RUN_REPORT_TEMPLATE.md).

Antes de iniciar uma execução, atribuir um ID anônimo (`run-001`, por exemplo) e registrá-lo com modelo, versão e reasoning em `benchmark/run-map.private.csv`. Criar esse arquivo local a partir do [modelo de mapeamento](./benchmark/RUN_MAP_TEMPLATE.csv); ele é ignorado pelo Git e não deve ser enviado ao candidato nem ao avaliador que fará a pontuação cega. Registrar no mesmo arquivo o commit final quando a execução terminar.

Como este repositório é público, não publicar branches ou relatórios antes de todas as execuções terminarem e das notas serem registradas: os próximos candidatos poderiam ver as soluções anteriores. Manter as cópias em pastas locais isoladas ou em repositórios privados até a divulgação. Após fechar as notas, preencher `model`, `model_version` e `reasoning_effort` no `metadata.json` de cada run, atualizar o índice e publicar as branches e relatórios. O arquivo privado de mapeamento continua fora do Git.

O build `dist/` é reproduzível a partir da branch e não precisa ser versionado. Guardar no resultado as capturas pequenas e os logs de verificação que sustentam a nota; não incluir chaves de API ou outros segredos em logs públicos. Se uma rodada exigir vídeos ou arquivos grandes, registrar no relatório um link estável para esses artefatos.

## Preparação de cada execução

1. Criar uma cópia de trabalho independente a partir de `benchmark-v4`, sem alterações de outro candidato. Pode ser um clone ou uma branch isolada iniciada no commit da tag.
2. Fornecer ao modelo o mesmo prompt de [`benchmark/PROMPT.md`](./benchmark/PROMPT.md), o PRD, as três imagens e as tarefas 01–08. A tarefa 09 não deve ser atribuída ao candidato.
3. Manter iguais, dentro da mesma rodada: ferramentas disponíveis, acesso à rede, tempo máximo, orçamento de tokens/custo, máquina, versão de Node e navegador. Se alguma dessas condições diferir, registrar a diferença e não tratar os resultados como comparação controlada.
4. Impedir que uma execução leia código, conversa, screenshots ou avaliações de outra antes de terminar.
5. Registrar modelo e versão exata, nível de reasoning, configuração do agente, limites, início e fim, uso de tokens/custo quando disponível, commit final e eventuais falhas de ferramenta.

Não conceder recursos de criação de arte ou bibliotecas especiais a apenas um candidato. Se quiser comparar modelos com capacidades diferentes, fazer uma rodada separada e declarar essa diferença.

## Contrato de entrega do candidato

- Entregar o jogo executável no navegador, cobrindo as tarefas 01–08.
- Documentar no README como instalar, iniciar, gerar o build e jogar.
- Disponibilizar `npm run dev` e `npm run build` funcionais. Uma suíte de testes automatizados pode ser adicionada, mas não substitui a verificação de jogo real.
- Preservar PRD, três referências visuais, prompt, rubrica e especificações das tarefas. Correções necessárias à implementação devem ocorrer no código e em seus próprios recursos.
- Informar limitações conhecidas e o commit final. O avaliador produz as capturas e as observações do teste para evitar evidências escolhidas pelo candidato.

## Avaliação

Usar a [rubrica](./benchmark/EVALUATION.md) antes de ver os resultados. O humano pontua a experiência de jogo (70 pontos) e uma IA avaliadora separada pontua verificações técnicas (30 pontos). Usar a mesma IA, configuração, prompt e ferramentas para todas as runs. Ambos recebem só o ID anônimo e registram as notas independentemente antes de ver a nota do outro. A tarefa 09 organiza os playtests e a publicação; ela não soma pontos por si só.

Para a rodada v4, a [configuração da IA avaliadora](./benchmark/EVALUATOR_CONFIG.json) está fixada em **`gpt-6-sol` com reasoning `high`** (“Sol 6 Alto”). Registrar a versão interna mais específica somente se a plataforma a informar; caso contrário, manter `model_version` como `null` e registrar data e configuração usada. A IA avaliadora é iniciada em uma conversa ou processo separado de cada candidato, recebendo o [prompt fixo da tag v4](./benchmark/AI_EVALUATOR_PROMPT.md) e um checkout anônimo. O repositório não aciona esse modelo automaticamente.

Uma rodada só deve comparar resultados gerados do mesmo baseline e sob condições equivalentes. Se o PRD, as referências, as tarefas, o prompt do candidato ou a rubrica mudarem, criar outra tag e registrar uma nova versão do benchmark. Resultados de tags diferentes não devem ser misturados, mesmo quando os pesos são iguais.

## Relação com os recursos do GitHub

O [template de issue](./.github/ISSUE_TEMPLATE/benchmark-task.md) ajuda a redigir tarefas futuras com estrutura consistente. Ele não substitui o congelamento dos textos em Git. Um repositório criado a partir de um template do GitHub copia arquivos, mas as issues originais não são o registro versionado da rodada; cada candidato deve receber as tarefas da tag.
