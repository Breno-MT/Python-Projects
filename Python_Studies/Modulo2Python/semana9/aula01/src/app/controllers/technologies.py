from flask import Blueprint, request, jsonify

from src.app.db import read, save
from src.app.utils import exists_key, exists_value

technology = Blueprint('technology', __name__, url_prefix='/technology')

# lista_json = {"data": ["JavaScript", "Python", "C++"]}


@technology.route("/", methods = ["GET"])
def list_all_technologies(): 

    techs = read()
    return jsonify(techs), 200


@technology.route("/", methods = ["POST"])
def add_new_technologies(): 

    list_keys = ['id', 'tech']

    data = exists_key(request.get_json(), list_keys)
    
    # insere na chave data, apartir da chave data passada ( esse data['data'] vem do POST que é enviado. )
    # lista_json["data"].append(data['data'])

    if 'error' in data:
        return jsonify(data), 400
    
    techs = read()

    if techs == None or len(techs) == 0:
        save([data])
        return jsonify(data), 201
    
    if exists_value(data, techs):
        return jsonify({"error": f"Algum item enviado já existe!"}), 400

    techs.append(data)
    save(techs)
    
    return jsonify(techs), 201

@technology.route("/<int:id>", methods = ["DELETE"])
def delete_technologies(id):

    techs = read()

    if techs == None or len(techs) == 0:
        return {"error": f"Não é possível excluir, pois não existem dados"}, 400

    only_technology_existents = []

    for data in techs:
        if data['id'] == id:
            index = techs.index(data)
            techs.pop(index)
            save(techs)
    
            return jsonify({"message": "Item deletado com sucesso!"}), 200

    return jsonify({"error": f"Não existe o id {id}"})

