from back.src.model.repositories.RepUsuario import RepositoryUsuario

def test_inserir_dados():
    dados = {
        "nome": "rodrigo",
        "email": "rodrigo2@gmail.com",
        "senha": "1234"
        }
    db_user = RepositoryUsuario()
    db_user.inserir(**dados)