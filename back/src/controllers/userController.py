from models.user import User, db
from flask import request
from app import app

@app.get('/')
def get_users():
    print('chegou aqui')
    users = [{"id": u.id, "name": u.name, "email": u.email}
             for u in User.query.with_entities(User.id, User.name, User.email).all()]
    return users, 200

def get_user_by_id(id):
    user_filtered = User.query.get(id)
    return user_filtered, 200

def create_user():
    name = request.json_get('name')
    email = request.json_get('email')
    passwd = request.json_get('passwd')

    user_exists = db.session.get(User, id)
    if not user_exists:
        user = User(name, email, passwd)
        db.session.add(user)
        db.session.flush()
        db.session.commit()
        return 'Created', 201
    else:
        user = user_exists
        return 'Bad request', 404
   

    