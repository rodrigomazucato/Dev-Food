from back.src.model.repositories import RepositoryUsuario
from flask import Blueprint, request

usuario_bp = Blueprint('usuario', __name__)

@usuario_bp.get("/hi")
def teste():
    return "Hi Lorena"

@usuario_bp.post("/users")
def create_user():
    nome = request.json_get('nome')
    email = request.json_get('email')
    senha = request.json_get('senha')

    db_user = RepositoryUsuario()
    db_user.inserir(nome, email, senha)

    # user_exists = db.session.get(Usuario, id)
    # if not user_exists:
    #     user = Usuario(name, email, passwd)
    #     db.session.add(user)
    #     db.session.flush()
    #     db.session.commit()
    #     return 'Created', 201
    # else:
    #     user = user_exists
    #     return 'Bad request', 404

# def get_users():
#     print('chegou aqui')
#     users = [{"id": u.id, "name": u.name, "email": u.email}
#              for u in Usuario.query.with_entities(Usuario.id, Usuario.name, Usuario.email).all()]
#     return users, 200

# def get_user_by_id(id):
#     user_filtered = Usuario.query.get(id)
#     return user_filtered, 200