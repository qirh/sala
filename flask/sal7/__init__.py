from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def homepage():
    return "Hola!"

@app.route ( '/index' )
def index ():
	return render_template('index.html', title='Mi sala')
