from models.usuario import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:
    def __init__(self,repository: UsuarioRepository) -> None:
        self.repository = repository
    
    def criar_usuario(self):
        try:
            nome = input("Digite seu nome: ")
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
            email_deletar = input("Digite o email que vc deseja deletar")
            usuario = self.repository.pesquisar_usuario(email = email_deletar)
            if usuario:
                print("Usuario deletado com sucesso!")
                self.repository.excluir_usuario(Usuario)
                return
            print("Usuario não encontrado.")
        
        except self:
            print(f"Erro ao salvar usuário: {erro}")
        except Exception as erro:
            print (f"ocorreu um erro inesperado: {erro}")
    
    def listar_todos_usuarios(self):
        return self.repository.listar_todos_usuarios()