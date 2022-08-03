from src.app.db import db,ma 
from src.app.models.country import Country

class State(db.Model):
    __tablename__ = 'states'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    country_id = db.Column(db.Integer, db.ForeignKey(Country.id), nullable=False)
    name = db.Column(db.String(84), nullable=False)
    initials = db.Column(db.String(2), nullable=False)

    def __init__(self, country_id, name, initials):
        self.country_id = country_id
        self.name = name
        self.initials = initials

class StateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'country_id', 'name', 'initials')

state_share_schema = StateSchema(many=True)
