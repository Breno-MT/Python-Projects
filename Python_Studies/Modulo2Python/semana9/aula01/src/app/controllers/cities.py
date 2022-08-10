from flask import Blueprint

from src.app.middlewares.auth import requires_access_level

cities = Blueprint('cities', __name__, url_prefix='/cities')

@cities.route("/", methods = ["GET"])
@requires_access_level("READ")
def list_all_cities(): return {"Cities": ["Orlando, Florida", "Florianopolis, SC", "Porto Alegre, RS"]}
