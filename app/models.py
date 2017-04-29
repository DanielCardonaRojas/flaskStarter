from app import db
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

class Settings(db.Model):
    __tablename__ = 'settings'
    name = db.Column(db.String(),unique = True, primary_key=True)
    value = db.Column(db.String())
