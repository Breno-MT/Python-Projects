from src.app.models.developer import Developer, developers_share_schema
from src.app.models.technology import technologies_share_schema

def list_all_developers_services():

    list_developers = Developer.query.all()

    list_developers_dict = developers_share_schema.dump(list_developers)

    list_all_devs = []

    for devs in list_developers_dict:
        tech_dict = technologies_share_schema.dump(devs['technologies'])
        list_all_devs.append(
            {
                "technologies": tech_dict,
                "id": devs['id'],
                'months_experience': devs['months_experience'],
                "accepted_remote_work": devs['accepted_remote_work']
            }
        )
    
    return list_all_devs
