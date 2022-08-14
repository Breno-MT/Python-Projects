from src.app.db import db, ma
from src.app.models.developer import developers_share_schema, developer_technologies
from src.app.models.user import user_developer_share_schema


class Technology(db.Model):
    __tablename__ = "technologies"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    devs = db.relationship('Technology', secondary=developer_technologies, backref='technologies')


    def __init__(self, name):
        self.name = name

    @classmethod
    def seed(cls, name):
        tech = Technology(
            name = name
        )

        tech.save()

    def save(self):
        db.session.add(self)
        db.session.commit()


class TechnologySchema(ma.Schema):

    class Meta:
        fields = ('id', 'name')

technology_share_schema = TechnologySchema()
technologies_share_schema = TechnologySchema(many=True)

class DevelopersSchema(ma.Schema):
    devs = ma.Nested(developers_share_schema)
    user = ma.Nested(user_developer_share_schema)

    class Meta:
        fields = ('id', 'name', 'devs')

devs_techs_share_schema = DevelopersSchema(many=True)
