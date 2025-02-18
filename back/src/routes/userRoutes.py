from flask import Blueprint, request, jsonify
from controllers.userController import create_user, get_users, get_user_id

user_bp = Blueprint('users', __name__)

@user_bp.route('/', methods=['POST'])
def register():
    data = request.get_json()
    if not data or 'name' not in data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Invalid data"}), 400
    return jsonify(create_user(data))
 
@user_bp.route('/', methods=['GET'])
def list_users():
    return jsonify(get_users())

@user_bp.route('/id',methods=['GET'])
def list_user_id(id):
    return jsonify(get_user_id(id))