from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class ConexaoBD:
    def __init__(self):
        self.__string_conexao = ""
        self.__motor_conexao = self.__criar_conexao()
        self.sessao = None

    def __criar_conexao(self):
        return create_engine(self.__string_conexao)
    
    def __enter__(self):
        GeradorSessao = sessionmaker(bind=self.__motor_conexao)
        self.sessao = GeradorSessao()
        return self
    
    def __exit__(self):
        self.sessao.close()
