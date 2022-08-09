import requests

from sqlalchemy.sql.expression import func


from src.app.models.city import City, cities_share_schema
from src.app.models.developer import Developer
from src.app.models.state import State, states_share_schema
from src.app.models.country import Country, country_share_schema
from src.app.models.user import User, users_share_schema
from src.app.models.technology import Technology
from src.app.models.roles import Role 
from src.app.models.permission import Permission 

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

    country = Country.query.first()

    if country != None:
        print('Já existe dados populados.')
        return

    brasil_code = 76
    #Requisições para pegar dados de país, estado e cidade respectivamente
    countries_data = requests.get(f"https://servicodados.ibge.gov.br/api/v1/localidades/paises/{brasil_code}")

    states_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados")

    cities_data = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios")

    country_name = countries_data.json()[0]['nome']

    Country.seed(country_name, 'Português') # Seed utilizada para salvar dados

    country = Country.query.first()

    country_dict = country_share_schema.dump(country) # Método para serializar o dado
    
    for stateObject in states_data.json(): # For para criar dados em massa dos estados
        State.seed(
            country_dict['id'],
            stateObject['nome'],
            stateObject['sigla']
        )
    
    state = State.query.order_by(State.name.asc()).all() # Query para ordenar de forma ascendente 
    state_dict = states_share_schema.dump(state)
    for city_object in cities_data.json(): # for para salvar dados da cidade
        state_id = 0
        for state_object in state_dict:# for para identificar em qual estado a cidade pertence
            if state_object['initials'] == city_object['microrregiao']['mesorregiao']['UF']['sigla']:
                state_id = state_object['id']
        City.seed(
            state_id,
            city_object['nome']
        )

    cities = City.query.order_by(City.name.asc()).all()# Query para ordenar de forma ascendente

    cities_dict = cities_share_schema.dump(cities)

    users = requests.get('https://randomuser.me/api?nat=br&results=100')
    techs = requests.get('https://lit-citadel-12163.herokuapp.com/technologies/get_all_technologies')


    permissions = ['DELETE', 'READ', 'WRITE', 'UPDATE']
    roles = ['OWNER', 'HELPER']

    for perm in permissions:
        Permission.seed(
            perm
        )

    permissions_helper = Permission.query.filter(
        Permission.description.in_([
            'READ', 'WRITE'
        ])
    ).all()

    permissions_owner = Permission.query.all()

    for index, role in enumerate(roles):
        if index == 0:
            Role.seed(
                role,
                permissions_owner
            )
        
        else:
            Role.seed(
                role,
                permissions_helper
            )


    roles_query = Role.query.filter_by(description = "HELPER").all()



    for tech_object in techs.json(): # for para salvar a lista de tecnologias
        Technology.seed(
            tech_object['name']
        )

    for user in users.json()['results']: # for criado para salvar lista de usuários
        city_id = 2 #inicialmente setado com 2, pois nem sempre é encontrado um valor definido

        for city_object in cities_dict: # for criado identificar a cidade do usuário

            if user['location']['city'] == city_object['name']:
                city_id = city_object['id']

        User.seed(
            city_id,
            user['name']['first'] + ' ' + user['name']['last'],
            user['registered']['age'],
            user['email'],
            user['login']['password'],
            roles_query
        )

    users = User.query.order_by(User.name.asc()).all()
    users_dict = users_share_schema.dump(users)

    for index, user_object in enumerate(users_dict):
        if index % 2 == 0: # if para verificar se o index é par
            techs = Technology.query.order_by(func.random()).limit(10).all() # query que retorna aleatóriamente 10 tecnologias
            Developer.seed(
                None,
                index % 2 == 0,
                user_object['id'],
                techs
            )
    print("Dados inseridos com sucesso.")
    return


