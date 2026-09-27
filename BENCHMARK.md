# Benchmark de implementação — Rabisco Tênis

## Objetivo

Comparar como diferentes modelos implementam **o mesmo jogo**, a partir do mesmo PRD, da mesma imagem conceitual e das mesmas tarefas. Este documento define a entrada, as condições de execução e a forma de avaliar. O benchmark mede a entrega do protótipo inteiro, não a resolução isolada de uma issue.

## Fonte de verdade

- [PRD](./PRD.md) e [imagem conceitual](./rabisco-tennis-conceito.png).
- Tarefas versionadas em [`benchmark/tasks`](./benchmark/tasks/). As tarefas 01–08 são o escopo de implementação; a 09 descreve a validação feita pelo avaliador.
- [Prompt comum](./benchmark/PROMPT.md), [rubrica de avaliação](./benchmark/EVALUATION.md) e [modelo de relatório](./benchmark/RUN_REPORT_TEMPLATE.md).
- **Baseline v1:** tag Git `benchmark-v1`. Usar o commit apontado pela tag, nunca a ponta mutável de `main` nem o texto atual das issues como entrada canônica.

As issues do GitHub continuam úteis para discussão e acompanhamento, mas podem mudar depois de uma rodada. Em caso de divergência, prevalecem os arquivos da tag usada na rodada.

## Preparação de cada execução

1. Criar uma cópia de trabalho independente a partir de `benchmark-v1`, sem alterações de outro candidato. Pode ser um clone ou uma branch isolada iniciada no commit da tag.
2. Fornecer ao modelo o mesmo prompt de [`benchmark/PROMPT.md`](./benchmark/PROMPT.md), o PRD, a imagem e as tarefas 01–08. A tarefa 09 não deve ser atribuída ao candidato.
3. Manter iguais, dentro da mesma rodada: ferramentas disponíveis, acesso à rede, tempo máximo, orçamento de tokens/custo, máquina, versão de Node e navegador. Se alguma dessas condições diferir, registrar a diferença e não tratar os resultados como comparação controlada.
4. Impedir que uma execução leia código, conversa, screenshots ou avaliações de outra antes de terminar.
5. Registrar modelo e versão exata, configuração do agente, limites, início e fim, uso de tokens/custo quando disponível, commit final e eventuais falhas de ferramenta.

Não conceder recursos de criação de arte ou bibliotecas especiais a apenas um candidato. Se quiser comparar modelos com capacidades diferentes, fazer uma rodada separada e declarar essa diferença.

## Contrato de entrega do candidato

- Entregar o jogo executável no navegador, cobrindo as tarefas 01–08.
- Documentar no README como instalar, iniciar, gerar o build e jogar.
- Disponibilizar `npm run dev` e `npm run build` funcionais. Uma suíte de testes automatizados pode ser adicionada, mas não substitui a verificação de jogo real.
- Preservar PRD, imagem, prompt, rubrica e especificações das tarefas. Correções necessárias à implementação devem ocorrer no código e em seus próprios recursos.
- Informar limitações conhecidas e o commit final. O avaliador produz as capturas e as observações do teste para evitar evidências escolhidas pelo candidato.

## Avaliação

Usar a [rubrica](./benchmark/EVALUATION.md) antes de ver os resultados. A mesma pessoa ou equipe avalia todos os candidatos, preferencialmente sem saber qual modelo produziu cada versão. Executar a checagem técnica e a mesma sequência de jogo em viewport 1536 × 1024. A tarefa 09 registra os playtests e ajustes como atividade do avaliador; ela não soma pontos por si só.

Uma rodada só deve comparar resultados gerados do mesmo baseline e sob condições equivalentes. Se o PRD, as tarefas ou a rubrica mudarem, criar outra tag e registrar uma nova versão do benchmark.

## Relação com os recursos do GitHub

O [template de issue](./.github/ISSUE_TEMPLATE/benchmark-task.md) ajuda a redigir tarefas futuras com estrutura consistente. Ele não substitui o congelamento dos textos em Git. Um repositório criado a partir de um template do GitHub copia arquivos, mas as issues originais não são o registro versionado da rodada; cada candidato deve receber as tarefas da tag.
