from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))
    passwd = db.Column(db.String(10))

    def __init__(self, name, email, __passwd):
        self.name = name
        self.email = email
        self.passwd = __passwd