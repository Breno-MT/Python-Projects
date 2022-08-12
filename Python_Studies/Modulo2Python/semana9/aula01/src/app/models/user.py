import bcrypt

from src.app.db import db, ma
from src.app.models.city import City, city_share_schema
from src.app.models.roles import roles_share_schema

users_roles = db.Table('users_role',
                    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                    db.Column('role_id', db.Integer, db.ForeignKey('role.id'))
                    )



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    city_id = db.Column(db.Integer, db.ForeignKey(City.id), nullable=False)
    name = db.Column(db.String(84), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(84), nullable=False)
    password = db.Column(db.String(84), nullable=False)
    city = db.relationship("City", foreign_keys=[city_id])
    roles = db.relationship('Role', secondary=users_roles, backref='users')



    def __init__(self, city_id, name, age, email, password, roles):
        self.city_id = city_id
        self.name = name
        self.age = age
        self.email = email
        self.password = password
        self.roles = roles

    @classmethod
    def seed(cls, city_id, name, age, email, password, roles):
        user = User(
            city_id = city_id,
            name = name,
            age = age,
            email = email,
            password = cls.encrypt_password(password.encode('utf-8')),
            roles = roles
        )

        user.save()

    @staticmethod
    def encrypt_password(password):
        return bcrypt.hashpw(password, bcrypt.gensalt()).decode('utf-8')


    def check_password(self, password):
        return bcrypt.checkpw(password.encode("utf-8"), self.password.encode("utf-8"))

    def save(self):
        db.session.add(self)
        db.session.commit()


class UserSchema(ma.Schema):
    
    city = ma.Nested(city_share_schema)
    roles = ma.Nested(roles_share_schema)

    class Meta:
        fields = ('id', 'city_id', 'name', 'age', 'email', 'password', 'city', 'roles')

user_share_schema = UserSchema()
users_share_schema = UserSchema(many=True)


class UserDevelopersSchema(ma.Schema):

    city = ma.Nested(city_share_schema)
    roles = ma.Nested(roles_share_schema)

    class Meta:
        fields = ('city_id', 'name', 'age', 'email', 'city', 'roles')

user_developer_share_schema = UserDevelopersSchema()
user_developers_share_schema = UserDevelopersSchema(many=True)
