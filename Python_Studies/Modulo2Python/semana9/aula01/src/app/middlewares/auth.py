from functools import wraps
import json
from jwt import encode, decode
from flask import current_app, request, jsonify

from src.app.models.user import User

#permissions = ['DELETE', 'READ', 'WRITE', 'UPDATE']
#roles = ['OWNER', 'HELPER']

def requires_access_level(permission):
    def jwt_required(function_current):
        @wraps(function_current)
        def wrapper(*args, **kwargs):

            token = None

            if "Authorization" in request.headers:
                token = request.headers['Authorization']
            
            if not token:
                return jsonify({"error": "Você não possui permissão."}), 403
            
            if not "Bearer" in token:
                return jsonify({"error": "Você não possui permissão."}), 401
            
            try:
                token_pure = token_pure.replace("Bearer ", "")
                decoded = decode(token_pure, current_app.config['SECRET_KEY'], "HS256")
                current_user = User.query.get(decoded['user_id'])

            except:
                return jsonify({"error": "O Token é inválido."})
        
            found_permission = 0

            for role in current_user.roles:
                for permission_in_roles in role.permissions:
                    if permission_in_roles.description == permission:
                        found_permission = found_permission + 1

            if found_permission == 0:
                return jsonify({"error": "Você não tem permissão para esta funcionalidade"}), 403


            return function_current(*args, **kwargs)
        
        return wrapper

    return jwt_required