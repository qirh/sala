# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, make_response, send_from_directory, request, redirect
app = Flask(__name__)

@app.errorhandler(404)
def error_page(error1=None, error2=None, error3=None):
    lang = request.cookies.get('lang')
    print("lang = " + lang)

    print(error1)
    if lang == "ar":
        print('/%s/404.html' %lang)
        num1 = u'٤'
        num2 = u'٠'
        num3 = u'٤'
        home = u'الصفحة الرئيسية'
    else:
        if lang != "en":
            lang = "en"
        num1 = '4'
        num2 = '0'
        num3 = '4'
        home = 'home'

    if (error2 is None or error3 is None) and lang == "ar":
        error2 = u'الصفحة غير موجودة'
        error3 = u''
    elif (error2 is None or error3 is None):
        error2 = 'PAGE NOT FOUND'
        error3 = 'The requested page could not be found'

    return render_template('/%s/404.html' %lang, title = 'Saleh', num1 = num1, num2 = num2, num3 = num3, error1 = error1, error2 = error2, error3 = error3, home = home)

@app.route("/")
@app.route ("/index")
@app.route ("/index/")
def index():
    lang = request.cookies.get('lang')
    if lang == "ar":
        res = make_response(render_template('/ar/index.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/index.html', title = 'Saleh'))
        res.set_cookie('lang', 'en')
    return res

@app.route ("/graph")
@app.route ("/graph/")
def graph():
    lang = request.cookies.get('lang')
    if lang == "ar":
        res = make_response(render_template('/en/graph.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/graph.html', title='Saleh'))
        res.set_cookie('lang', 'en')
    return res

@app.route ("/voicegarden")
@app.route ("/voicegarden/")
def voicegarden():
    lang = request.cookies.get('lang')
    if lang == "ar":
        res = make_response(render_template('/ar/voicegarden.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/voicegarden.html', title='Saleh'))
        res.set_cookie('lang', 'en')
    return res

@app.route('/cv')
@app.route('/cv/')
def cv():
    lang = request.cookies.get('lang')
    if lang == "ar":
        res = make_response(render_template('/en/cv.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/cv.html', title='Saleh'))
        res.set_cookie('lang', 'en')
    return res

@app.route('/photos/<path:filename>')
@app.route('/photos/<path:filename>/')
def get_photo(filename=None):
    lang = request.cookies.get('lang')
    if lang == "ar":
        res = make_response(render_template('/en/photo.html', filename=filename, title = filename))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/photo.html', filename=filename, title = filename))
        res.set_cookie('lang', 'en')
    return res

@app.route('/docs/cv')
@app.route('/docs/cv/')
def get_cv_file():
    filename = "CV_Saleh_Alghusson.pdf"
    lang = request.cookies.get('lang')
    res = make_response(send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True))
    if lang == "ar":
        res.set_cookie('lang', 'ar')
    else:
        res.set_cookie('lang', 'en')
    return res

@app.route('/docs/<path:filename>')
@app.route('/docs/<path:filename>/')
def get_document(filename=None):
    lang = request.cookies.get('lang')
    if filename is not None:
        arr = os.listdir(os.path.join(app.static_folder, 'docs/'))
        if filename in arr:
            res = make_response(send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True))
            if lang == "ar":
                res.set_cookie('lang', 'ar')
            else:
                res.set_cookie('lang', 'en')
            return res
    if lang == "ar":
        return error_page(error2 = u'الملف غير موجود', error3 = u'')
    else:
        return error_page(error2 = 'FILE NOT FOUND', error3 = 'The requested file could not be found')

@app.route("/blog")
@app.route("/blog/")
@app.route("/<path:filename>/blog")
@app.route("/<path:filename>/blog/")
def blog():
    return redirect("https://qirh.github.io")

@app.route("/jones")
@app.route("/jones/")
@app.route("/<path:filename>/jones")
@app.route("/<path:filename>/jones/")
def jones():
    return redirect("http://salehjones.com")

@app.route("/en")
@app.route("/en/")
@app.route("/en/index")
@app.route("/en/index/")
def en_index():
    res = make_response(render_template('/en/index.html', title = 'Saleh'))
    res.set_cookie('lang', 'en')
    return res

@app.route ("/en/graph")
@app.route ("/en/graph/")
def en_graph():
    res = make_response(render_template('/en/graph.html', title = 'Saleh'))
    res.set_cookie('lang', 'en')
    return res

@app.route ("/en/voicegarden")
@app.route ("/en/voicegarden/")
def en_voicegarden():
    res = make_response(render_template('/en/voicegarden.html', title = 'Saleh'))
    res.set_cookie('lang', 'en')
    return res

@app.route('/en/cv')
@app.route('/en/cv/')
def en_cv():
    res = make_response(render_template('/en/cv.html', title='Saleh'))
    res.set_cookie('lang', 'en')
    return res

@app.route('/en/photos/<path:filename>')
@app.route('/en/photos/<path:filename>/')
def en_get_photo(filename=None):
    res = make_response(render_template('/en/photo.html', filename=filename, title=filename))
    res.set_cookie('lang', 'en')
    return res

@app.route('/en/docs/cv')
@app.route('/en/docs/cv/')
def en_get_cv_file():
    filename = "CV_Saleh_Alghusson.pdf"
    res = make_response(send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True))
    res.set_cookie('lang', 'en')
    return res

@app.route('/en/docs/<path:filename>')
@app.route('/en/docs/<path:filename>/')
def en_get_document(filename=None):
    if filename is not None:
        arr = os.listdir(os.path.join(app.static_folder, 'docs/'))
        if filename in arr:
            filename = "CV_Saleh_Alghusson.pdf"
            res = make_response(
            send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True))
            res.set_cookie('lang', 'en')
            return res
    return error_page(error2 = 'FILE NOT FOUND', error3 = 'The requested file could not be found')

###	Arabic
@app.route("/ar")
@app.route("/ar/")
@app.route ("/ar/index")
@app.route ("/ar/index/")
def ar_index():
    res = make_response(render_template('/ar/index.html', title = u'صالح'))
    res.set_cookie('lang', 'ar')
    return res

@app.route ("/ar/graph")
@app.route ("/ar/graph/")
def ar_graph():
    res = make_response(render_template('/en/graph.html', title=u'صالح'))
    res.set_cookie('lang', 'ar')
    return res

@app.route ("/ar/voicegarden")
@app.route ("/ar/voicegarden/")
def ar_voicegarden():
    res = make_response(render_template('/ar/voicegarden.html', title=u'صالح'))
    res.set_cookie('lang', 'ar')
    return res
