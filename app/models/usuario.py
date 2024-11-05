from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from ..config.connection import db

Base = declarative_base()



class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer,primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150), unique=True)
    senha = Column(String(150))

    def __init__(self, nome: str, email:str, senha:str):
        self.nome = self._nome_vazio(nome)
        self.email = email    
        self.senha = senha
        
#      -- Funções de teste --

    def _nome_vazio(self,nome):
        if not nome.strip():
            raise TypeError("O nome não pode ser vazio")
        return nome

# Criando tabela no banco de dados
Base.metadata.create_all(bind=db)

