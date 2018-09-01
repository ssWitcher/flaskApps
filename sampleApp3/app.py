from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("home.html")

@app.route('/signup')
def signup_form():
	return render_template("signup.html")

@app.route('/thankyou')
def thankyou():
	first = request.args.get('inputFirstName')
	second = request.args.get('inputSecondName')
	return render_template('thankyou.html', first=first, second=second)

@app.errorhandler(404)
def error(e):
	return render_template('404.html'), 404

if __name__ == "__main__":
	app.run(debug=True)