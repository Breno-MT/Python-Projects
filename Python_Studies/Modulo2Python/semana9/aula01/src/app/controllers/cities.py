from flask import Blueprint

cities = Blueprint('cities', __name__, url_prefix='/cities')

@cities.route("/", methods = ["GET"])
def list_all_cities(): return {"Cities": ["Orlando, Florida", "Florianopolis, SC", "Porto Alegre, RS"]}
