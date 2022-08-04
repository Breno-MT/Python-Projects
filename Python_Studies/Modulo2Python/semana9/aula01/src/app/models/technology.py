from src.app.db import db, ma

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


class TechnologySchema(ma.Schema):

    class Meta:
        fields = ('id', 'name')

technology_share_schema = TechnologySchema(many=True)

