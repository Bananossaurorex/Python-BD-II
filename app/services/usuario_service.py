from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self,repository: UsuarioRepository) -> None:
        self.repository = repository
    
    def criar_usuario(self):
        try:
            nome= input("Digite seu nome: ")
            email= input("Digte seu email: ")
            senha= input ("Digite sua senha: ")

            usuario = Usuario(nome=nome,email=email,senha=senha)
            consulta_usuario = self.repository.pesquisar_usuario(usuario.email)
            if consulta_usuario:
                print("Usuário já existe no banco de dados.")
                return
            
            self.repository.salvar_usuario(usuario)
            print("Usuário salvo com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print (f"ocorreu um erro inesperado: {erro}")

    def deletar_usuario(self):
        try:
            email_deletar = input("Digite o email que vc deseja deletar: ")
            usuario = self.repository.pesquisar_usuario(email = email_deletar)
            if usuario:
                self.repository.excluir_usuario(usuario)
                print("Usuario deletado com sucesso!")

                return
            
            print("Usuário não encontrado")
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print (f"ocorreu um erro inesperado: {erro}")
            
    def modificar_usuario(self):
        try:
            email_alterar = input("Digite o email que vc deseja alterar: ")
            usuario = self.repository.pesquisar_usuario(email = email_alterar)
            if usuario:
                usuario.nome = input("Digite seu nome: ")
                usuario.email= input("Digte seu email: ")
                usuario.senha= input ("Digite sua senha: ")
                
                self.repository.atualizar_usuario(usuario)
                print("Usuario alterado com sucesso!")
                return
            
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print (f"ocorreu um erro inesperado: {erro}")
    
    def pesquisar_id(self):
        try:
            id_pesquisar = input("Digite o id que você deseja pesquisar: ")
            usuario = self.repository.pesquisar_usuario_id(id_pesquisar)
            if usuario:
                print(f"{usuario.id} - {usuario.nome} - {usuario.email} - {usuario.senha}")
                return
            print("Usuario não encontrado!")
        
        except TypeError as erro:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print (f"ocorreu um erro inesperado: {erro}")

    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()