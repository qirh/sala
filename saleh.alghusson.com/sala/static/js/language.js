var languages = ["en", "es", "pt", "fr", "de", "ar", "he"];
var ready_languages = ["en", "ar"];
var lang_default = 'en' //TODO: set default langugae based on broweser prefrence

function check_language(current_lang, new_lang) {

    if(current_lang == new_lang)
        return;
    else if ($.inArray(new_lang, languages) > -1)
        set_language_cookie(new_lang);
    else
        set_language_cookie(lang_default);
}
function set_language_cookie(lang) {
    var ret;
    if ($.inArray(lang, ready_languages) > -1) {
        $.cookie('lang', lang, {expires: 7, path: '/'});
        ret = lang;
    }
    else {
        $.cookie('lang', lang_default, {expires: 7, path: '/'});
        ret = lang_default;
    }

    location.reload();
    return ret;
}
function get_language_cookie() {
    var lang = $.cookie('lang');

    if(lang)
        return lang;
    return lang_default;
}
function ready_cookie() {
    $.cookie('lang', get_language_cookie(), { expires: 7, path:'/' });
}
document.addEventListener('DOMContentLoaded', function() {ready_cookie();}, false);