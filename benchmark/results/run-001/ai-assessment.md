# Avaliação técnica da IA — run-001

**Rubrica:** `benchmark-v4`<br>
**Identidade do candidato:** oculta até fechar as notas<br>
**Modelo avaliador:** `gpt-6-sol`, reasoning `high`; versão interna não informada

A avaliação usou uma cópia limpa da tag `benchmark-v4` separada do commit entregue pelo candidato. As notas humanas e o mapeamento privado não foram fornecidos ao avaliador. As notas abaixo cobrem somente a coluna IA da rubrica.

| Tarefa | Nota 0–4 | Evidência e falha observada |
| --- | ---: | --- |
| 01 · Projeto | 4 | `npm ci`, `npm run dev` e `npm run build` concluíram; o navegador não registrou erros de página ou HTTP. Regras em `src/game/simulation.ts`, entradas em `src/game/input.ts` e desenho em `src/game/view.ts`. |
| 02 · Quadra e movimento | 4 | Em 1536 × 1024, A, D e ambas as setas foram mantidas até os extremos sem tirar o jogador dos limites. `src/game/geometry.ts` define a quadra lógica e `src/game/view.ts` projeta as coordenadas. Em 1280 × 800, a área 3:2 coube inteira em 1200 × 800. |
| 03 · Bola e ponto | 4 | Trajetórias determinísticas sobre `TennisMatch` encerraram pontos em rede, fora e segundo quique com vencedor correto e apenas uma pontuação. `src/game/simulation.ts` verifica altura ao cruzar a rede e limites no primeiro quique. Bola e sombra foram observadas no navegador. |
| 04 · Rebatida | 4 | Teste independente da simulação rejeitou golpes cedo e longe, aceitou um contato válido e rejeitou uma segunda tentativa. No navegador, o aviso “AGORA!” seguido de Espaço produziu “BOA!” e a devolução. |
| 05 · Adversário | 4 | No navegador, quatro contatos válidos ocorreram na mesma troca sem mudança do placar, confirmando devoluções. Teste independente confirmou devolução alcançável e erro controlado; `src/game/simulation.ts` aplica atraso e velocidade limitada ao adversário. |
| 06 · Partida e telas | 4 | No navegador, a partida chegou a “JOGO”, reiniciou por Enter com 0–0 e respondeu aos botões “COMEÇAR”, pausa e “CONTINUAR”. O canvas permaneceu idêntico após um segundo pausado. Teste determinístico confirmou vitória no ponto seguinte a 40–40. |
| 07 · Arte em camadas | 4 | `src/game/assets.ts` mantém chaves separadas; SVGs distintos representam personagens, poses e bola. `src/game/view.ts` cria objetos independentes para papel, quadra, rede, jogadores, sombra, rastro e bola; `src/ui.ts` atualiza o placar em HTML. A inspeção visual não encontrou bola ou personagens fixos no cenário. |
| 08 · Integração visual | 4 | Inspeção em 1536 × 1024 mostrou início, troca e resultado legíveis. Em 1280 × 800, `.game-shell` mediu 1200 × 800 sem corte; placar, controles e quadra permaneceram visíveis. Não houve erro de página ou resposta HTTP com falha. |

## Comandos e ambiente

- `npm ci`: sucesso.
- `npm run dev`: Vite iniciou em `http://127.0.0.1:5177/`.
- `npm run build`: sucesso, com aviso de bundle acima de 500 kB.
- `npm test`: seis testes passaram.
- `npm run test:browser`: passou. O avaliador também fez verificações independentes no Chromium headless em 1536 × 1024.
- PRD, rubrica, prompt e tarefas 01–08 do candidato não divergiram da cópia limpa da tag nos diffs executados.
- Capturas da execução estão em `screenshots/` nesta pasta.

## Limitações da avaliação

Falhas de rede e fora foram reproduzidas por trajetórias determinísticas na simulação; não ocorreram durante a sessão no navegador. O aviso de bundle não impediu o build nem a execução.
