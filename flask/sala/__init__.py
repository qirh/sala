from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route ("/index")
def index ():
	return render_template('index.html',
						    title='saleh')

@app.route ("/cv")
def cv ():
	return render_template('cv.html',
						    title='cv')
