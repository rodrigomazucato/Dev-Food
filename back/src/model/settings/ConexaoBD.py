from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from back.src.model.settings.Base import Base

class ConexaoBD:
    def __init__(self):
        self.__string_conexao = "sqlite:///back/database/devfood.db"
        self.__motor_conexao = self.__criar_conexao()
        self.sessao = None
        # Base.metadata.create_all(self.__motor_conexao) # Para criar as tabelas

    def __criar_conexao(self):
        return create_engine(self.__string_conexao)

    def __enter__(self):
        GeradorSessao = sessionmaker(bind=self.__motor_conexao)
        self.sessao = GeradorSessao()
        return self
    
    def __exit__(self, *_):
        self.sessao.close()
