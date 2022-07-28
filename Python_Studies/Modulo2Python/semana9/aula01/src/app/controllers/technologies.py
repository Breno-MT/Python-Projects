from flask import Blueprint, request, jsonify

technology = Blueprint('technology', __name__, url_prefix='/technology')

lista_json = {"data": ["JavaScript", "Python", "C++"]}


@technology.route("/", methods = ["GET"])
def list_all_technologies(): return lista_json

@technology.route("/", methods = ["POST"])
def add_new_technologies(): 
    
    data = request.get_json()
    print(data)
    
    lista_json["data"].append(data['data'])

    return lista_json
