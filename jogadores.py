from random import randint


tipos = ['IMPULSIVO', 'EXIGENTE', 'CAUTELOSO', 'ALEATORIO']


class Jogador:
    def __init__(self, tipo):
        self.saldo = 300
        self.tipo = tipo
        self.posicao_atual = 0

    def jogar_dado(self):
        return randint(1, 6)

    def calcula_posicao_tabuleiro(self):
        dado = self.jogar_dado()
        if self.posicao_atual + dado > 20:
            self.posicao_atual = self.posicao_atual + dado - 20
            self.saldo += 100
        else:
            self.posicao_atual += dado
        return self.posicao_atual

    def valida_rodada(self, propriedade):
        proprietario = propriedade.proprietario
        if proprietario is not None:
            self.saldo -= propriedade.aluguel
            propriedade.proprietario.saldo += propriedade.aluguel
        else:
            self.comprar_ou_nao(propriedade)

    def comprar_ou_nao(self, propriedade):
        if self.tipo == 'IMPULSIVO' or \
                self.tipo == 'EXIGENTE' and propriedade.aluguel > 50 or \
                self.tipo == 'CAUTELOSO' and self.saldo - propriedade.venda > 80:
            comprar = 1
        elif self.tipo == 'ALEATORIO':
            comprar = randint(0, 1)
        else:
            comprar = 0

        if comprar:
            if self.saldo - propriedade.venda >= 0:
                self.saldo -= propriedade.venda

    def libera_propriedades(self, tabuleiro):
        for propriedade in tabuleiro:
            if propriedade.proprietario == self:
                propriedade.proprietario = None

    @staticmethod
    def get_jogadores_rodada():
        return [Jogador(tipo) for tipo in tipos]
