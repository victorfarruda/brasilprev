from random import randint


# 1,15; 16,30; 31;45; 46,60
class Propriedade:
    def __init__(self):
        self.aluguel = randint(1, 80)
        self.venda = self.aluguel * 10
        self.proprietario = None


tabuleiro = [Propriedade() for i in range(20)]
