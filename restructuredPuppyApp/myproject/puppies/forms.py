from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
	name = StringField("The name of the puppy : ")
	submit = SubmitField("Add Puppy")

class DeleteForm(FlaskForm):
	id = IntegerField("Enter the id of the puppy you want to remove : ")
	submit = SubmitField("Delete puppy")