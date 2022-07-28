from flask import Blueprint

developers = Blueprint('developers', __name__, url_prefix='/developers')

@developers.route("/", methods = ["GET"])
def list_all_developers(): return {"Devs": ["Breno", "Maycon", "Pedro"]}
