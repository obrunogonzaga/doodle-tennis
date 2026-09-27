# PRD — Doodle Tênis

**Status:** proposta para o primeiro protótipo jogável  
**Referências visuais:** [conceito principal](./doodle-tennis-conceito.png), [quadra vazia](./references/quadra-vazia.png) e [personagens/interface](./references/personagens-interface.png)<br>
**Plataforma inicial:** navegador em computador, com teclado

## 1. Visão do produto

Doodle Tênis é um jogo curto de tênis de arcade que parece acontecer dentro de um caderno. O jogador controla a personagem mais próxima da câmera, troca bolas com um adversário simples e tenta vencer uma partida. Movimento, trajetória e resultado de cada golpe devem ser fáceis de entender, enquanto o cenário preserva o caráter artesanal da imagem conceitual.

O primeiro lançamento é um **protótipo para testar a diversão da troca de bolas e a legibilidade da estética**. Uma partida deve durar aproximadamente 2 a 4 minutos.

### Hipótese a validar

Controles de movimento lateral e rebatida por tempo de acerto, combinados com uma apresentação de papel e desenhos à mão, produzem uma experiência divertida e compreensível já na primeira partida.

### Público inicial

Pessoas que gostam de jogos rápidos e acessíveis no navegador. Não se pressupõe conhecimento das regras completas de tênis.

## 2. Objetivos e critérios de sucesso

1. Permitir iniciar, jogar e reiniciar uma partida completa sem instruções externas.
2. Fazer o jogador reconhecer a posição da bola, seu quique e a janela de rebatida durante a partida.
3. Manter a estética da referência sem sacrificar a leitura da quadra ou dos personagens.
4. Validar o núcleo com pelo menos três sessões de teste observadas: os jogadores devem entender os controles em até 30 segundos, concluir uma partida e conseguir explicar por que ganharam ou perderam os pontos.

Se a bola ou o momento da rebatida não forem claros nos testes, ajustar contraste, sombra, trajetória e tempo de contato antes de acrescentar novos recursos.

## 3. Escopo da primeira versão

### Incluído

- Partida individual contra um adversário controlado pelo jogo.
- Quadra fixa em perspectiva, com jogador embaixo e adversário em cima.
- Movimento lateral do jogador, golpe com um botão e assistência de direção para a bola cruzar a rede quando o contato for válido.
- Saque automático do adversário para iniciar cada ponto.
- Bola com trajetória visível, sombra no chão, quique e indicação visual de contato.
- Regras de ponto: bola na rede, fora da quadra, segundo quique ou rebatida não realizada.
- Placar `0 → 15 → 30 → 40 → jogo`; em `40–40`, o ponto seguinte decide a partida.
- Tela inicial com controles, estado de pausa, resultado final e opção de jogar novamente.
- Identidade visual inspirada diretamente na imagem da pasta.

### Fora do escopo nesta versão

- Multijogador, progressão, torneios, contas e salvamento.
- Regras completas de tênis, vantagem, sets ou escolha manual de saque.
- Golpes especiais, tipos de piso, personalização de personagens ou loja.
- Controles de toque e suporte mobile como requisito de lançamento.

## 4. Experiência de jogo

### Ciclo principal

1. O jogador vê os controles e inicia a partida.
2. O adversário saca automaticamente.
3. O jogador se posiciona para a bola e aperta o botão de golpe no momento certo.
4. A bola retorna para o lado oposto; o adversário tenta alcançá-la e devolvê-la.
5. A troca continua até ocorrer uma falta ou a bola quicar duas vezes.
6. O placar é atualizado, há uma pausa curta para entender o resultado e começa o próximo ponto.
7. Ao fim da partida, o jogador pode recomeçar.

### Controles

| Ação | Entrada inicial |
| --- | --- |
| Mover para a esquerda ou direita | `A` / `D` ou `←` / `→` |
| Rebater | `Espaço` |
| Pausar ou retomar | `Esc` |
| Iniciar ou reiniciar | `Enter` ou botão na interface |

O jogador se desloca apenas lateralmente na primeira versão. O golpe depende de estar próximo à bola e acioná-lo durante uma janela de contato visível. Um contato válido envia a bola automaticamente para uma área jogável do outro lado, com alguma variação de direção. O erro precisa ter uma causa reconhecível: posição, tempo de golpe, rede ou bola fora.

### Adversário

O adversário deve se mover em direção à previsão de quique com pequeno atraso e capacidade limitada de alcance. Ele consegue sustentar trocas curtas, mas também comete erros. A dificuldade inicial deve favorecer o aprendizado; seu objetivo é proporcionar uma boa troca de bolas, não simular um tenista real.

## 5. Direção visual e sonora

### Elementos obrigatórios da estética

- Papel pautado e textura quente como base do cenário.
- Quadra azul desenhada com linhas levemente irregulares, mantendo limites bem visíveis.
- Rede com desenho legível e separação clara entre as metades da quadra.
- Personagens com contorno de caneta azul, detalhes vermelhos e verdes e poses expressivas.
- Bola amarela como foco de maior contraste, com sombra e pequeno rastro de movimento.
- Placar em recorte de papel preso por fita, inspirado no topo da referência.
- Anotações e pequenos desenhos nas margens como decoração fora da área principal de jogo.

