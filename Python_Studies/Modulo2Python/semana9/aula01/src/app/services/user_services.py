from src.app.models.user import User
from src.app.models.roles import Role

def create_user(city_id, name, age, email, password, roles = "HELPER"):
    try:
        roles_query = Role.query.filter_by(description = roles).all()
    
        User.seed(
            city_id, 
            name, 
            age, 
            email, 
            password, 
            roles_query
        )

        return {"message": "Usuário foi criado com sucesso"}

    except:
        return {"error": "Algo deu errado."}
