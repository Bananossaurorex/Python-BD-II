import pytest
from ..models.usuario import Usuario


@pytest.fixture
def criar_usuario():
    return Usuario("Breno","brenosalvavidas@gmail.com","123")

def test_nome_valido(criar_usuario):
    assert criar_usuario.nome == "Breno"
