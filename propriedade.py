from random import randint


# 1,15; 16,30; 31;45; 46,60

class Propriedade:
    MIN = 1
    MAX = 60
    TAXA_VENDA = 10

    def __init__(self):
        self.aluguel = randint(self.MIN, self.MAX)
        self.venda = self.aluguel * self.TAXA_VENDA
        self.proprietario = None

    def colocar_proprietario(self, proprietario):
        self.proprietario = proprietario


tabuleiro = [Propriedade() for i in range(20)]
