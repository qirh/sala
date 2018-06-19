# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, make_response, send_from_directory, request, redirect
app = Flask(__name__)
app.url_map.strict_slashes = False

langauges = {'en':'', 'pt':'language coming soon', 'es':'language coming soon', 'fr':'language coming soon', 'de':'language coming soon', 'ar':'', 'he':'language coming soon'}
lang_default = 'en' #TODO: set default langugae based on broweser prefrence
routes = ['', 'blog', 'cv', 'graph', 'index', 'jones', 'voicegarden']
routes_follow = ['docs', 'photos']

@app.errorhandler(404)
def error_page(error1=None, error2=None, error3=None):
    lang = request.cookies.get('lang')
    if lang == 'ar':
        num1 = u'٤'
        num2 = u'٠'
        num3 = u'٤'
        home = u'الصفحة الرئيسية'
    else:
        if lang != 'en':
            lang = 'en'
        num1 = '4'
        num2 = '0'
        num3 = '4'
        home = 'home'

    if (error2 is None or error3 is None) and lang == 'ar':
        error2 = u'الصفحة غير موجودة'
        error3 = u''
    elif (error2 is None or error3 is None):
        error2 = 'PAGE NOT FOUND'
        error3 = 'The requested page could not be found'

    return render_template('/%s/404.html' %lang, title = 'Saleh', num1 = num1, num2 = num2, num3 = num3, error1 = error1, error2 = error2, error3 = error3, home = home)

@app.route('/')
@app.route ('/index')
def index():
    lang = request.cookies.get('lang')
    if lang == 'ar':
        res = make_response(render_template('/ar/index.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/index.html', title = 'Saleh'))
        res.set_cookie('lang', 'en')
    return res

# takes an optional language
@app.route('/<path:lang>')
@app.route ('/<path:lang>/index')
def lang_index(lang=None):

    # if no language specified in url check cookies
    if not lang:
        lang = request.cookies.get('lang')
        # if nothing in cookies
        if not lang:
            # change to default
            lang = lang_default

    # if language specified is not in the dict of supported laguages
    if not lang in langauges:
        lang = lang_default

    res = make_response(redirect('/'))
    res.set_cookie('lang', lang)
    return res


@app.route ('/graph')
def graph():
    lang = request.cookies.get('lang')
    if lang == 'ar':
        res = make_response(render_template('/en/graph.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/graph.html', title='Saleh'))
        res.set_cookie('lang', 'en')
    return res

@app.route ('/voicegarden')
def voicegarden():
    lang = request.cookies.get('lang')
    if lang == 'ar':
        res = make_response(render_template('/ar/voicegarden.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/voicegarden.html', title='Saleh'))
        res.set_cookie('lang', 'en')
    return res

@app.route('/cv')
def cv():
    lang = request.cookies.get('lang')
    if lang == 'ar':
        res = make_response(render_template('/en/cv.html', title=u'صالح'))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/cv.html', title='Saleh'))
        res.set_cookie('lang', 'en')
    return res

@app.route('/photos/<path:filename>')
def get_photo(filename=None):
    lang = request.cookies.get('lang')
    if lang == 'ar':
        res = make_response(render_template('/en/photo.html', filename=filename, title = filename))
        res.set_cookie('lang', 'ar')
    else:
        res = make_response(render_template('/en/photo.html', filename=filename, title = filename))
        res.set_cookie('lang', 'en')
    return res

@app.route('/docs/cv')
def get_cv_file():
    filename = 'CV_Saleh_Alghusson.pdf'
    lang = request.cookies.get('lang')
    res = make_response(send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True))
    if lang == 'ar':
        res.set_cookie('lang', 'ar')
    else:
        res.set_cookie('lang', 'en')
    return res

@app.route('/docs/<path:filename>')
def get_document(filename=None):
    lang = request.cookies.get('lang')
    if filename is not None:
        arr = os.listdir(os.path.join(app.static_folder, 'docs/'))
        if filename in arr:
            res = make_response(send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True))
            if lang == 'ar':
                res.set_cookie('lang', 'ar')
            else:
                res.set_cookie('lang', 'en')
            return res
    if lang == 'ar':
        return error_page(error2 = u'الملف غير موجود', error3 = u'')
    else:
        return error_page(error2 = 'FILE NOT FOUND', error3 = 'The requested file could not be found')

@app.route('/blog')
@app.route('/<path:lang>/blog')
def blog(lang=None):
    return redirect('https://qirh.github.io')

@app.route('/jones')
@app.route('/<path:lang>/jones')
def jones(lang=None):
    return redirect('http://salehjones.com')
