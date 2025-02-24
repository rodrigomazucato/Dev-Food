from back.src.model.classes import Usuario
from back.src.model.interfaces.IUsuario import InterfaceUsuario
from back.src.model.settings.ConexaoBD import ConexaoBD
from back.src.model.classes.Usuario import Usuario

class RepositoryUsuario(InterfaceUsuario):
    def inserir(self, nome: str, email: str, senha: str, is_admin: bool = False) -> None:
        with ConexaoBD() as db:
            try:
                novo_usuario = Usuario(nome=nome, email=email, senha=senha, is_admin=is_admin)  # outra forma: **locals()
                db.sessao.add(novo_usuario)
                db.sessao.commit()
            except Exception as e:
                db.sessao.rollback()
                raise Exception(f"Erro ao salvar usuário no banco de dados: {e}")
