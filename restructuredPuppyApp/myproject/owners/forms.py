from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

class AddForm(FlaskForm):
	name = StringField("The name of the owner : ")
	puppy_id = IntegerField("Id of the puppy to attach : ")
	submit = SubmitField("Add Ow ner")
