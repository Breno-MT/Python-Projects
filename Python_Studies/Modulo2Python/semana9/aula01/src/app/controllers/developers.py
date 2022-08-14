from flask import Blueprint, jsonify
from app.models.developer import Developer, developer_share_schema
from src.app.models.technology import Technology, technologies_share_schema, technology_share_schema, developers_techs_share_schema, developer_techs_share_schema
from src.app.models.user import User

from src.app.services.developer_services import list_all_developers_services
from src.app.middlewares.auth import requires_access_level



developers = Blueprint('developers', __name__, url_prefix='/developers')

@developers.route("/", methods = ["GET"])
@requires_access_level("READ")
def list_all_developers():
    list_devs = list_all_developers_services()

    return jsonify(list_devs)

@developers.route("/<int:id>", methods = ["GET"])
# @requires_access_level("READ")
def list_by_id(id):

    list_dev = Developer.query.filter_by(user_id=id).first()

    list_dev_dict = developer_share_schema.dump(list_dev)

    if list_dev_dict == {}:
        return jsonify({"error": "Dev não encontrado!"}), 404

    return jsonify(list_dev_dict), 200

@developers.route("/techs/<int:id_tech>", methods = ["GET"])
# @requires_access_level("READ")
def list_by_tech_id(id_tech):
    
    list_tech = Technology.query.filter_by(id=id_tech).first() # pega tech por id

    list_tech_id_dict = developer_techs_share_schema.dump(list_tech)

    return jsonify(list_tech_id_dict), 200
    

    

