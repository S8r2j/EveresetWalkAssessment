from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import settings

app = Flask(__name__)

# configuring the database url to connect with db at localhost
app.config["SQLALCHEMY_DATABASE_URI"] = f'postgresql://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOST}/{settings.DATABASE_NAME}'
db = SQLAlchemy(app)

# creating tables for storage of data
class user(db.Model):
    id = db.Column(db.Integer, nullable = False, autoincrement = True, primary_key = True)
    name = db.Column(db.String(50), nullable = False)
    email = db.Column(db.String(100), nullable = False, unique = True)
    phone = db.Column(db.String(10), nullable = False, unique = True)
    issuperuser = db.Column(db.Boolean, default = False)
    login = db.relationship('login', backref = 'account', lazy = True)

class login(db.Model):
    index = db.Column(db.Integer, nullable = False, autoincrement = True, primary_key = True)
    id = db.Column(db.Integer, db.ForeignKey('user'), nullable = False)
    password = db.Column(db.Text, nullable = False)


# creating the tables in the postgresql database
with app.app_context():
    db.create_all()