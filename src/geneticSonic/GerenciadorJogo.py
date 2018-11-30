from Sonic import *
from KeyController import *
from MemoryHandler import *
from solucao import *
from operator import *


TAMANHOGER = 5
MELHORES = 0.6
MUTACAO = 0.05
RESETGERACOES = 4
class GerenciadorJogo(object):

    geracao = 0
    gerenciadorMemoria = None
    controladorTeclado = None
    sonic = None
    vetorSolucoes = []
    tempoLimite = 3

    melhorSolucaoGerAnterior = 0
    resetSolucoes=0


    maxDistance = 0

    melhorSolucao = None

    auxSolucao = None

    indiceSolucao = 0

    def __init__(self,nomeProcesso):
        self.geracao = 0
        self.gerenciadorMemoria = MemoryHandler(nomeProcesso)
        self.controladorTeclado = keyController()
        self.sonic = Sonic(self.gerenciadorMemoria)

        self.melhorSolucao = solucao()

        for i in range (0,TAMANHOGER):
            individuo = solucao()
            individuo.geracao=0
            individuo.gerarSolucaoAleatoria()
            self.vetorSolucoes.append(individuo)






    def iniciar(self):

        while True:
            self.executarsolucao()
            pass




    def executarsolucao(self):
        self.resetGame()
        if (self.indiceSolucao>=TAMANHOGER):
            self.proximaSolucao()
            self.indiceSolucao=0

        solucao = self.vetorSolucoes[self.indiceSolucao]
        quantidadeComandos = len(solucao.comandos)
        comandos = solucao.comandos
        tempoComandos = solucao.tempoComandos
        self.sonic.atualizarPersoangem()
        tempoPassado = 0
        for i in range (0,quantidadeComandos):
            self.sonic.atualizarPersoangem()
            qualidadeAntiga = solucao.qualidade
            tempoInicial = time()
            vidaAnterior = self.sonic.vidas
            distanciaAntiga = self.sonic.posX
            quantidadeAneisAntiga = self.sonic.aneis

            self.controladorTeclado.pressionar(comandos[i],tempoComandos[i])
            self.sonic.atualizarPersoangem()
            vidaAtual = self.sonic.vidas
            distanciaAtual = self.sonic.posX
            quantidadeAneisNova = self.sonic.aneis
            tempoFinal = time()
            self.fitnessAneis(solucao,quantidadeAneisAntiga,quantidadeAneisNova)
            self.fitnessDistancia(solucao,distanciaAntiga,distanciaAtual)
            novaQualidade = solucao.qualidade

            if (novaQualidade-qualidadeAntiga<=0):
                tempoPassado+= tempoFinal-tempoInicial
            else:
                tempoPassado=0

            if (tempoPassado>=2):
                if (self.melhorSolucaoGerAnterior <= solucao.qualidade):
                    self.melhorSolucaoGerAnterior = solucao.qualidade
                solucao.qualidade = solucao.qualidade - solucao.qualidade*0.5-2
                self.verificaSolucao(solucao)
                self.resetGame()
                self.proximaSolucao()
                return


            if (vidaAtual<vidaAnterior):
                if (self.melhorSolucaoGerAnterior <= solucao.qualidade):
                    self.melhorSolucaoGerAnterior = solucao.qualidade
                solucao.qualidade-=solucao.qualidade*0.5
                self.verificaSolucao(solucao)
                self.resetGame()
                self.proximaSolucao()
                return

        if (self.melhorSolucaoGerAnterior<=solucao.qualidade):
            self.melhorSolucaoGerAnterior=solucao.qualidade


        self.verificaSolucao(solucao)
        self.proximaSolucao()


    def resetInvididuos(self):
        self.vetorSolucoes.clear()
        for i in range (0,TAMANHOGER):
            self.vetorSolucoes.append(solucao.gerarSolucaoAleatoria())



    def verificaSolucao(self,solucaoAtual):
        if (self.melhorSolucao.qualidade<solucaoAtual.qualidade):
            self.melhorSolucao.qualidade= solucaoAtual.qualidade
            self.melhorSolucao.comandos.clear()
            self.melhorSolucao.tempoComandos.clear()

            for comando in solucaoAtual.comandos:

                self.melhorSolucao.comandos.append(comando)

            for tempo in solucaoAtual.tempoComandos:
                self.melhorSolucao.tempoComandos.append(tempo)

            self.melhorSolucao.geracao = solucaoAtual.geracao
        print ("Melhor Solução atual:")
        print ("Geração: "+str(self.melhorSolucao.geracao))
        print ("Qualidade da solução: "+str(self.melhorSolucao.qualidade))

    def fitnessAneis(self,solucao,antigo,novo):
        delta = novo - antigo

        if (delta>=0):
            solucao.qualidade+=(0.05*delta)*solucao.qualidade
        else:
            solucao.qualidade-=(0.25*solucao.qualidade)




    def fitnessDistancia(self,solucao,antigo,novo):
        delta = novo - antigo


        if (delta>0 and novo > self.maxDistance):
            self.maxDistance = novo

            solucao.qualidade+=(delta)


    def proximaSolucao(self):
        if (self.indiceSolucao<TAMANHOGER):
            self.indiceSolucao  = self.indiceSolucao + 1
        else:

            if (self.melhorSolucaoGerAnterior<=self.melhorSolucao.qualidade):
                self.resetSolucoes+=1
                print("Não houve melhoria nesta geração")

            if (self.resetSolucoes==RESETGERACOES):
                self.resetSolucoes=0
                print ("Resetando indivíduos atuais ( mantendo melhor solução obtida )")
                self.resetInvididuos()



            self.indiceSolucao=0
            self.geracao= self.geracao +1
            print("Geração: "+ str(self.geracao))
            self.cruzamento()

            pass

    def atualizarPersonagem(self):
        self.sonic.atualizarPersoangem()



    def resetGame(self):
        self.maxDistance=0
        self.controladorTeclado.pressionar(6,0.1)

    def cruzamento(self):
        self.indiceSolucao=0
        print ("Iniciando Cruzamento !!!")
        print ("Geração Atual:"+str(self.geracao))
        self.vetorSolucoes.sort(key=attrgetter('qualidade'), reverse=True)
        vetorCruzamento = []

        melhores = int(len(self.vetorSolucoes) * MELHORES)


        for i in range (0,melhores):
            elementoAuxiliar = solucao()
            elementoAuxiliar.geracao=self.geracao
            elementoAuxiliar.tempoComandos=[]
            elementoAuxiliar.comandos=[]
            elementoAuxiliar.qualidade=0

            solucaoAuxiliar = self.vetorSolucoes[i]


            for j in range(0,len(solucaoAuxiliar.comandos)):
                valor  = uniform(0,1)
                if (valor>=0.5):
                    elementoAuxiliar.comandos.append(solucaoAuxiliar.comandos[j])
                    elementoAuxiliar.tempoComandos.append(solucaoAuxiliar.tempoComandos[j])
                else:
                    elementoAuxiliar.comandos.append(self.melhorSolucao.comandos[j])
                    elementoAuxiliar.tempoComandos.append(self.melhorSolucao.tempoComandos[j])
                    pass

            vetorCruzamento.append(elementoAuxiliar)

        resto = TAMANHOGER-melhores

        for i in range (0,resto):
            elementoAuxiliar = solucao()
            elementoAuxiliar.geracao=self.geracao
            elementoAuxiliar.tempoComandos=[]
            elementoAuxiliar.comandos=[]
            elementoAuxiliar.qualidade=0
            elementoAuxiliar.gerarSolucaoAleatoria()
            vetorCruzamento.append(elementoAuxiliar)

        self.vetorSolucoes.clear()

        for solucoesCruzadas in vetorCruzamento:
            self.vetorSolucoes.append(solucoesCruzadas)