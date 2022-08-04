import requests

from src.app.models.country import Country


def exists_key(request_json, list_keys):

    keys_not_found_in_request = []

    for key in list_keys:
        if key in request_json:
            continue
        
        else:
            keys_not_found_in_request.append(key)

    if len(keys_not_found_in_request) == 0:    
        return request_json
    
    return {"error": f"Está faltando o item {keys_not_found_in_request}"}

def exists_value(request_json, data_already_in_db):

    for json in data_already_in_db:
        if json['id'] == request_json['id'] or json['tech'] == request_json['tech']:
            return json
    
    return False

def populate_db():

    data_request = requests.get("https://randomuser.me/api/?nat=br&results=100")
    techs = requests.get("https://lit-citadel-12163.herokuapp.com/technologies/get_all_technologies")

    unique_cities = set([])
    unique_states = set([])

    country = Country.query.first()

    if country == None:
        Country.seed('Brazil', 'Português')

    for index, user in enumerate(data_request.json()['results']):
        name = ({"name": user['name']['first'] + ' ' + user['name']['last']})
        email = ({'email': user['email']})

