from enderecos import *

class Sonic(object):

    vidas=None
    aneis=None
    posX=None
    posY=None
    velocidade=None
    ato = None
    zona = None

    gerenciadorMemoria=None
    def __init__(self,gerenciadorMemoria):
        self.vidas = None
        self.aneis = None
        self.posX = None
        self.posY = None
        self.velocidade = None
        self.ato = None
        self.zona = None
        self.gerenciadorMemoria = gerenciadorMemoria





    def atualizarPersoangem(self):
        self.vidas = self.gerenciadorMemoria.lerByte(VIDAS)
        self.aneis = self.gerenciadorMemoria.lerPalavra(ANEIS)
        self.posX = self.gerenciadorMemoria.lerPalavra(POSX)
        self.posY = self.gerenciadorMemoria.lerPalavra(POXY)
        self.velocidade = self.gerenciadorMemoria.lerPalavra(VELOCIDADE)
        self.ato = self.gerenciadorMemoria.lerByte(ACT)
        self.zona = self.gerenciadorMemoria.lerByte(ZONA)