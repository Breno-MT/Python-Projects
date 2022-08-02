import json
from flask import Blueprint, request, jsonify

from src.app.db import read, save
from src.app.utils import exists_key, exists_value
from src.app.models.technology import Technology, TechnologySchema, technology_share_schema
from src.app.db import db, ma


technology = Blueprint('technology', __name__, url_prefix='/technology')


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


# @technology.route("/<int:id>", methods = ["DELETE"])
# def delete_technologies(id):

#     techs = read()

#     if techs == None or len(techs) == 0:
#         return {"error": f"Não é possível excluir, pois não existem dados"}, 400

#     only_technology_existents = []

#     for data in techs:
#         if data['id'] == id:
#             index = techs.index(data)
#             techs.pop(index)
#             save(techs)
    
#             return jsonify({"message": "Item deletado com sucesso!"}), 200

#     return jsonify({"error": f"Não existe o id {id}"})


@technology.route("/getAllTechinDb", methods = ["GET"])
def get_all_techs():

    if len(Technology.query.all()) == 0:
        return jsonify({"message": "Não tem nenhuma tecnologia salva."}), 200

    return jsonify(technology_share_schema.dump(Technology.query.all())), 200


@technology.route("/createNewTech", methods = ["POST"])
def create_new_tech():
    list_keys = ['name']

    data = exists_key(request.get_json(), list_keys)  

    if 'error' in data:
        return jsonify(data), 400

    tech = Technology(
        name=data['name']
    )

    db.session.add(tech)
    db.session.commit()

    return {"message": "Tecnologia salva com sucesso"}, 202

@technology.route("/deleteTech", methods = ["DELETE"])
def delete_tech():
    
    pass

