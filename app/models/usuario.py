from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.connection import db

Base = declarative_base()



class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer,primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True)
    senha = Column(String(150))

    def __init__(self, nome: str, email:str, senha:str):
        self.nome = self._nome_test(nome)
        self.email = self._email_test(email)    
        self.senha = self._senha_test(senha)
        
#      -- Funções de teste --

    def _nome_test(self,nome):
        if not isinstance (nome,str):
            raise TypeError ("Digite apenas letras")
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio")
        return nome
    
    def _email_test(self,nome):
        if not nome.strip():
            raise TypeError("O email não pode ser vazio")
        return nome
    
    def _senha_test(self,senha):
        if not senha.strip():
            raise TypeError("A senha não pode estar vazia")
        return senha

# Criando tabela no banco de dados
Base.metadata.create_all(bind=db)