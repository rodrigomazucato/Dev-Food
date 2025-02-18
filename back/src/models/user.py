from werkzeug.security import generate_password_hash, check_password_hash
class User:
   def __init__(self, id, name, email, password):
      self.id = id
      self.name = name
      self.email = email
      self._password = generate_password_hash(password)

   def check_password(self, password):
        return check_password_hash(self._password, password)

users = []