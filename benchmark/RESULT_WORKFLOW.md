# Registrar e publicar uma avaliação v4

Este é o fluxo do **organizador**, executado no checkout da branch `main`. A entrada dos candidatos e a rubrica continuam congeladas na tag `benchmark-v4`; estes arquivos operacionais podem evoluir sem alterar a partida recebida pelos candidatos.

## Antes da primeira run

1. Conferir [`EVALUATOR_CONFIG.json`](./EVALUATOR_CONFIG.json): nesta rodada, a IA técnica é `gpt-6-sol` com reasoning `high` (“Sol 6 Alto”). Usar a mesma configuração, ferramentas e ambiente em todas as avaliações. Se a plataforma informar uma revisão mais específica do modelo, registrá-la no resultado; caso contrário, manter `model_version` como `null`.
2. Criar `benchmark/run-map.private.csv` a partir de [`RUN_MAP_TEMPLATE.csv`](./RUN_MAP_TEMPLATE.csv). Registrar ali o ID anônimo, modelo candidato, versão, reasoning e branch. O arquivo privado é ignorado pelo Git.
3. Para cada candidato, iniciar um checkout isolado da tag `benchmark-v4`. Não publicar as branches até todos terminarem.

## Preparar a pasta da run

No checkout `main` do organizador:

```bash
python3 benchmark/prepare_result.py run-001
```

Isso cria `benchmark/results/run-001/` com metadados, notas vazias, modelos de avaliação humana e da IA, relatório e pasta para capturas. O script registra automaticamente o SHA da tag e a configuração fixa da IA. A pasta permanece **local e sem push** até todas as runs da rodada estarem avaliadas.

Quando o candidato terminar, registrar o SHA completo de seu commit em `metadata.json` e no mapeamento privado. Registrar também horário, limites e uso real quando disponíveis.

## Avaliações independentes

1. **IA:** abrir uma conversa ou processo separado com `gpt-6-sol` e reasoning `high`. Fornecer o ID da run, o checkout anônimo do candidato e os arquivos de especificação de uma cópia limpa da tag `benchmark-v4`. Enviar o conteúdo de [`AI_EVALUATOR_PROMPT.md`](./AI_EVALUATOR_PROMPT.md) daquela tag. Não enviar identidade do candidato, mapeamento privado ou notas humanas. Salvar a resposta com notas e evidências em `ai-assessment.md`; transcrever as oito notas para a seção `ai` de `scores.json`.
2. **Humano:** jogar com o roteiro da [rubrica](./EVALUATION.md), sem ver a avaliação da IA, e preencher `human-assessment.md`. Transcrever as sete notas para a seção `human` de `scores.json` e o número de sessões observadas para `human_playtest_sessions` em `metadata.json`. Guardar capturas em `screenshots/` e um trecho de log limpo em `build.txt` somente se ele sustentar alguma conclusão.
3. Verificar que cada nota de 0 a 4 tem evidência correspondente nos arquivos de avaliação. Resolver divergências de 2 pontos ou mais segundo a rubrica, mantendo registro da nota original e da eventual revisão.

Mensagem de abertura para a IA avaliadora, trocando apenas o ID e os caminhos:

> Avalie a run `run-001`. O checkout anônimo do candidato está em `<pasta-da-run>`; a especificação limpa está em `<pasta-da-tag-benchmark-v4>`. Leia e siga integralmente `benchmark/AI_EVALUATOR_PROMPT.md` da especificação limpa. Não edite o candidato. Entregue notas de 0 a 4 e evidência por tarefa para eu registrar em `ai-assessment.md` e `scores.json`.

O repositório **não invoca automaticamente** a IA: o organizador inicia a conversa/processo com o modelo fixado e salva a resposta. O script abaixo calcula e persiste a pontuação depois que as duas avaliações estão completas.

## Calcular e fechar as notas

```bash
python3 benchmark/finalize_result.py run-001
```

O script valida IDs, tag, SHA do candidato, modelo avaliador e preenchimento dos arquivos; executa o cálculo 70/30 e grava `score-summary.json` e os subtotais em `metadata.json`. Ele marca automaticamente `evaluation_status` como `provisional` enquanto houver menos de três sessões humanas e como `final` quando houver pelo menos três. Identificar notas provisórias no relatório.

Depois que **todas** as runs da rodada estiverem pontuadas, revelar o mapeamento privado e preencher `model`, `model_version` e `reasoning_effort` em cada `metadata.json`. Completar `report.md` e o [índice de resultados](./results/README.md). Publicar as branches de código e, em seguida, os resultados na `main`. Não publicar `run-map.private.csv` nem logs com segredos.
