import pytest
from app.models.usuario import Usuario



@pytest.fixture
def criar_usuario():
    return Usuario("Breno","brenosalvavidas@gmail.com","123")

def test_nome_valido(criar_usuario):
    assert criar_usuario.nome == "Breno"


def test_nome_vazio_invalido():
        with pytest.raises(ValueError, match = "O nome não pode ser vazio"):
            Usuario("","brenosalvavidas@gmail.com","123")

def test_nome_apenas_letras():
      with pytest.raises(TypeError, match = "Digite apenas letras"):
            Usuario(12323432,"brenosalvavidas@gmail.com","123")

def test_email_vazio_invalido():
        with pytest.raises(TypeError, match = "O email não pode ser vazio"):
            Usuario("Breno","","123")

def test_senha_vazio_invalido():
        with pytest.raises(TypeError, match = "A senha não pode estar vazia"):
            Usuario("Breno","brenosalvavidas@gmail.com","")

def test_senha_muito_grande():
      with pytest.raises(TypeError, match= "A senha só pode possuir até 10 caracteres"):
            Usuario("Breno","brenosalvavidas@gmail.com","1234567891011")
