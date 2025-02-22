from flask import Flask
from flask_cors import CORS
from src.controllers.usuario import usuario_bp

app = Flask(__name__)
app.register_blueprint(usuario_bp, url_prefix='/user')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devfood.db'
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)