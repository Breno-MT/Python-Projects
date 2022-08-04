import requests

from flask import json
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# from src.app.models.user import User 
# from src.app.models.developer import Developer
# from src.app.models.technology import  Technology
# from src.app.models.developer_technologies import DeveloperTechnology 
# from src.app.models.city import City 
# from src.app.models.country import Country 
# from src.app.models.state import State 


db = SQLAlchemy()
ma = Marshmallow()

def read():
    try:
        with open ("src/app/db/technologies.json", "r") as openfile:
            json_object = json.load(openfile)
            return json_object

    except:
        return None


def save(data):
    json_object = json.dumps(data, indent=4)

    with open("src/app/db/technologies.json", "w") as outfile:
        outfile.write(json_object)
