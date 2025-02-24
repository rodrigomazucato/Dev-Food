from abc import ABC, abstractmethod

class InterfaceUsuario(ABC):
    @abstractmethod
    def inserir(self, nome: str, email: str, senha: str, is_admin: bool) -> None:
        pass
