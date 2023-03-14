from random import randint


tipos = ['IMPULSIVO', 'EXIGENTE', 'CAUTELOSO', 'ALEATORIO']


class Jogador:
    def __init__(self, tipo):
        self.saldo = 300
        self.tipo = tipo
        self.posicao_atual = 0

    def jogar_dado(self):
        return randint(1, 6)

    def calcular_posicao_tabuleiro(self):
        dado = self.jogar_dado()
        if self.posicao_atual + dado > 20:
            self.posicao_atual = self.posicao_atual + dado - 20
            self.saldo += 100
        else:
            self.posicao_atual += dado
        return self.posicao_atual

    def validar_rodada(self, propriedade):
        proprietario = propriedade.proprietario
        if proprietario is not None:
            self.saldo -= propriedade.aluguel
            proprietario.saldo += propriedade.aluguel
        else:
            self.comprar_ou_nao(propriedade)

    def comprar_ou_nao(self, propriedade):
        preco_venda = propriedade.venda
        if self.tipo == 'IMPULSIVO' or \
                self.tipo == 'EXIGENTE' and propriedade.aluguel > 50 or \
                self.tipo == 'CAUTELOSO' and self.saldo - preco_venda > 80:
            comprar = 1
        elif self.tipo == 'ALEATORIO':
            comprar = randint(0, 1)
        else:
            comprar = 0

        if comprar:
            if self.saldo - preco_venda >= 0:
                self.saldo -= preco_venda
                propriedade.colocar_proprietario(self)

    def liberar_propriedades(self, tabuleiro):
        for propriedade in tabuleiro:
            if propriedade.proprietario == self:
                propriedade.colocar_proprietario(None)

    @staticmethod
    def pegar_jogadores_simulacao():
        return [Jogador(tipo) for tipo in tipos]
