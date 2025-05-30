from app.models.usuario import Usuario
from sqlalchemy.orm import Session

class UsuarioRepository:
    def __init__(self,session: Session) -> None:
        self.session = session

    def salvar_usuario(self, usuario: Usuario):
        self.session.add(usuario)
        self.session.commit()
        self.session.refresh(usuario)
    
    def pesquisar_usuario(self, email:str):
        return self.session.query(Usuario).filter_by(email = email).first()
    
    def excluir_usuario(self, usuario: Usuario):
        self.session.delete(usuario)
        self.session.commit()

    def atualizar_usuario(self,usuario: Usuario):
        self.session.commit()
        self.session.refresh(usuario)

    def pesquisar_usuario_id(self,id:int):
        return self.session.query(Usuario).filter_by(id=id).first()

    def listar_todos_usuarios(self):
        return self.session.query(Usuario).all()
    