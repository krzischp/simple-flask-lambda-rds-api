# https://marshmallow.readthedocs.io/en/stable/_modules/marshmallow/fields.html
# https://docs.sqlalchemy.org/en/13/core/type_basics.html

from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields

db = SQLAlchemy()


class Data(db.Model):
    __tablename__ = 'Data'
    id = db.Column(db.Integer, primary_key=True)
    notes = db.Column(db.String(128), index=True, unique=False)

    def __init__(self, notes):
        self.notes = notes

    def __repr__(self):
        return '<Data %r>' % self.notes


class DataSchema(Schema):
    id = fields.Integer(dump_only=True)
    notes = fields.String(required=True)
