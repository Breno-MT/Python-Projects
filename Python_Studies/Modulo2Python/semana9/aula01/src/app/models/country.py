from src.app.db import db, ma 

class Country(db.Model):
    __tablename__ = 'country'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(84), nullable=False)
    language = db.Column(db.String(84), nullable=False)

    def __init_(self, name, language):
        self.name = name
        self.language = language


class CountrySchema(ma.Schema):
    fields = ('id', 'name', 'language')

country_share_schema = CountrySchema(many=True)
