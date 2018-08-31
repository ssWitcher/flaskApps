from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	name = "Saurabh"
	letters = list(name)
	return render_template('home.html', name=name, letters=letters) 

if __name__ == "__main__":
	app.run(debug=True)