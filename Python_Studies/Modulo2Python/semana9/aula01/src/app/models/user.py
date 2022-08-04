from src.app.db import db, ma
from src.app.models.city import City

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey(City.id), nullable=False)
    name = db.Column(db.String(84), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(84), nullable=False)
    password = db.Column(db.String(84), nullable=False)

    def __init__(self, city_id, name, age, email, password):
        self.city_id = city_id
        self.name = name
        self.age = age
        self.email = email
        self.password = password

    @classmethod
    def seed(cls, city_id, name, age, email, password):
        user = User(
            city_id = city_id,
            name = name,
            age = age,
            email = email,
            password = password
        )

        user.save()

    def save(self):
        db.session.add(self)
        db.session.commit()




class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'city_id', 'name', 'age', 'email', 'password')

users_share_schema = UserSchema(many=True)
