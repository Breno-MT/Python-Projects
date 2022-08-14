import os
import requests

from flask import Blueprint, request, jsonify
from flask.globals import session
from sqlalchemy.sql.expression import func

from google import auth
from google.oauth2 import id_token
from google_auth_oauthlib.flow import Flow
from werkzeug.utils import redirect

from src.app.utils import exists_key, exists_value, generate_jwt
from src.app.services.user_services import create_user, login_user, get_user_email
from src.app.middlewares.auth import requires_access_level
from src.app.models.user import User, user_developers_share_schema, user_developer_share_schema, users_share_schema
from src.app.models.developer import Developer
from src.app.models.technology import Technology

user = Blueprint('user', __name__, url_prefix='/user')

flow = Flow.from_client_secrets_file(
    client_secrets_file="src/app/db/client_secret.json",
    scopes=[
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "openid"
    ],
    redirect_uri = "http://localhost:5000/user/callback"
)

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

@user.route("/", methods = ['GET'])
@requires_access_level("READ")
def list_users():

    list_users = User.query.all()

    list_users_dict = user_developers_share_schema.dump(list_users)
  
    return jsonify(list_users_dict), 200

@user.route("/<int:id>", methods = ['GET'])
@requires_access_level("READ")
def list_user_by_id(id):

    list_users = User.query.filter_by(id=id).first()

    list_users_dict = user_developer_share_schema.dump(list_users)
  
    return jsonify(list_users_dict), 200

@user.route('/create', methods = ['POST'])
@requires_access_level("WRITE")
def create_users():
    
    list_keys = ['city_id', 'name', 'age', 'email', 'password']

    data = exists_key(request.get_json(), list_keys)

    if "@" not in data['email']:
        return jsonify({"error": "Email inválido!"}), 422

    if len(data['password']) <= 8:
        return jsonify({"error": "Senha deve ser maior que 8 caracteres!"}), 401

    response = create_user(
        data["city_id"],
        data["name"],
        data["age"], 
        data["email"], 
        data["password"], 
        data["roles"]
    )

    users = User.query.filter_by(name=data['name'])
    users_dict = users_share_schema.dump(users)

    for index, user_object in enumerate(users_dict):
        if index % 2 == 0: # if para verificar se o index é par
            techs = Technology.query.order_by(func.random()).limit(10).all() # query que retorna aleatóriamente 10 tecnologias
            Developer.seed(
                None,
                index % 2 == 0,
                user_object['id'],
                techs
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

@user.route('/auth/google', methods = ['POST'])
def auth_google():

    authorization_url, state = flow.authorization_url()

    return {"url": authorization_url}

@user.route('/callback', methods = ['GET'])
def callback():

    flow.fetch_token(authorization_response = request.url)
    credentials = flow.credentials
    request_session = requests.session()
    token_google = auth.transport.requests.Request(session=request_session)

    user_google_dict = id_token.verify_oauth2_token(
        id_token = credentials.id_token,
        request= token_google,
        audience= "140957057308-lqbhhmto7jpfr3mpc7a0rq9halkkqqqo.apps.googleusercontent.com"
    )

    user = {}
    user = get_user_email(user_google_dict['email'])

    if "error" in user:
        
        user = create_user(
            50,
            user_google_dict['name'],
            25,
            user_google_dict['email'],
            "PASSWORD_DEFAULT",
            None
        )

    user_google_dict['user_id'] = user['id']
    user_google_dict['roles'] = user['roles']

    del user_google_dict['aud']
    del user_google_dict['azp']

    token = generate_jwt(user_google_dict)

    return redirect(f"http://localhost:3000/?jwt={token}")

