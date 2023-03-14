from unittest.mock import Mock

from jogador import Jogador
from main import Main


def test_calcular_resultado_final():
    main = Main()
    main.comportamento = Mock()
    main.comportamento.items = Mock(return_value={"IMPULSIVO":300}.items())
    main.comportamento.get = Mock(return_value=300)

    main.calcular_resultado_final()

    main.comportamento.get.assert_called()
    main.comportamento.items.assert_called()


def test_calcular_ganhador_timeout():
    main = Main()
    jogadores = Jogador.pegar_jogadores_simulacao()

    main.calcular_ganhador_timeout(jogadores)

    assert main.timeout == 1
    assert main.comportamento[jogadores[-1].tipo] == 1
    assert main.turnos == [1000]


def test_jogar_rodada():
    main = Main()
    j1 = Mock()
    j1.calcular_posicao_tabuleiro = Mock(return_value=5)

    main.jogar_rodada(j1)

    j1.calcular_posicao_tabuleiro.assert_called_once()
    j1.validar_rodada.assert_called_once()


def test_jogador_perdeu():
    main = Main()
    jogadores = Jogador.pegar_jogadores_simulacao()
    j1 = jogadores[0]
    j1.saldo = -250

    main.jogador_perdeu(jogadores, j1)

    assert jogadores.count(j1) == 0


def test_finalizar_rodada():
    main = Main()
    jogadores = Jogador.pegar_jogadores_simulacao()
    rodada = 50

    main.finalizar_rodada(jogadores, rodada)

    assert main.turnos == [rodada + 1]
    assert main.comportamento[jogadores[0].tipo] == 1


def test_jogar_rodada_jogadores():
    main = Main()
    jogadores = Jogador.pegar_jogadores_simulacao()
    main.jogar_rodada = Mock()

    main.jogar_rodada_jogadores(jogadores)

    main.jogar_rodada.assert_called()


def test_jogar_rodada_jogadores_jogador_perdeu():
    main = Main()
    jogadores = Jogador.pegar_jogadores_simulacao()
    main.jogador_perdeu = Mock()
    j1 = jogadores[0]
    j1.saldo = -500

    main.jogar_rodada_jogadores(jogadores)

    main.jogador_perdeu.assert_called_with(jogadores, jogadores[0])


def test_main():
    main = Main()
    main.calcular_resultado_final = Mock()

    main.main()

    main.calcular_resultado_final.assert_called_once()


