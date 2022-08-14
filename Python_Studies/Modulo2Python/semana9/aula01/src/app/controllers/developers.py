from flask import Blueprint, jsonify
from ..models.developer import Developer, developer_share_schema

from src.app.services.developer_services import list_all_developers_services
from src.app.middlewares.auth import requires_access_level

developers = Blueprint('developers', __name__, url_prefix='/developers')

@developers.route("/", methods = ["GET"])
@requires_access_level("READ")
def list_all_developers():
    list_devs = list_all_developers_services()

    return jsonify(list_devs)

@developers.route("/<int:id>", methods = ["GET"])
# @requires_access_level("WRITE")
def list_by_id(id):

    

    list_dev = Developer.query.filter_by(user_id=id).first()

    list_dev_dict = developer_share_schema.dump(list_dev)

    if list_dev_dict == {}:
        return jsonify({"error": "Dev não encontrado!"}), 404

    return jsonify(list_dev_dict), 200
