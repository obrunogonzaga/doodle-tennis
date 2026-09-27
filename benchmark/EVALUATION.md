# Rubrica de avaliação — benchmark v1

## Procedimento comum

1. Registrar o commit final do candidato e as condições de execução descritas em `BENCHMARK.md`.
2. Em ambiente limpo, executar os comandos documentados para instalar dependências, iniciar e gerar o build. Registrar falhas sem modificar o código entregue.
3. Abrir o jogo no mesmo navegador e em viewport **1536 × 1024**. Verificar console, tela inicial, controles, pontos, pausa, resultado e reinício.
4. Jogar pelo menos uma partida completa. Tentar também um golpe cedo, um golpe tarde, um segundo quique e uma bola na rede ou fora, quando a versão permitir.
5. Fazer capturas equivalentes da tela inicial, de uma troca de bolas e do resultado final. Avaliar a arte comparando com a imagem conceitual, sem acesso ao nome do modelo quando possível.
6. Registrar observações por tarefa e evidências. Quando houver playtests com pessoas, usar as mesmas instruções, tempo e participantes para todos os candidatos.

## Pontuação

Cada tarefa recebe nota de **0 a 4**: 0 = ausente; 1 = tentativa sem funcionamento útil; 2 = parcialmente funcional com falhas relevantes; 3 = funcional com falha menor; 4 = todos os critérios de aceite atendidos. A pontuação da tarefa é `peso × nota / 4`. Não presumir funcionamento por leitura de código: verificar no jogo sempre que possível.

| Tarefa | Dimensão | Peso |
| --- | --- | ---: |
| 01 | Projeto inicia, gera build e tem estrutura reproduzível | 10 |
| 02 | Quadra lógica, projeção e movimento | 10 |
| 03 | Trajetória, quique e fim de ponto | 15 |
| 04 | Rebatida e feedback de contato | 15 |
| 05 | Saque e adversário | 10 |
| 06 | Placar, pausa e ciclo da partida | 15 |
| 07 | Elementos visuais de rabisco em camadas | 10 |
| 08 | Integração visual, legibilidade e adaptação desktop | 15 |
| **Total** | | **100** |

Se o jogo não iniciar, registrar isso explicitamente e atribuir zero aos comportamentos impossíveis de observar. Não inferir pontos de jogabilidade a partir de intenções descritas no README. Publicar o total junto com as notas por tarefa, evidências, falhas e condições da rodada.

## Critérios de desempate

1. Maior nota conjunta nas tarefas 03, 04, 05 e 06, que compõem a partida jogável.
2. Maior nota conjunta nas tarefas 07 e 08, que medem a estética de rabisco.
3. Menor número de falhas bloqueantes observadas na partida completa.

Tempo e custo são informados ao lado da pontuação, não incorporados ao total: isso permite comparar qualidade e eficiência sem ocultar uma pela outra.
