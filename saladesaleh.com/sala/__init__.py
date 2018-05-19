# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, send_file, send_from_directory, request, redirect
app = Flask(__name__)

@app.errorhandler(404)
def own_404_page(num1=None, num2=None, num3=None, error1=None, error2=None, error3=None, back = None, home = None):

    begin = 'en'
    if (num1 is None or num2 is None or num3 is None) and request.path.startswith("/ar"):
        begin = 'ar'
        num1 = u'٤'
        num2 = u'٠'
        num3 = u'٤'
    elif (num1 is None or num2 is None or num3 is None) and not request.path.startswith("/ar"):
        num1 = '4'
        num2 = '0'
        num3 = '4'

    if (error1 is None or back is None or home is None) and request.path.startswith("/ar"):
        error1 = u'خطأ !'
        back = u'إلى الخلف'
        home = u'إلى الرئيسية'
    elif (error1 is None or back is None or home is None) and request.path.startswith("/es"):
        begin = 'es'
        error1 = u'¡Error!'
        back = u'Retroceda'
        home = u'Al Inicio'
    elif (error1 is None or back is None or home is None) and not request.path.startswith("/ar") and not request.path.startswith("/es"):
        error1 = u'Error !'
        back = 'Go Back'
        home = 'Go Home'

    if (error2 is None or error3 is None) and request.path.startswith("/ar"):
        error2 = u'الصفحة غير موجودة'
        error3 = u''
    elif (error2 is None or error3 is None) and request.path.startswith("/es"):
        error2 = u'NO SE ENCONTRÓ LA PÁGINA'
        error3 = u''
    elif (error2 is None or error3 is None) and not request.path.startswith("/ar") and not request.path.startswith("/es"):
        error2 = 'PAGE NOT FOUND'
        error3 = 'The requested page could not be found'

    return render_template('/%s/404.html' %begin, title = 'Saleh', num1 = num1, num2 = num2, num3 = num3, error1 = error1, error2 = error2, error3 = error3, back = back, home = home)

@app.route("/")
@app.route("/en")
@app.route("/en/")
@app.route("/en/index")
@app.route ("/index")
def index():
    return render_template('/en/index.html', title = 'Saleh')
@app.route ("/en/graph")
@app.route ("/graph")
def graph():
    return render_template('/en/graph.html', title = 'Saleh')
@app.route ("/en/voicegarden")
@app.route ("/voicegarden")
def voicegarden():
    return render_template('/en/voicegarden.html', title = 'Saleh')

@app.route('/cv')
@app.route('/en/cv')
@app.route('/es/cv')
@app.route('/ar/cv')
@app.route('/docs/cv')
@app.route('/en/docs/cv')
@app.route('/es/docs/cv')
@app.route('/ar/docs/cv')
def get_cv():
    filename = 'CV_Saleh_Alghusson.pdf'
    return send_from_directory(os.path.join(app.static_folder, 'docs'), filename)


@app.route('/en/docs/<path:filename>')
@app.route('/docs/<path:filename>')
def get_pdf(filename=None):
    if filename is not None:
        arr = os.listdir(os.path.join(app.static_folder, 'docs'))
        if filename in arr:
            return send_from_directory(os.path.join(app.static_folder, 'docs'), filename)
    return own_404_page(error2 = 'FILE NOT FOUND', error3 = 'The requested file could not be found')

@app.route("/blog")
@app.route("/en/blog")
@app.route("/es/blog")
@app.route("/ar/blog")
def blog():
    return redirect("https://qirh.github.io")
@app.route("/jones")
@app.route("/en/jones")
@app.route("/es/jones")
@app.route("/ar/jones")
def jones():
    return redirect("http://salehjones.com")



###	Espangol
@app.route("/es")
@app.route("/es/")
@app.route ("/es/index")
def es_index():
    return render_template('/es/index.html', title = u'Sáleh')
@app.route ("/es/graph")
def es_graph():
    return render_template('/es/graph.html', title = u'Sáleh')
@app.route ("/es/voicegarden")
def es_voicegarden():
    return render_template('/es/voicegarden.html', title = u'Sáleh')

@app.route('/es/docs/<path:filename>')
def es_get_pdf(filename=None):
    if filename is not None:
        arr = os.listdir(os.path.join(app.static_folder, 'docs'))
        if filename in arr:
            return send_from_directory(os.path.join(app.static_folder, 'docs'), filename)
    return own_404_page(error2 = u'NO SE ENCONTRÓ EL ARCHVO', error3 = u'')

###	Arabic
@app.route("/ar")
@app.route("/ar/")
@app.route ("/ar/index")
def ar_index():
    return render_template('/ar/index.html', title = u'صالح')
@app.route ("/ar/graph")
def ar_graph():
    return render_template('/ar/graph.html', title = u'صالح')
@app.route ("/ar/voicegarden")
def ar_voicegarden():
    return render_template('/ar/voicegarden.html', title = u'صالح')

@app.route('/ar/docs/<path:filename>')
def ar_get_pdf(filename=None):
    if filename is not None:
        arr = os.listdir(os.path.join(app.static_folder, 'docs'))
        if filename in arr:
            return send_from_directory(os.path.join(app.static_folder, 'docs'), filename)
    return own_404_page(error2 = u'الملف غير موجود', error3 = '')
