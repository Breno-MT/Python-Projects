from datetime import datetime, timedelta
from jwt import encode
from flask import Blueprint, request, jsonify, current_app

from src.app.models.user import User, user_share_schema
from src.app.db import read, save
from src.app.utils import exists_key, exists_value
from src.app.services.user_services import create_user

user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/create', methods = ['POST'])
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

    user_query = User.query.filter_by(email = data['email']).first_or_404()

    user_dict = user_share_schema.dump(user_query)

    if not user_query.check_password(data['password']):
        return jsonify({
            "error": "Suas credênciais estão incorretas!"
        }), 403
    
    payload = {
        "user_id": user_query.id,
        "exp": datetime.utcnow() + timedelta(days=1),
        "roles": user_dict['roles']
    }

    token = encode(payload, current_app.config["SECRET_KEY"], "HS256")

    return jsonify({"token": token})


