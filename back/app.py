from flask import Flask
from flask_cors import CORS
from src.models.user import db
from src.models.user import userBlueprint

def create_app():

    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///devfood.db'
    db.init_app(app)
    CORS(app)

    app.register_blueprint(userBlueprint, url_prefix='user')
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)