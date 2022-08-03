from src.app.db import db, ma 
from src.app.models.state import State 

class City(db.Model):
    __tablename__ = 'cities'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    state_id = db.Column(db.Integer, db.ForeignKey(State.id), nullable=False)
    name= db.Column(db.String(84), nullable=False)

    def __init__(self, state_id, name):
        self.state_id = state_id
        self.name = name

class CitySchema(ma.Schema):
    class Meta:
        fields = ('id', 'state_id', 'name')

city_share_schema = CitySchema(many=True)
