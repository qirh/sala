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
@app.route ("/projects")
def cv ():
	return render_template('projects.html',
						    title='cv')
@app.route ("/artnavigator")
def cv ():
	return render_template('artnavigator.html',
						    title='cv')
@app.route ("/myqueue")
def cv ():
	return render_template('myqueue.html',
						    title='cv')
@app.route ("/apex")
def cv ():
	return render_template('apex.html',
						    title='cv')
@app.route ("/stockexchange")
def cv ():
	return render_template('stockexchange.html',
						    title='cv')
@app.route ("/emailmanager")
def cv ():
	return render_template('emailmanager.html',
						    title='cv')
