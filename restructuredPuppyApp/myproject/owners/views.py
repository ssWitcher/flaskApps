from flask import Blueprint, render_template, url_for, redirect
from myproject.owners.forms import AddForm
from myproject.models import Owner
from myproject import db


owners_blueprint = Blueprint('owners', __name__, template_folder='templates/owner')

@owners_blueprint.route('/add', methods=['GET','POST'])
def add_owner():
	form = AddForm()
	if form.validate_on_submit():
		name = form.name.data
		puppy_id = form.puppy_id.data	
		owner = Owner(name,puppy_id)
		db.session.add(owner)
		db.session.commit()
		return redirect(url_for('puppies.list_pup'))
	return render_template('addowner.html', form=form)