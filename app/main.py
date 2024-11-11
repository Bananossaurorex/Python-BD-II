import os
import sys
#Adiciona o diretrorio app como diretorio padrão
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from app.repositories.usuario_repository import UsuarioRepository
from app.services.usuario_service import UsuarioService
from app.config.connection import Session


def limpar_tela():
    return os.system("cls || clear")

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    while True:
        limpar_tela()
        print("\n1- Criar usuário")
        print("2- Deletar usuário")
        print("3- Modificar usuário")
        print("4- Pesquisar usuário")
        print("5- Listar usuário")
        opcao = int(input("Digite a opção: "))
    
        match(opcao):
            case 1:
                limpar_tela()
                service.criar_usuario()

            case 2 :
                limpar_tela()
                service.deletar_usuario()

            case 3:
                limpar_tela()
                service.modificar_usuario() 
            
            case 4:
                limpar_tela()
                service.pesquisar_id()

            case 5:
                limpar_tela()
                print("\nListando todos os usuários.")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
                service.listar_todos_usuarios()
            
            case 0:
                break
            
            case _:
                limpar_tela()
                print("Opção inválida")
    # Listando todos os usuários.

if __name__ == "__main__":
    main() # Chamando para a função.