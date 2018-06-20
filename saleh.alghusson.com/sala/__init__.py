# -*- coding: utf-8 -*-

import os
from flask import Flask, render_template, make_response, send_from_directory, request, redirect
app = Flask(__name__)
app.url_map.strict_slashes = False

languages = {'en':'', 'pt':'language coming soon', 'es':'language coming soon', 'fr':'language coming soon', 'de':'language coming soon', 'ar':'', 'he':'language coming soon'}
lang_default = 'en' #TODO: set default langugae based on broweser prefrence

#routes = ['', 'blog', 'cv', 'graph', 'index', 'jones', 'voicegarden']
#routes_follow = ['docs', 'photos']


@app.errorhandler(404)
def error_page(error1=None, error2=None, error3=None):
    lang = get_lang()
    if lang == 'ar':
        num1 = u'٤'
        num2 = u'٠'
        num3 = u'٤'
    else:
        if lang != 'en':
            lang = 'en'
        num1 = '4'
        num2 = '0'
        num3 = '4'

    if (error2 is None or error3 is None) and lang == 'ar':
        error2 = u'الصفحة غير موجودة'
        error3 = u''
    elif (error2 is None or error3 is None):
        error2 = 'PAGE NOT FOUND'
        error3 = 'The requested page could not be found'

    return render_template('/%s/back_button.html' %lang, task='404', title = 'Saleh', num1 = num1, num2 = num2, num3 = num3, error1 = error1, error2 = error2, error3 = error3)


def get_lang(lang=None):
    # if no language specified in url check cookies
    if not lang:
        lang = request.cookies.get('lang')
        # if nothing in cookies
        if not lang:
            # change to default
            lang = lang_default

    # if language specified is not in the dict of supported languages
    if not lang in languages:
        lang = lang_default
    return lang


@app.route('/')
@app.route ('/index')
def index():
    lang = get_lang()
    if lang == 'ar':
        return render_template('/ar/index.html', title=u'صالح')
    else:
        return render_template('/en/index.html', title = 'Saleh')
# takes an optional language
@app.route('/<path:lang>')
@app.route ('/<path:lang>/index')
def lang_index(lang=None):
    if lang in languages:
        res = make_response(redirect('/'))
        res.set_cookie('lang', get_lang(lang))
        return res
    return error_page()


@app.route ('/graph')
def graph():
    lang = get_lang()
    if lang == 'ar':
        return render_template('/ar/back_button.html', task='graph', title=u'صالح')
    else:
        return render_template('/en/back_button.html', task='graph', title='Saleh')
# takes an optional language
@app.route ('/<path:lang>/graph')
def lang_graph(lang=None):
    res = make_response(redirect('/graph'))
    res.set_cookie('lang', get_lang(lang))
    return res

@app.route ('/voicegarden')
def voicegarden():
    lang = get_lang()
    if lang == 'ar':
        return render_template('/ar/back_button.html', task='voicegarden', title=u'صالح')
    else:
        return render_template('/en/back_button.html', task='voicegarden', title='Saleh')
# takes an optional language
@app.route ('/<path:lang>/voicegarden')
def lang_voicegarden(lang=None):
    res = make_response(redirect('/voicegarden'))
    res.set_cookie('lang', get_lang(lang))
    return res


@app.route('/cv')
def cv():
    lang = get_lang()
    if lang == 'ar':
        return render_template('/ar/back_button.html', task='cv', title=u'صالح')
    else:
        return render_template('/en/back_button.html', task='cv', title='Saleh')
# takes an optional language
@app.route ('/<path:lang>/cv')
def lang_cv(lang=None):
    res = make_response(redirect('/cv'))
    res.set_cookie('lang', get_lang(lang))
    return res


@app.route('/photos/<path:filename>')
def get_photo(filename=None):
    lang = get_lang()
    if lang == 'ar':
        return render_template('/ar/back_button.html', task='photo', filename=filename, title = filename)
    else:
        return render_template('/en/back_button.html', task='photo', filename=filename, title = filename)
# takes an optional language
@app.route ('/<path:lang>/photos/<path:filename>')
def lang_get_photo(lang=None, filename=None):
    res = make_response(redirect('/photos/'+ filename))
    res.set_cookie('lang', get_lang(lang))
    return res


@app.route('/docs/<path:filename>')
def get_document(filename=None):
    lang = get_lang()
    if filename is not None:
        arr = os.listdir(os.path.join(app.static_folder, 'docs/'))
        if filename in arr:
            return send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True)
    if lang == 'ar':
        return error_page(error2 = u'الملف غير موجود', error3 = u'')
    else:
        return error_page(error2 = 'FILE NOT FOUND', error3 = 'The requested file could not be found')
# takes an optional language
@app.route ('/<path:lang>/docs/<path:filename>')
def lang_get_document(lang=None, filename=None):
    res = make_response(redirect('/docs/'+ filename))
    res.set_cookie('lang', get_lang(lang))
    return res


@app.route('/docs/cv')
def get_document_cv():
    filename = 'CV_Saleh_Alghusson.pdf'
    lang = get_lang()
    if lang == 'ar':
        return send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True)
    else:
        return send_from_directory(os.path.join(app.static_folder, 'docs/'), filename, as_attachment=True)
# takes an optional language
@app.route ('/<path:lang>/cv')
def lang_get_document_cv(lang=None):
    res = make_response(redirect('/docs/cv'))
    res.set_cookie('lang', get_lang(lang))
    return res


@app.route('/blog')
@app.route('/<path:lang>/blog')
def blog(lang=None):
    return redirect('https://qirh.github.io')


@app.route('/jones')
@app.route('/<path:lang>/jones')
def jones(lang=None):
    return redirect('http://salehjones.com')
