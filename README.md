# Projeto-IP: Medieval Jumper

"Doodle Jump" é um popular jogo de plataforma para dispositivos móveis, onde os jogadores controlam um personagem que salta de plataforma em plataforma para alcançar alturas cada vez maiores. O objetivo é evitar obstáculos, inimigos e coletar power-ups enquanto sobe. O jogo é conhecido por sua jogabilidade simples, mas viciante, e desafia os jogadores a baterem seus recordes pessoais.

Nos inspiramos no "Doodle Jump" para criar um jogo semelhante, com mecânicas de salto e escalada vertical, desafios crescentes e a oportunidade para os jogadores aumentar o tempo para alcançar alturas cada vez maiores. 

## Contribuições dos Integrantes:

- [Karolyne Rocha](https://github.com/karolrocha): Criou os coletáveis e suas mecânicas, design e display. Implementou o pulo duplo do personagem e o design das plataformas. 
- [Lucas Oliveira](https://github.com/lucvseco): Criou a tela inicial e ajudou na parte do game over.
- [Lucas Alexandre](https://github.com/LucasalMarques): Trabalhou nas plataformas e tela cheia.
- [Gabriel Marques](https://github.com/gabriel-gma5): Criou o personagem, suas funcionalidades e o mapa do jogo, além de ajudar outros integrantes.
- [Leandro Lucas](https://github.com/LeandroLucas8520): Gerenciou o projeto, reestruturou o código e criou a tela de game over.


## Recursos Utilizados no Projeto:

### Programação Orientada a Objetos (POO):

A Programação Orientada a Objetos (POO) é um paradigma de programação que se baseia na criação de objetos, que são instâncias de classes. No contexto do nosso projeto, POO foi usado para criar objetos que representam elementos do jogo, como o player, coletáveis, troca de tela e cenário.
A utilização de POO ajuda a organizar o código de forma mais modular, facilitando a manutenção e o entendimento do projeto.
### Laços de Repetição e Condicionais:

Laços de repetição, como for e while, são usados para executar um conjunto de instruções várias vezes. Eles são essenciais em jogos para atualizar o estado do jogo, como a posição dos objetos em cada quadro.
Esses elementos foram fundamentais para criar a lógica do jogo e para garantir que ele responda corretamente às ações do jogador.
### Listas:

No contexto do jogo, listas podem ser usadas para várias finalidades.
Por exemplo, foram usadas para armazenar as posições das plataformas no cenário, permitindo que o jogo saiba onde colocá-las e como atualizá-las.
Além disso, listas podem ser usadas para controlar a quantidade de coletáveis no jogo, permitindo que você defina um número máximo e remova-os da lista quando forem coletados.
### Tuplas:

Tuplas são estruturas de dados semelhantes às listas, mas são imutáveis, ou seja, seus elementos não podem ser alterados após a criação. No Pygame, as tuplas foram usadas para definir as cores dos objetos, as posições iniciais dos elementos no jogo ou as dimensões de uma imagem.
### Dicionários:

Eles são úteis para armazenar informações que podem ser acessadas de forma eficiente usando uma chave específica.
No nosso projeto, dicionários foram usados para armazenar informações sobre a movimentação do personagem, como mapear teclas do teclado para ações no jogo.

## Bibliotecas Utilizadas:
1. Pygame: Fornecendo funcionalidades para o jogo.
2. Random: Usado para a geração de plataformas e decisões quanto à probabilidade de aparecimento de coletáveis ao longo do jogo.
3. OS: Ela é uma biblioteca de comandos do sistema operacional que vai te auxiliar a fazer algumas operações dentro do seu computador.

## Divisão do Projeto em Módulos:

1. Classe Telas: Armazena os módulos de tela inicial, tela do jogo e a tela de game over.
2. Cenário: Inclui a classe plataforma.
3. Coletáveis: Responsável pelas botas, que permitem os pulos duplos; as moedas e o tempo extra.
4. Funcs: Armazena variáveis importantes.
5. Menu: Funciona como o menu do jogo, permitindo iniciar o jogo e sair.
6. Player: Gerencia as questões relacionadas ao jogador, além de guardar informações importantes, como a quantidade de cada coletável.

## Desafios e Aprendizados:

### Primeiro Tópico - Subestimação do Projeto:

O maior erro foi subestimar o projeto. Achávamos que o projeto seria fácil, pois estaríamos utilizando uma biblioteca pré-definida, o que nos levou a pensar que seria mais simples. No entanto, tomamos um choque de realidade quando efetivamente começamos a trabalhar no projeto e percebemos que não seria tão simples como imaginávamos.

Lidamos: Tivemos que ajustar nossas expectativas e abordagem. Foi como um choque de realidade quando percebemos que o projeto era realmente complexo. Então, nos comprometemos a trabalhar mais duro e a estudar pra conseguir entregar um bom trabalho.

### Segundo Tópico - Desafio com o Tempo:

O segundo grande desafio que enfrentamos foi o gerenciamento do tempo, especialmente porque estávamos no final do período letivo e enfrentávamos muitos contratempos, incluindo a necessidade de lidar com várias provas e projetos de outras disciplinas em um curto espaço de tempo.

Lidamos: Para enfrentar esse desafio, implementamos um sólido gerenciamento de projeto. Isso nos permitiu dividir as tarefas de forma equitativa e eficiente, garantindo que ninguém ficasse sobrecarregado. Além disso, estabelecemos prioridades e prazos para manter o projeto dentro do cronograma.

### Terceiro Tópico - Experiência de Trabalho em Grupo e Outros Aprendizados:

Nesse terceiro ponto, adquirimos uma valiosa experiência de trabalho em grupo, aprendemos sobre o versionamento de código com o Git/GitHub, desenvolvemos habilidades de gerenciamento de tempo e aplicamos os conceitos que aprendemos em sala de aula para criar um projeto real e tangível.

## Como jogar 
 ### Inicializando
 1. É necessário instalar a biblioteca PyGame para executar o jogo utilizando o comando "pip install pygame" no cmd.
 2. Clone/baixe o repositório em sua máquina para ter acesso ao código
 3. Após instalar a biblioteca PyGame o arquivo zip em sua máquina local, execute o arquivo "main_menu.py"
 ### Jogabilidade
A - Move para esquerda<br>
D - Move para direita<br>
Barra de espaço - Pula<br>
E - Pulo duplo (Power-up)
### Itens
TIMER - Aumenta +10seg de tempo de sobrevivência <br>
GOLD - Moedas coletáveis<br>
BOTA - Power-up para pulo duplo<br>