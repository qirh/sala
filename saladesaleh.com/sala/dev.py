from __init__ import app

#ssl tutorial from here: https://blog.miguelgrinberg.com/post/running-your-flask-application-over-https

if __name__ == "__main__" :
	app.run(host='0.0.0.0', use_reloader=True, debug=True)
