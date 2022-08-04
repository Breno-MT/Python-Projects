from flask import Blueprint, request, jsonify
import requests

from src.app.db import read, save
from src.app.utils import exists_key, exists_value
from src.app.models.technology import Technology, TechnologySchema, technology_share_schema
from src.app.db import db, ma


technology = Blueprint('technology', __name__, url_prefix='/technology')


@technology.route("/getAllTech", methods = ["GET"])
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


@technology.route("/deleteTech/<int:id>", methods = ["DELETE"])
def delete_tech(id):

    if not (tech := Technology.query.filter_by(id=id).first()):
        return jsonify({"message": f"O id {id} não foi encontrado ou não existe."}), 400

    db.session.delete(tech)
    db.session.commit()
    
    return {"message": f"Tecnologia deletada com sucesso."}, 200


@technology.route("/updateTech/<int:id>", methods = ["PUT"])
def update_tech(id):

    if not (tech_query := Technology.query.filter_by(id=id).first()):
        return jsonify({"message": f"A Tecnologia com id {id} não existe."}), 400
    

    list_keys = ['name']

    data = exists_key(request.get_json(), list_keys)

    if 'error' in data:
        return jsonify(data), 400

    tech_query.name = data['name']

    db.session.commit()

    return {"message": "Tecnologia atualizada com sucesso"}, 202

