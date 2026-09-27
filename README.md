# Rabisco Tênis

Protótipo de tênis de arcade no navegador, inspirado em desenhos feitos num caderno.

## Projeto

- [PRD](./PRD.md): visão, escopo, regras, critérios de aceite e etapas de entrega.
- [Referências visuais](./references/README.md): conceito original, quadra vazia e prancha de personagens/interface.
- [Protocolo de benchmark](./BENCHMARK.md): entrada comum, execução isolada e avaliação dos modelos.
- [Resultados do benchmark](./benchmark/results/README.md): índice das execuções avaliadas.
- [Como registrar uma avaliação](./benchmark/RESULT_WORKFLOW.md): IA fixa, notas humanas, evidências e publicação.

O código do jogo será desenvolvido em Phaser, TypeScript e Vite. A primeira versão terá uma partida curta contra o computador, com movimento lateral, rebatida por tempo de acerto e pontuação simplificada.

## Estado

Planejamento concluído. A implementação será acompanhada pelas issues do repositório. As especificações congeladas para comparação entre modelos ficam em [`benchmark/tasks`](./benchmark/tasks/).

## Como convidar um modelo para o benchmark

Escolha um ID para a execução e prepare uma cópia isolada. Por exemplo, para `run-001`, execute **fora da pasta deste repositório**, em um diretório que ainda não contenha `rabisco-run-001`:

```bash
git clone https://github.com/obrunogonzaga/rabisco-tennis.git rabisco-run-001
cd rabisco-run-001
git switch -c runs/run-001 benchmark-v3
```

Abra o modelo de programação **nessa cópia** e envie a mensagem abaixo. Os limites de 2 horas e US$ 20 são apenas um exemplo; escolha os limites da rodada antes de começar e aplique os mesmos a todos os modelos.

> Você é o candidato `run-001` do benchmark Rabisco Tênis. Leia e execute integralmente `benchmark/PROMPT.md`. Sua entrada é a tag `benchmark-v3`. Você tem uma tentativa. Os limites desta rodada são 2 horas ou US$ 20 de uso, o que ocorrer primeiro. Trabalhe somente neste checkout, não consulte soluções de outros candidatos e não faça push. Ao terminar, faça um commit local e informe o SHA, as verificações executadas e as limitações conhecidas.

Quem organiza a rodada controla o tempo e o gasto; não dependa do modelo para medir o custo. Para o próximo candidato, crie outra cópia **da mesma tag** e troque apenas o ID (`run-002`, `run-003`...). Mantenha as implementações separadas até todas terminarem. Depois, avalie pela [rubrica](./benchmark/EVALUATION.md) e publique o código e o relatório conforme o [protocolo](./BENCHMARK.md).

Antes de cada execução, registre em privado qual modelo e nível de reasoning corresponde ao ID. No checkout do organizador, copie [`benchmark/RUN_MAP_TEMPLATE.csv`](./benchmark/RUN_MAP_TEMPLATE.csv) para `benchmark/run-map.private.csv` e preencha uma linha por run; esse arquivo é ignorado pelo Git. Após pontuar todos os candidatos, coloque essa identificação no `metadata.json` e no [índice de resultados](./benchmark/results/README.md). Assim a avaliação pode usar apenas o ID da run até as notas estarem fechadas.

Na **v3**, a [rubrica](./benchmark/EVALUATION.md) combina **70 pontos de avaliação humana** com **30 pontos de uma IA avaliadora independente**. A IA usa sempre o mesmo [prompt](./benchmark/AI_EVALUATOR_PROMPT.md) e configuração para todas as runs. As duas notas são registradas separadamente antes de calcular o total.
