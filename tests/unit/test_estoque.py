import pytest
from src.estoque import Estoque, ErroEstoque

# Uma instância de Estoque é necessária para acessar o método _validar_quantidade
@pytest.fixture
def estoque():
    return Estoque()

# Cenário 1: Testes do método interno _validar_quantidade
def test_validar_quantidade_valida(estoque):
    """Caso de Teste 1: Caminho Feliz/Valor Válido (inteiro positivo)."""
    assert estoque._validar_quantidade(10) is True

def test_validar_quantidade_invalida_zero(estoque):
    """Caso de Teste 2: Valor Inválido (zero). Deve levantar uma exceção."""
    with pytest.raises(ErroEstoque, match="A quantidade deve ser um número inteiro positivo."):
        estoque._validar_quantidade(0)

def test_validar_quantidade_invalida_negativa(estoque):
    """Caso de Teste 3: Valor Inválido (negativo)."""
    with pytest.raises(ErroEstoque):
        estoque._validar_quantidade(-5)

def test_validar_quantidade_invalida_string(estoque):
    """Caso de Teste 4 (Extra): Valor Inválido (tipo de dado errado)."""
    with pytest.raises(ErroEstoque):
        estoque._validar_quantidade("dez")

def test_validar_quantidade_extrema(estoque):
    """Caso de Teste 5 (Extra): Valor Extremo (número muito grande)."""
    # Embora o sistema real possa ter limites de memória, a validação lógica deve passar.
    assert estoque._validar_quantidade(999999999) is True