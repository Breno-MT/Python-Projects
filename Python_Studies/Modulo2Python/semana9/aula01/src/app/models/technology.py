from src.app.db import db, ma
from src.app.models.user import user_developer_share_schema


class Technology(db.Model):
    __tablename__ = "technologies"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    


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


class DeveloperSchema(ma.Schema):

    user = ma.Nested(user_developer_share_schema)

    class Meta:
        fields = ('id', 'months_experience', 'accepted_remote_work', 'user_id', 'user')

developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many=True)


class TechnologySchema(ma.Schema):
    developers = ma.Nested(developers_share_schema)

    class Meta:
        fields = ('id', 'name', 'developers')

technology_share_schema = TechnologySchema()
technologies_share_schema = TechnologySchema(many=True)

