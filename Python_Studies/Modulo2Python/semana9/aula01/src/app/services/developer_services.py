from sqlalchemy.orm import load_only

from src.app.models.developer import Developer, developers_share_schema
from src.app.models.technology import technologies_share_schema
from src.app.models.user import User, UserSchema

def list_all_developers_services():

   
    list_developers = Developer.query.all()

    list_developers_dict = developers_share_schema.dump(list_developers)
  
    return list_developers_dict
