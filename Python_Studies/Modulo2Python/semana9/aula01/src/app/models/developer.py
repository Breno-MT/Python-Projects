from src.app.db import db, ma 
from src.app.models.user import User

class Developer(db.Model):
    __tablename__ = "developers"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    months_experience = db.Column(db.Integer, nullable=True)
    accept_remote_work = db.Column(db.Boolean, nullable=False, default=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)

    def __init__(self, months_experience, accepted_remote_work, user_id):
        self.months_experience = months_experience
        self.accept_remote_work = accepted_remote_work
        self.user_id = user_id

    @classmethod
    def seed(cls, months_experience, accepted_remote_work, user_id):
        developer = Developer(
            months_experience = months_experience, 
            accepted_remote_work = accepted_remote_work,
            user_id = user_id
        )

        developer.save()

    def save(self):
        db.session.add(self)
        db.session.commit()

class DeveloperSchema(ma.Schema):
    class Meta:
        fields = ('id', 'months_experience', 'accept_remote_work', 'user_id')

developer_share_schema = DeveloperSchema(many=True)
