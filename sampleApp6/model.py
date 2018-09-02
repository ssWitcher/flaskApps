from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Puppy(db.Model):
	__tablename__ = 'puppies'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)
	age = db.Column(db.Integer)

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __repr__(self):
		return f"Puppy {self.name} is {self.age} year/s old"


