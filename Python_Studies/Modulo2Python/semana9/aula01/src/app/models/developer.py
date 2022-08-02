from src.app.db import db, ma 

class Developer(db.Model):
    __tablename__ = "developers"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    months_experience = db.Column(db.Integer, nullable=False)
    accept_remote_work = db.Column(db.Boolean, nullable=False, default=True)

    def __init__(self, months_experience, accepted_remote_work):
        self.months_experience = months_experience
        self.accept_remote_work = accepted_remote_work

class DeveloperSchema(ma.Schema):
    class Meta:
        fields = ('id', 'months_experience', 'accept_remote_work')

developer_share_schema = DeveloperSchema(many=True)
