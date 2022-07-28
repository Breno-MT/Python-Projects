import json
from flask import Blueprint, request, jsonify

from src.app.db import read, save
from src.app.utils import exists_key

technology = Blueprint('technology', __name__, url_prefix='/technology')

# lista_json = {"data": ["JavaScript", "Python", "C++"]}


@technology.route("/", methods = ["GET"])
def list_all_technologies(): return {"data": ["JavaScript", "Python"]}

@technology.route("/", methods = ["POST"])
def add_new_technologies(): 

    list_keys = ['id', 'tech']

    data = exists_key(request.get_json(), list_keys)
    
    # insere na chave data, apartir da chave data passada ( esse data['data'] vem do POST que é enviado. )
    # lista_json["data"].append(data['data'])

    try:
        if data['error']:
            return jsonify(data)
    
    except:
        return data
