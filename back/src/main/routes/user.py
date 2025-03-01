from flask import Blueprint, jsonify, request
import json

user_route_bp = Blueprint('user_route', __name__)

from src.validators.users_creator_validator import users_creator_validator

from src.http_types.http_request import HttpRequest

from src.controllers.users.users_creator import UsersCreator
from src.controllers.users.users_reader import UsersReader
from src.model.repositories.users_repository import UsersRepository

@user_route_bp.route('/user', methods=['POST'])
def create_new_user():
    users_creator_validator(request)
    http_request = HttpRequest(body=request.json)

    users_repo = UsersRepository()
    users_creator = UsersCreator(users_repo)

    http_response = users_creator.create_user(http_request)

    return jsonify(http_response.body), http_response.status_code

@user_route_bp.route('/user', methods=['GET'])
def get_all_users():
    users_repo = UsersRepository()
    users_reader = UsersReader(users_repo)

    http_request = HttpRequest(params=request.args.to_dict())

    http_response = users_reader.get_all_users(http_request)

    return jsonify(http_response.body), http_response.status_code