# Rubrica de avaliação — benchmark v4

## Composição da nota

A avaliação é independente em duas partes: **70 pontos humanos** para a experiência de jogar e **30 pontos da IA** para verificações técnicas. Nenhum candidato avalia a própria entrega. A IA usa sempre o mesmo modelo, versão, nível de reasoning, prompt e ferramentas em todas as runs. O avaliador humano e a IA registram suas notas antes de ver as notas um do outro e antes de revelar qual modelo implementou cada run.

| Tarefa | O humano observa | A IA verifica | Humano | IA |
| --- | --- | --- | ---: | ---: |
| 01 · Projeto | — | Instalação, inicialização, build e separação básica de responsabilidades | 0 | 10 |
| 02 · Quadra e movimento | Controles e limites perceptíveis | Coordenadas lógicas, projeção e limites | 8 | 2 |
| 03 · Bola e ponto | Clareza da trajetória, quique e resultado | Regras de rede, fora, segundo quique e resultado único | 11 | 4 |
| 04 · Rebatida | Justiça e feedback do tempo de contato | Validação de contato e ausência de golpes duplicados | 13 | 2 |
| 05 · Adversário | Qualidade das trocas e dificuldade inicial | Saque, movimento, erros e reinício de ponto | 8 | 2 |
| 06 · Partida e telas | Compreensão do placar, pausa e reinício | Regras de pontuação e transições de estado | 11 | 4 |
| 07 · Arte em camadas | Fidelidade à estética de desenho à mão | Separação dos recursos móveis e organização | 7 | 3 |
| 08 · Integração visual | Legibilidade e apresentação no desktop | Layout, redimensionamento e erros de interface | 12 | 3 |
| **Total** | | | **70** | **30** |

Os pesos são fixados em [`WEIGHTS.json`](./WEIGHTS.json). Cada avaliador atribui uma nota de **0 a 4** por tarefa em que tem peso: 0 = ausente ou impossível de observar; 1 = tentativa sem funcionamento útil; 2 = parcialmente funcional com falhas relevantes; 3 = funcional com falha menor; 4 = critérios de aceite atendidos. A pontuação é `peso × nota / 4`. A soma das duas partes produz a nota final sobre 100. Usar [`score.py`](./score.py) com uma cópia preenchida de [`SCORE_TEMPLATE.json`](./SCORE_TEMPLATE.json) para calcular a nota sem arredondamentos manuais.

## Roteiro humano

1. Receber somente o ID anônimo e a versão executável da run. Não consultar código, identidade do modelo ou nota da IA.
2. Abrir no mesmo navegador, em viewport **1536 × 1024**, e observar tela inicial e instruções por até 30 segundos, sem explicação externa.
3. Jogar ao menos uma partida completa. Tentar deslocar-se para os dois lados, rebater cedo e tarde, pausar, retomar e reiniciar.
4. Registrar por tarefa os pontos fortes, falhas e capturas equivalentes de início, troca e fim. Atribuir as notas humanas antes de ler a avaliação da IA.
5. Para cumprir a validação do PRD, fazer ao menos três sessões observadas com pessoas que não desenvolveram o jogo, sob as mesmas instruções para todas as runs. Se essas sessões ainda não ocorreram, marcar o resultado como **provisório**.

## Roteiro da IA avaliadora

1. Receber apenas o ID e o checkout anônimo do candidato. Ler PRD, tarefas, rubrica e [prompt de avaliação](./AI_EVALUATOR_PROMPT.md) numa cópia limpa da tag `benchmark-v4`, nunca na cópia potencialmente alterada pelo candidato. Não receber o mapeamento privado, notas humanas ou soluções anteriores.
2. Em ambiente limpo, executar instalação, `npm run dev` e `npm run build`; registrar comandos, erros e logs relevantes. Usar o mesmo navegador e viewport do roteiro humano quando testar a interface.
3. Examinar código e comportamento para atribuir somente as notas da coluna IA. Não inferir que uma função existe apenas porque o README diz que existe.
4. Entregar notas de 0 a 4 para as oito tarefas, com evidência verificável para cada uma. Não editar o código do candidato e não atribuir notas humanas.

Se o jogo não iniciar, registrar a falha. Itens que não podem ser observados recebem zero, inclusive na parte humana. Se as notas humana e da IA diferirem em **2 pontos ou mais** numa tarefa, revisar as evidências e repetir a verificação relevante antes de fechar o resultado; preservar ambas as notas originais e registrar qualquer correção. Não mudar pesos após ver os resultados.

## Publicação e desempate

Depois de fechar todas as notas, revelar o mapeamento de run para modelo, gerar o total e publicar `scores.json`, `metadata.json`, relatório e capturas na pasta da run. Reportar também tempo e custo, sem incorporá-los aos 100 pontos. Para desempatar: maior subtotal nas tarefas 03–06; depois, maior subtotal nas tarefas 07–08; por fim, menos falhas bloqueantes.

Juízes baseados em LLM podem ter vieses próprios. O uso de um prompt fixo, identidade oculta, evidência por item e peso humano maior reduz a dependência de uma única opinião automatizada; veja a pesquisa [Judging LLM-as-a-Judge](https://arxiv.org/abs/2306.05685).
