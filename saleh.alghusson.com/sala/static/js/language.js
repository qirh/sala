var languages = ["en", "es", "pt", "fr", "de", "ar", "he"];
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
    $.cookie('lang', lang, { expires: 7, path:'/' });
    location.reload();
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