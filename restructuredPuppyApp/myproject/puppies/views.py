from flask import Blueprint, render_template, url_for, redirect
from myproject.puppies.forms import AddForm, DeleteForm
from myproject.models import Puppy
from myproject import db


puppies_blueprint = Blueprint('puppies', __name__, template_folder='templates/puppies')

@puppies_blueprint.route('/add', methods=['GET','POST'])
def add_pup():
	form = AddForm()
	if form.validate_on_submit():
		name = form.name.data
		pup = Puppy(name)
		db.session.add(pup)
		db.session.commit()
		return redirect(url_for('puppies.list_pup'))
	return render_template('addpup.html', form=form)

@puppies_blueprint.route('/del',methods=['GET', 'POST'])
def del_pup():
	form = DeleteForm()
	if form.validate_on_submit():
		id = form.id.data
		id = Puppy.query.get(id)
		db.session.delete(id)
		db.session.commit()
		return redirect(url_for('puppies.list_pup'))
	return render_template('delpup.html', form=form)

@puppies_blueprint.route('/list')
def list_pup():
	data = Puppy.query.all()
	return render_template('listpup.html', data=data)