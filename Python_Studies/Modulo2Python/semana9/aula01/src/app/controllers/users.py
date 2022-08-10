from flask import Blueprint, request, jsonify

from src.app.utils import exists_key, exists_value
from src.app.services.user_services import create_user, login_user
from src.app.middlewares.auth import requires_access_level

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/create', methods = ['POST'])
@requires_access_level("CREATE")
def create_users():
    list_keys = ['city_id', 'name', 'age', 'email', 'password']

    data = exists_key(request.get_json(), list_keys)

    response = create_user(
        data["city_id"],
        data["name"],
        data["age"], 
        data["email"], 
        data["password"], 
        data["roles"]
    )

    if "error" in response:
        return jsonify(response), 400

    return jsonify(response), 201

@user.route('/login', methods = ['POST'])
def login():
    list_keys = ['email', 'password']

    data = exists_key(request.get_json(), list_keys)

    response = login_user(data['email'], data ['password'])

    if "error" in response:
        return jsonify(response['error']), response['status_code']
    
    return jsonify(response), 200


