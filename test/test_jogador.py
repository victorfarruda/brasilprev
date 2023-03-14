from unittest.mock import Mock

import pytest

from jogador import Jogador
from propriedade import Propriedade, tabuleiro


def test_jogar_dado():
    val_dado = Jogador.jogar_dado()

    assert val_dado in [1, 2, 3, 4, 5, 6]


@pytest.mark.parametrize(
    'posicao_atual, mock_value, expected, saldo',
    [
        (0, 5, 5, 300),
        (18, 4, 2, 400),
    ]
)
def test_calcular_posicao_tabuleiro(posicao_atual, mock_value, expected, saldo):
    j = Jogador('CAUTELOSO')
    j.posicao_atual = posicao_atual
    j.jogar_dado = Mock(return_value=mock_value)

    assert j.calcular_posicao_tabuleiro() == expected
    assert j.saldo == saldo


def test_validar_rodada_quando_nao_ha_proprietario():
    j = Jogador('CAUTELOSO')
    p = Propriedade()
    j.comprar_ou_nao = Mock()

    j.validar_rodada(p)

    j.comprar_ou_nao.assert_called_once()


def test_validar_rodada_quando_ha_proprietario():
    j1 = Jogador('CAUTELOSO')
    j2 = Jogador('EXIGENTE')
    p = Propriedade()
    p.proprietario = j2
    j1.comprar_ou_nao = Mock()

    j1.validar_rodada(p)

    assert j1.saldo == 300 - p.aluguel
    assert j2.saldo == 300 + p.aluguel


@pytest.mark.parametrize(
    'venda, aluguel, tipo',
    [
        (100, 10, 'IMPULSIVO'),
        (650, 65, 'EXIGENTE'),
        (150, 15, 'CAUTELOSO'),
    ]
)
def test_comprar_ou_nao_quando_compra(venda, aluguel, tipo):
    j = Jogador(tipo)
    p = Propriedade()
    p.venda = venda
    p.aluguel = aluguel
    j.comprar_propriedade = Mock()

    j.comprar_ou_nao(p)

    j.comprar_propriedade.assert_called_once()


@pytest.mark.parametrize(
    'venda, aluguel, tipo',
    [
        (450, 45, 'EXIGENTE'),
        (280, 28, 'CAUTELOSO'),
    ]
)
def test_comprar_ou_nao_quando_nao_compra(venda, aluguel, tipo):
    j = Jogador(tipo)
    p = Propriedade()
    p.venda = venda
    p.aluguel = aluguel
    j.comprar_propriedade = Mock()

    j.comprar_ou_nao(p)

    j.comprar_propriedade.assert_not_called()


def test_comprar_ou_nao_ALEATORIO():
    j = Jogador('ALEATORIO')
    p = Propriedade()
    j.comprar_propriedade = Mock()

    j.comprar_ou_nao(p)

    if j.comprar == 1:
        j.comprar_propriedade.assert_called_once()
    else:
        j.comprar_propriedade.assert_not_called()


def test_comprar_quanto_tem_saldo():
    j = Jogador('CAUTELOSO')
    p = Propriedade()
    p.venda = 150
    p.aluguel = 15

    j.comprar_propriedade(p, p.venda)

    assert j.saldo == 300 - p.venda
    assert p.proprietario == j


def test_comprar_quanto_nao_tem_saldo():
    j = Jogador('CAUTELOSO')
    p = Propriedade()
    p.venda = 350
    p.aluguel = 35

    j.comprar_propriedade(p, p.venda)

    assert j.saldo == 300
    assert p.proprietario is None


def test_liberar_propriedades():
    j = Jogador('CAUTELOSO')
    for t in tabuleiro:
        t.colocar_proprietario(j)

    for t in tabuleiro:
        assert t.proprietario is j

    j.liberar_propriedades(tabuleiro)

    for t in tabuleiro:
        assert t.proprietario is None


def test_pegar_jogadores_simulacao():
    jogadores = Jogador.pegar_jogadores_simulacao()

    assert len(jogadores) == 4
    for j in jogadores:
        assert isinstance(j, Jogador)

