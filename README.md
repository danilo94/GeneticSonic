# ![Sonic](https://github.com/danilo94/GeneticSonic/blob/master/imgs/msonic.gif) Genetic Sonic
 Um Algoritmo Genético para o jogo Sonic The Hedgehog 1.

![Sonic](https://github.com/danilo94/GeneticSonic/blob/master/imgs/dev.PNG) 
## Motivação
 Implementação de um algoritmo genético capaz de jogar e eventualmente, passar as fases do jogo sonic the hedgehog 1. Se trata de uma implementação baseada no conceito de algoritmos genéticos, que utiliza o conceito da evolução dos seres vivos para que eventualmente o algoritmo consiga vencer os desafios da fase e chegar até o final.
### Pre-requisitos
Este programa é composto por um Dashboard, que foi implementado em Electron, e pela implementação do algoritmo genético que foi implementada em python. Com isso será necessária a instalação das seguintes dependências para execução do algoritmo:


```
* [Python 3](https://www.python.org/downloads/) - Implementação do algoritmo Genético
* [Node JS](https://nodejs.org/) - Implementação do Dashboard (Opcional)

* [Gens](https://segaretro.org/Gens/GS) - Emulador Utilizado para rodar o jogo
* [Alguma Hack Rom do jogo] - ¯\_(ツ)_/¯

```

###  ![Sonic](https://github.com/danilo94/GeneticSonic/blob/master/imgs/control.gif)  Configurando o Emulador

Para que o algoritmo genético consiga jogar o jogo normalmente, será necessário utilizar o buffer do teclado diretamente, logo este ficará impossibilitado de ser utilizado. Também será necessário configurar as teclas do teclado na seguinte ordem: I ( Cima ), K (Baixo), L (Direita), J (Esquerda). Será também necessário criar um ponto de partida na fase em que deseja jogar. Para isso basta pressionar F5 no inicio da fase que deseja começar :) .


### ![Sonic](https://github.com/danilo94/GeneticSonic/blob/master/imgs/sonicrun.gif) Rodando o pela primeira vez

Ao rodar o algoritmo deve se levar em consideração que como utilizamos o buffer do teclado para injetar os comandos, é necessário que o emulador esteja SEMPRE em foco na tela. Sabendo disso, para executar tanto o dashboard, quanto o algoritmo genético basta executar o seguinte conjunto de passos no prompt de comando do windows.


```
npm install - Deve ser executado uma única vez para baixar as dependências do projeto
npm start - Irá inicializar o dashboard.
Abrir o Gens e carregar a rom do jogo.
python main.py - Dentro da pasta do emulador
```
O código irá aguardar cerca de 3 segundos para que o usuário posicione a tela do emulador em foco e o processo evolutivo irá iniciar.


### ![eggman](https://github.com/danilo94/GeneticSonic/blob/master/imgs/egg.gif) Contribua !

Se você gostou do projeto, faça um fork e contribua adicionando novas funcionalidades e corrigindo bugs tanto no algoritmo genético quanto no dashboard.


### Assista em tempo real
Se você curtiu o projeto se inscreva nos dois canais e ajude o projeto a alcançar mais pessoas :D.

* [Sonic Bot](https://www.youtube.com/channel/UCKKpIwiQ8cANH-Fb1dYGDgA) - Live onde é possível ver o algoritmo jogando as fases
* [Dan Maker](https://www.youtube.com/channel/UCZbZ0IEMOoLiDxAGM7KBXwA?view_as=subscriber) - Canal do criador do projeto

