from flask import Blueprint
from controllers.userController import create_user, get_users, get_user_by_id

userBlueprint = Blueprint('blueprint', __name__)

userBlueprint.route('/', methods=['GET'])
userBlueprint.route('/users', methods=['GET'](get_users))
userBlueprint.route('/users/<id>', methods=['GET'](get_user_by_id))
userBlueprint.route('/users', methods=['POST'](create_user))




