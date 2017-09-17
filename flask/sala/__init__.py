from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route ("/index")
def index():
	return render_template('index.html',
						    title='saleh')
@app.route ("/cv")
def cv():
	return render_template('cv.html',
						    title='cv')
@app.route ("/graph")
def graph():
	return render_template('graph.html',
						    title='graph')
@app.route ("/projects")
def projects():
	return render_template('projects.html',
						    title='projects')
@app.route ("/artnavigator")
def artnavigator():
	return render_template('proj-artnavigator.html',
						    title='artnavigator')
@app.route ("/myqueue")
def myqueue():
	return render_template('proj-myqueue.html',
						    title='myqueue')
@app.route ("/apex")
def apex():
	return render_template('apex.html',
						    title='apex')
@app.route ("/stockexchange")
def stockexchange():
	return render_template('stockexchange.html',
						    title='stockexchange')
@app.route ("/emailmanager")
def emailmanager():
	return render_template('emailmanager.html',
						    title='emailmanager')
