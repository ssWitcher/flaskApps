from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)

app.config['SECRET_KEY'] = "saurabhshrivastava"

class InputForm(FlaskForm):
	breed = StringField("What's your breed ??")
	submit = SubmitField("Enter")

@app.route('/',methods=['GET','POST'])
def index():
	breed = False
	form  = InputForm()
	if form.validate_on_submit():	
		breed = form.breed.data
		form.breed.data = ''
	return render_template('home.html', form=form, breed=breed)

if __name__ == "__main__":
	app.run(debug=True)