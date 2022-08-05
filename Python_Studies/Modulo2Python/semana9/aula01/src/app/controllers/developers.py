from flask import Blueprint, jsonify

from src.app.services.developer_services import list_all_developers_services

developers = Blueprint('developers', __name__, url_prefix='/developers')

@developers.route("/", methods = ["GET"])
def list_all_developers():
    list_devs = list_all_developers_services()

    return jsonify(list_devs)