A [imagem conceitual](./doodle-tennis-conceito.png) mostra a composição desejada, mas não deve ser usada inteira como campo jogável: ela já contém bola, personagens, placar e trajetória estáticos. A [quadra vazia](./references/quadra-vazia.png) detalha o cenário sem esses elementos; a [prancha de personagens e interface](./references/personagens-interface.png) orienta poses, paleta e recortes de papel. As imagens são referências visuais, não recursos finais obrigatórios. O protótipo usará esses elementos como guia para criar camadas separadas. A quadra e os personagens podem ser redesenhados como SVGs ou imagens transparentes; a textura do papel pode vir de um recorte tratado das referências, se funcionar sem elementos estáticos indesejados. Veja também as [notas das referências](./references/README.md).

Animações discretas de traço e pequenas imperfeições devem sugerir desenho manual sem deslocar os limites reais da quadra. Um som curto para golpe, quique e ponto pode entrar após a jogabilidade e a clareza visual estarem validadas.

## 6. Requisitos funcionais e aceite

| ID | Requisito | Critério de aceite |
| --- | --- | --- |
| RF-01 | Iniciar e reiniciar | O jogador inicia e reinicia uma partida pela interface e pelo teclado. |
| RF-02 | Movimento | O personagem responde a ambas as opções de teclas e permanece na área permitida. |
| RF-03 | Rebatida | Um golpe válido altera a trajetória da bola uma única vez; um golpe fora da janela não rebate. |
| RF-04 | Física e ponto | A bola cruza a rede, quica e encerra o ponto corretamente em rede, fora ou segundo quique. |
| RF-05 | IA | O adversário alcança parte das bolas, devolve golpes válidos e pode errar. |
| RF-06 | Placar | Cada ponto atualiza o lado correto e a partida termina conforme a regra simplificada. |
| RF-07 | Pausa | Pausar congela a partida; retomar não concede um golpe ou ponto involuntário. |
| RF-08 | Clareza | Placar, controles e motivo do fim do ponto aparecem de forma legível. |

## 7. Tecnologia e estrutura

- **Runtime:** Phaser com TypeScript e Vite.
- **Apresentação:** canvas para quadra, personagens e bola; interface HTML/CSS sobreposta para menu, placar, pausa e resultado.
- **Estado do jogo:** regras de ponto, placar, posição e trajetória mantidas separadas do desenho da cena. A quadra possui coordenadas lógicas retangulares, projetadas visualmente na perspectiva da imagem.
- **Arte:** arquivos organizados por `characters`, `environment`, `ui`, `fx` e `audio`, com chaves estáveis para carregamento.
- **Formato:** área de jogo baseada na proporção 3:2 da referência, ajustada à janela do navegador sem cortar a quadra.

Essa separação permite ajustar o desenho e a perspectiva sem alterar as regras de bola dentro, fora ou contato.

## 8. Etapas de entrega

### Etapa 1 — Núcleo jogável

Montar o projeto, a quadra lógica, o movimento, a bola, a rebatida e a detecção de ponto com formas temporárias. **Saída:** duas personagens conseguem trocar bolas e um ponto termina corretamente.

### Etapa 2 — Partida completa

Adicionar adversário, placar, saque automático, telas de início/fim e pausa. **Saída:** uma pessoa consegue concluir e reiniciar uma partida sem intervenção de quem desenvolveu.

### Etapa 3 — Identidade do caderno

Criar camadas visuais separadas a partir da referência, aplicar personagens, bola, quadra e interface. **Saída:** o jogo lembra a imagem de conceito e continua fácil de ler em movimento.

### Etapa 4 — Teste e ajuste

Realizar ao menos três sessões observadas, registrar dificuldades e ajustar velocidade da bola, alcance do jogador, janela de golpe, IA e contraste. **Saída:** os critérios da seção 2 são atendidos, sem falhas que interrompam a partida.

## 9. Riscos e decisões abertas

| Tema | Risco ou decisão | Abordagem inicial |
| --- | --- | --- |
| Perspectiva | Uma bola aérea pode parecer tocar o chão antes do quique. | Usar sombra fixa no plano da quadra e animação separada de altura. |
| Arte | O conceito é uma imagem única com objetos estáticos. | Redesenhar os elementos jogáveis em camadas. |
| Dificuldade | Golpes por tempo de acerto podem frustrar iniciantes. | Começar com janela generosa e ajustar após observar testes. |
| Direção do golpe | O controle de apenas um botão pode reduzir a estratégia. | Usar assistência na primeira versão; avaliar mira manual somente após validar a troca de bolas. |
| Dispositivos | A quadra pode perder legibilidade em telas pequenas. | Priorizar desktop no primeiro lançamento e medir a necessidade de mobile nos testes. |

## 10. Definição de pronto do protótipo

O protótipo está pronto para avaliação quando uma pessoa consegue abrir o jogo no navegador, entender os controles pela tela inicial, jogar até o resultado final, identificar a causa de cada ponto e iniciar outra partida; a apresentação deve remeter claramente ao caderno da imagem de referência.
