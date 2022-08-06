from src.app.models.technology import TechnologySchema, technologies_share_schema
from src.app.models.user import User, UserSchema, user_developer_share_schema
from src.app.db import db, ma 

developer_technologies = db.Table('developer_technologies',
                    db.Column('developer_id', db.Integer, db.ForeignKey('developers.id')),
                    db.Column('technology_id', db.Integer, db.ForeignKey('technologies.id'))
                    )



class Developer(db.Model):
    __tablename__ = "developers"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    months_experience = db.Column(db.Integer, nullable = True)
    accepted_remote_work = db.Column(db.Boolean, nullable = False, default = True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable = False)
    technologies = db.relationship('Technology', secondary=developer_technologies, backref='developers')
    user = db.relationship('User', foreign_keys=[user_id])

    def __init__(self, months_experience, accepted_remote_work, user_id, technologies):
        self.months_experience = months_experience
        self.accepted_remote_work = accepted_remote_work
        self.user_id = user_id
        self.technologies = technologies


    @classmethod
    def seed(cls, months_experience, accepted_remote_work, user_id, technologies):
        developer = Developer(
        months_experience = months_experience,
        accepted_remote_work = accepted_remote_work,
        user_id = user_id,
        technologies = technologies
        )

        developer.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

class DeveloperSchema(ma.Schema):
    technologies = ma.Nested(technologies_share_schema)
    user = ma.Nested(user_developer_share_schema)

    class Meta:
        fields = ('id', 'months_experience', 'accepted_remote_work', 'user_id', 'technologies', 'user')

developer_share_schema = DeveloperSchema()
developers_share_schema = DeveloperSchema(many=True)
