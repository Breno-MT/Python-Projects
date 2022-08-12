from flask import Blueprint, jsonify

from src.app.middlewares.auth import requires_access_level
from src.app.models.city import City, city_share_schema, cities_share_schema



cities = Blueprint('cities', __name__, url_prefix='/cities')

@cities.route("/", methods = ["GET"])
# @requires_access_level("READ")
def list_all():

    cities = City.query.all()
    city_dict = cities_share_schema.dump(cities)

    id_total = City.query.paginate()

    for _ in city_dict:
        return jsonify({"cities_all": city_dict, "page_total": id_total.total}), 200


@cities.route("/<int:id>", methods = ["GET"])
# @requires_access_level("READ")
def list_city_id(id):

    cities = City.query.filter_by(id=id).first()
    city_dict = city_share_schema.dump(cities)

    if id > 5570:
        return jsonify({"error": "Página não existe!"}), 404

    return city_dict, 200

