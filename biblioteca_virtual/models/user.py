from enum import Enum

from biblioteca_virtual.extensions import db

class Roles(Enum):
    ADMIN = "admin"
    USER = "user"

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    role = db.Column(db.Enum(Roles), nullable=False)
