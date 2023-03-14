import random

from jogadores import Jogador
from propriedades import tabuleiro


class Main:
    def __init__(self):
        self.turnos = []
        self.timeout = 0
        self.comportamento = {'IMPULSIVO': 0, 'EXIGENTE': 0, 'CAUTELOSO': 0, 'ALEATORIO': 0}

    def calcular_resultado_final(self):
        comportamento_mais_vence, quant = None, 0
        for i, j in self.comportamento.items():
            if j / 300 > quant:
                quant = j / 300
                comportamento_mais_vence = i

        print(f'QUANTIDADE DE TIMEOUT: {self.timeout}')
        print(f'MÉDIA DE TURNOS: {sum(self.turnos) / 300}')
        print(f'COMPORTAMENTO IMPULSIVO: {self.comportamento.get("IMPULSIVO") / 300}', )
        print(f'COMPORTAMENTO EXIGENTE: {self.comportamento.get("EXIGENTE") / 300}', )
        print(f'COMPORTAMENTO CAUTELOSO: {self.comportamento.get("CAUTELOSO") / 300}', )
        print(f'COMPORTAMENTO ALEATORIO: {self.comportamento.get("ALEATORIO") / 300}', )
        print(f'COMPORTAMENTO QUE MAIS VENCE: {comportamento_mais_vence}')

    def calcular_ganhador_timeout(self, jogadores):
        if len(jogadores) > 1:
            self.timeout = self.timeout + 1
            melhor = 0
            jogador = None
            for j in jogadores:
                if j.saldo > melhor:
                    jogador = j

            self.comportamento[jogador.tipo] = self.comportamento[jogador.tipo] + 1
            self.turnos.append(999 + 1)

    def jogar_rodada(self, j):
        vez = j.calcular_posicao_tabuleiro()
        propriedade = tabuleiro[vez - 1]
        j.validar_rodada(propriedade)

    def jogador_perdeu(self, jogadores, j):
        j.liberar_propriedades(tabuleiro)
        jogadores.remove(j)

    def finalizar_rodada(self, jogadores, rodada):
        self.comportamento[jogadores[0].tipo] = self.comportamento[jogadores[0].tipo] + 1
        self.turnos.append(rodada + 1)

    def jogar_rodada_jogadores(self, jogadores):
        for j in jogadores:
            if j.saldo > 0:
                self.jogar_rodada(j)
            else:
                self.jogador_perdeu(jogadores, j)

    def main(self):
        for simulacao in range(300):
            jogadores = Jogador.pegar_jogadores_simulacao()

            for rodada in range(1000):
                quantidade_jogadores = len(jogadores)
                jogadores = random.choices(jogadores, k=quantidade_jogadores)
                if quantidade_jogadores == 1:
                    self.finalizar_rodada(jogadores, rodada)
                    break

                self.jogar_rodada_jogadores(jogadores)

            self.calcular_ganhador_timeout(jogadores)
        self.calcular_resultado_final()


if __name__ == '__main__':
    main = Main()
    main.main()
