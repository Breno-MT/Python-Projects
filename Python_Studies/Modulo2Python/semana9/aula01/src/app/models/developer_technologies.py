from src.app.db import db, ma 
from src.app.models.developer import Developer
from src.app.models.technology import Technology 

class DeveloperTechnology(db.Model):
    __tablename__ = 'developer_technologies'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    technology_id = db.Column(db.Integer, db.ForeignKey(Technology.id), nullable=False)
    developer_id = db.Column(db.Integer, db.ForeignKey(Developer.id), nullable=False)
    is_main_tech = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, technology_id, developer_id, is_main_tech):
        self.technology_id = technology_id
        self.developer_id = developer_id
        self.is_main_tech = is_main_tech

class DeveloperTechnologySchema(ma.Schema):
    class Meta:
        fields = ('id', 'technology_id', 'developer_id', 'is_main_tech')

dev_tech_share_schema = DeveloperTechnologySchema(many=True)
