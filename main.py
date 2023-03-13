from jogadores import Jogador, tipos
from propriedades import tabuleiro


def main():
    turnos = []
    timeout = 0
    comportamento = {'IMPULSIVO': 0, 'EXIGENTE': 0, 'CAUTELOSO': 0, 'ALEATORIO': 0}
    for rodada in range(300):
        jogadores = [Jogador(tipo) for tipo in tipos]
        for i in range(1000):
            if len(jogadores) == 1:
                # print('GANHADOR', rodada, jogadores[0].tipo)
                comportamento[jogadores[0].tipo] = comportamento[jogadores[0].tipo] +1
                turnos.append(i + 1)
                break

            for j in jogadores:
                if j.saldo > 0:
                    vez = j.calcula_posicao_tabuleiro()
                    propriedade = tabuleiro[vez-1]
                    j.valida_rodada(propriedade)
                else:
                    j.libera_propriedades(tabuleiro)
                    jogadores.remove(j)
        if len(jogadores) > 1:
            timeout = timeout + 1
            melhor = 0
            jogador = None
            for j in jogadores:
                if j.saldo > melhor:
                    jogador = j
            # print('TIMEOUT', rodada, jogador.tipo)
            comportamento[jogador.tipo] = comportamento[jogador.tipo] + 1
            turnos.append(999 + 1)

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


if __name__ == '__main__':
    main()
