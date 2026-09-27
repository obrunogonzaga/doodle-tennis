# Doodle Tênis

Protótipo de tênis de arcade no navegador, inspirado em desenhos feitos num caderno.

## Projeto

- [PRD](./PRD.md): visão, escopo, regras, critérios de aceite e etapas de entrega.
- [Referências visuais](./references/README.md): conceito principal, quadra vazia e prancha de personagens/interface.
- [Protocolo de benchmark](./BENCHMARK.md): entrada comum, execução isolada e avaliação dos modelos.
- [Resultados do benchmark](./benchmark/results/README.md): índice das execuções avaliadas.
- [Como registrar uma avaliação](./benchmark/RESULT_WORKFLOW.md): IA fixa, notas humanas, evidências e publicação.

O código do jogo será desenvolvido em Phaser, TypeScript e Vite. A primeira versão terá uma partida curta contra o computador, com movimento lateral, rebatida por tempo de acerto e pontuação simplificada.

## Estado

Planejamento concluído. A implementação será acompanhada pelas issues do repositório. As especificações congeladas para comparação entre modelos ficam em [`benchmark/tasks`](./benchmark/tasks/).

## Como convidar um modelo para o benchmark

Escolha um ID para a execução e prepare uma cópia isolada. Por exemplo, para `run-001`, execute **fora da pasta deste repositório**, em um diretório que ainda não contenha `doodle-run-001`:

```bash
git clone https://github.com/obrunogonzaga/doodle-tennis.git doodle-run-001
cd doodle-run-001
git switch -c runs/run-001 benchmark-v4
```

Abra o modelo de programação **nessa cópia** e envie a mensagem abaixo. Para as próximas execuções da mesma rodada, troque `run-001` pelo novo ID nos comandos e na mensagem; mantenha a tag, o limite de 60 minutos e as demais condições iguais às da primeira execução. Copie a mensagem deste README na branch `main`: a tag `benchmark-v4` é imutável e seu README ainda mostra o exemplo anterior de limites.

> Você é o candidato `run-001` do benchmark Doodle Tênis. Leia e execute integralmente `benchmark/PROMPT.md`, usando a tag `benchmark-v4` como entrada. Você tem uma tentativa e 60 minutos de execução. Se houver cobrança por uso, a rodada também termina ao atingir US$ 10, o que ocorrer primeiro; esse gasto será monitorado externamente. Faça commits locais ao concluir etapas funcionais para preservar o progresso. Trabalhe somente neste checkout, não consulte outras runs, não use serviços pagos externos e não faça push. Se eu disser **PARAR**, interrompa o trabalho, faça um commit local do estado atual e informe o SHA. Ao terminar, informe também as verificações executadas e as limitações conhecidas.

O texto da mensagem não impõe um bloqueio de cobrança. Se usar uma API, configure o teto de gasto na plataforma antes de iniciar; um alerta de custo não encerra a execução. Se usar uma assinatura sem teto por run em dólares, acompanhe a cota ou os créditos da plataforma e controle o tempo externamente. Quem organiza a rodada registra o motivo da interrupção e avalia o estado entregue, sem aumentar o limite apenas para um candidato. Para o próximo candidato, crie outra cópia **da mesma tag** e mantenha as implementações separadas até todas terminarem. Depois, avalie pela [rubrica](./benchmark/EVALUATION.md) e publique o código e o relatório conforme o [protocolo](./BENCHMARK.md).

Antes de cada execução, registre em privado qual modelo e nível de reasoning corresponde ao ID. No checkout do organizador, copie [`benchmark/RUN_MAP_TEMPLATE.csv`](./benchmark/RUN_MAP_TEMPLATE.csv) para `benchmark/run-map.private.csv` e preencha uma linha por run; esse arquivo é ignorado pelo Git. Após pontuar todos os candidatos, coloque essa identificação no `metadata.json` e no [índice de resultados](./benchmark/results/README.md). Assim a avaliação pode usar apenas o ID da run até as notas estarem fechadas.

Na **v4**, a [rubrica](./benchmark/EVALUATION.md) combina **70 pontos de avaliação humana** com **30 pontos de uma IA avaliadora independente**. A IA usa sempre o mesmo [prompt](./benchmark/AI_EVALUATOR_PROMPT.md) e configuração para todas as runs. As duas notas são registradas separadamente antes de calcular o total.
