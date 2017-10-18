from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route ("/index")
def index():
	return render_template('index.html',
						    title='Saleh')
@app.route ("/cv")
def cv():
	return render_template('cv.html',
						    title='Saleh')
@app.route ("/graph")
def graph():
	return render_template('graph.html',
						    title='Saleh')
@app.route ("/projects")
def projects():
	return render_template('projects.html',
						    title='Saleh')
@app.route ("/artnavigator")
def artnavigator():
	return render_template('proj-artnavigator.html',
						    title='Saleh')
@app.route ("/myqueue")
def myqueue():
	return render_template('proj-myqueue.html',
						    title='Saleh')
@app.route ("/gameoflife")
def gameoflife():
	return render_template('proj-gameoflife.html',
						    title='Saleh')
@app.route ("/sala")
def sala():
	return render_template('proj-sala.html',
						    title='Saleh')
@app.route ("/downing")
def downing():
	return render_template('proj-downing.html',
						    title='Saleh')
@app.route ("/texas")
def texas():
	return render_template('proj-texas.html',
						    title='Saleh')
