from flask import Flask
from routes.userRoutes import user_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Registrar o blueprint das rotas de usuário
app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    app.run(debug=True)