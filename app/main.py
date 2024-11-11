from repositories.usuario_repository import UsuarioRepository
from services.usuario_service import UsuarioService
from config.connection import Session

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    opcao = int(input("Digite a opção: "))
    print("1- Criar usuario")
    print("2- Deletar usuario")
    print("3- Modificar usuario")
    match(opcao):
        case 1:
            service.criar_usuario()
        
        case 2 :
            service.deletar_usuario()
        
        case 3:
            service.modificar_usuario()
    
    # Listando todos os usuários.
    print("\nListando todos os usuários.")
    lista_usuarios = service.listar_todos_usuarios()
    for usuario in lista_usuarios:
        print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")


if __name__ == "__main__":
    main() # Chamando para a função.