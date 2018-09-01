from flask import Flask, render_template, url_for, redirect, session 
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField, SelectField, TextField,
					TextAreaField, SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = "SaurabhShrivastava"


class InfoForm(FlaskForm):
	breed = StringField("What's your breed? ", validators=[DataRequired()])
	neutured = BooleanField("Are you neutured? ")
	mood = RadioField("Please choose your mood : ",choices=[("one","Happy"),("two","Sad")])
	color_choice = SelectField("Pick your favourite color : ",choices=[("red","Red"),("blue","Blue"),
		("green","Green"),("yellow","Yellow")])
	feedback = TextAreaField()
	submit = SubmitField("Enter")

@app.route('/', methods=['GET','POST'])
def index():
	form = InfoForm()
	if form.validate_on_submit():
		session['breed'] = form.breed.data
		session['neutured'] = form.neutured.data
		session['mood'] = form.mood.data
		session['color_choice'] = form.color_choice.data
		session['feedback'] = form.feedback.data
		return redirect(url_for("thankyou"))
	return render_template("index.html",form=form)

@app.route('/thankyou')
def thankyou():
	return render_template('thankyou.html')

if __name__ == "__main__":
	app.run(debug=True)
