from flask import Flask
from flask_cors import CORS
from back.src.model.repositories.RepUsuario import RepositoryUsuario
from src.controller.usuario import usuario_bp

app = Flask(__name__)
app.register_blueprint(usuario_bp, url_prefix='/user')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost/meu_banco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)