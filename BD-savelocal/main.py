from sqlalchemy import create_engine, Column, String, Integer, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import sys
db=create_engine("sqlite:///meubanco.db")
Session = sessionmaker(bind=db)
session=Session()

Base = declarative_base()

#Tabelas iniciais

class Usuario(Base):
    __tablename__ = "usuarios" #Da nome a sua tabela
    id = Column("id", Integer, primary_key= True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self,nome,email,senha):
        self.nome= nome
        self.email= email
        self.senha= senha

class Livro(Base):
    __tablename__ = "livros" #Da nome a sua tabela
    id = Column(Integer,primary_key= True, autoincrement=True)
    titulo = Column(String)
    paginas = Column(Integer)
    dono = Column("dono",ForeignKey("usuarios.id"))
    
    def __init__(self,titulo,paginas,dono):
        self.titulo= titulo
        self.paginas= paginas
        self.dono = dono

Base.metadata.create_all(bind=db) #Cria todas as tabelas e outras informações

class UsuarioRepository:
    def __init__(self,session: sessionmaker) -> None:
        self.session = session
    
    def salvar_usuario(self,usuario: Usuario):
        try:
            self.session.add(usuario)
            self.session.commit()
            print("Usuário salvo com sucesso!")
        except Exception as erro:
            print(f"Erro ao salvar usuario:{erro}")
    def pesquisar_usuario(self, nome:str):
        return self.session.query(Usuario).filter_by(nome = nome).first()


class UsuarioService:
    def __init__(self,repository: UsuarioRepository) -> None:
        self.repository = repository

    def criar_usuario(self):
        try:
            nome=  input("Digite seu nome: ")
            email= input("Digte seu email: ")
            senha= input ("Digite sua senha: ")

            usuario = Usuario(nome=nome,email=email,senha=senha)
            
            consulta_usuario = self.repository.pesquisar_usuario(usuario.nome)
            if consulta_usuario:
                print("Usuário já existe no banco de dados.")
                return
            
            self.repository.salvar_usuario(usuario)
        except Exception as erro:
            print(f"Erro inesperado: {erro}")
def main():
    def limpartela():
        return os.system("cls || clear")
    
    session = Session()
    
    service.criar_usuario()


if __name__ == "__main__":
    main()

 
