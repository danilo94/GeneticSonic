from random import *


MAXIMOCOMANDOS = 550


class solucao(object):

    geracao = 0
    qualidade = 0
    comandos = []
    tempoComandos = []


    def __init__(self):
        self.geracao = 0
        self.qualidade = 0
        self.comandos = []
        self.tempoComandos = []

    def gerarSolucaoAleatoria(self):

        for i in range (0,MAXIMOCOMANDOS):
            indice = randint(0, 3)
            self.comandos.append(indice)
            self.tempoComandos.append(uniform(0.5,1.5))