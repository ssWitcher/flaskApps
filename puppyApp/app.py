from flask import Flask, render_template, url_for, redirect
from  flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from form import AddForm, DeleteForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Saurabh'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/pups'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)


class Puppy(db.Model):

	__tablename__ = 'puppies'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Text)

	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return f'{self.id} {self.name}'

@app.route('/')
def index():
	return render_template('home.html')


@app.route('/add', methods= ['GET', 'POST'])
def add_pup():
	form = AddForm()
	if form.validate_on_submit():
		name = form.name.data
		pup = Puppy(name)
		db.session.add(pup)
		db.session.commit()
		return redirect(url_for('list_pup'))
	return render_template('addpup.html', form=form)


@app.route('/del',methods=['GET', 'POST'])
def del_pup():
	form = DeleteForm()
	if form.validate_on_submit():
		id = form.id.data
		id = Puppy.query.get(id)
		db.session.delete(id)
		db.session.commit()
		return redirect(url_for('list_pup'))
	return render_template('delpup.html', form=form)

@app.route('/list')
def list_pup():
	data = Puppy.query.all()
	return render_template('listpup.html', data=data)


if __name__ == "__main__":
	app.run(debug=True)