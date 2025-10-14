from src.estoque import Estoque, ErroEstoque


def test_cenario_adicao_remocao():
    """Cenário funcional: adicionar e remover produtos no estoque (caminho feliz)."""
    est = Estoque()

    # início: vazio
    assert est.verificar_estoque('Caneta') == 0

    # adicionar
    msg = est.adicionar_produto('Caneta', 20)
    assert 'Adicionadas' in msg
    assert est.verificar_estoque('caneta') == 20

    # adicionar novamente
    est.adicionar_produto(' Caneta ', 5)
    assert est.verificar_estoque('caneta') == 25

    # remover parte
    msg = est.remover_produto('caneta', 10)
    assert 'Removidas' in msg
    assert est.verificar_estoque('Caneta') == 15

    # remover tudo
    est.remover_produto('caneta', 15)
    assert est.verificar_estoque('caneta') == 0


def test_cenario_erro_remover_produto_inexistente():
    """Cenário funcional: tentativa de remover produto não cadastrado (caminho alternativo)."""
    est = Estoque()
    msg = est.remover_produto('Lapis', 1)
    assert "não está cadastrado" in msg


def test_cenario_quantidade_invalida():
    """Cenário funcional: entradas inválidas para quantidade (valores inválidos)."""
    est = Estoque()
    # adicionar com quantidade zero
    msg = est.adicionar_produto('Borracha', 0)
    assert 'A quantidade deve ser' in msg

    # remover com quantidade negativa
    msg2 = est.remover_produto('Borracha', -3)
    assert 'A quantidade deve ser' in msg2
