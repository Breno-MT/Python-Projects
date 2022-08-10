from flask import Blueprint, jsonify

from src.app.services.developer_services import list_all_developers_services
from src.app.middlewares.auth import requires_access_level

developers = Blueprint('developers', __name__, url_prefix='/developers')

@developers.route("/", methods = ["GET"])
@requires_access_level("READ")
def list_all_developers():
    list_devs = list_all_developers_services()

    return jsonify(list_devs)

@developers.route("/create", methods = ["POST"])
@requires_access_level("WRITE")
def create_developer():
    pass
