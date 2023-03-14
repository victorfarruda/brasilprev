from jogadores import Jogador
from propriedades import Propriedade


def test_pode_criar_propriedade():
    p = Propriedade()

    assert isinstance(p, Propriedade)


def test_propriedade_tem_atributos_necessarios():
    p = Propriedade()

    assert Propriedade.MIN <= p.aluguel <= Propriedade.MAX
    assert Propriedade.MIN <= (p.aluguel*Propriedade.TAXA_VENDA) <= (Propriedade.MAX*Propriedade.TAXA_VENDA)
    assert p.proprietario is None


def test_can_colocar_proprietario():
    p = Propriedade()
    j = Jogador('CAUTELOSO')
    p.colocar_proprietario(j)

    assert p.proprietario == j
