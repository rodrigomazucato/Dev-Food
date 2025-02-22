from back.src.model.classes import Usuario
from src.model.configs import ConexaoBD
from src.model.classes.Usuario import Usuario

class InterfaceUsuario:
    def inserir(self, nome: str, email: str, senha: str, is_admin: bool = False) -> None:
        with ConexaoBD() as db:
            try:
                novo_usuario = Usuario(nome=nome, email=email, senha=senha, is_admin=is_admin)  # outra forma: **locals()
                db.session.add(novo_usuario)
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise Exception(f"Erro: {e}")
