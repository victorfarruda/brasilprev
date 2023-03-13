import random

from jogadores import Jogador
from propriedades import tabuleiro


def calcular_resultado_final(timeout, turnos, comportamento):
    print('TIMEOUT', timeout)
    print('MÉDIA DE TURNOS', sum(turnos)/300)

    print(f'COMPORTAMENTOS IMPULSIVO: {comportamento.get("IMPULSIVO")/300}', )
    print(f'COMPORTAMENTOS EXIGENTE: {comportamento.get("EXIGENTE")/300}', )
    print(f'COMPORTAMENTOS CAUTELOSO: {comportamento.get("CAUTELOSO")/300}', )
    print(f'COMPORTAMENTOS ALEATORIO: {comportamento.get("ALEATORIO")/300}', )

    comp, quant = None, 0
    for i, j in comportamento.items():
        if j/300 > quant:
            quant = j/300
            comp = i

    print(f'COMPORTAMENTOS MAIS VENCE: {comp}', )


def calcular_ganhador(jogadores, comportamento, timeout, turnos):
    timeout = timeout + 1
    melhor = 0
    jogador = None
    for j in jogadores:
        if j.saldo > melhor:
            jogador = j

    comportamento[jogador.tipo] = comportamento[jogador.tipo] + 1
    turnos.append(999 + 1)
    return timeout


def jogar_rodada(j):
    vez = j.calcula_posicao_tabuleiro()
    propriedade = tabuleiro[vez - 1]
    j.valida_rodada(propriedade)


def jogador_perdeu(jogadores, j):
    j.libera_propriedades(tabuleiro)
    jogadores.remove(j)


def finaliza_rodada(comportamento, jogadores,turnos, rodada):
    comportamento[jogadores[0].tipo] = comportamento[jogadores[0].tipo] + 1
    turnos.append(rodada + 1)
    return rodada


def main():
    turnos = []
    timeout = 0
    comportamento = {'IMPULSIVO': 0, 'EXIGENTE': 0, 'CAUTELOSO': 0, 'ALEATORIO': 0}
    for simulacao in range(300):
        jogadores = Jogador.get_jogadores_simulacao()
        for rodada in range(1000):
            jogadores = random.choices(jogadores, k=len(jogadores))
            if len(jogadores) == 1:
                finaliza_rodada(comportamento, jogadores, turnos, rodada)
                break

            for j in jogadores:
                if j.saldo > 0:
                    jogar_rodada(j)
                else:
                    jogador_perdeu(jogadores, j)

        if len(jogadores) > 1:
            timeout = calcular_ganhador(jogadores, comportamento, timeout, turnos)
    calcular_resultado_final(timeout, turnos, comportamento)


if __name__ == '__main__':
    main()
