
function checkLanguage(currentLanguage, newLanguage) {
    var languages = ["en", "es", "pt", "fr", "de", "ar", "he"];
    if(currentLanguage == newLanguage)
        return;
    else if ($.inArray(newLanguage, languages) > -1)
        setLanguage(newLanguage);
    else
        return;
}
function setLanguage(language) {
    $.cookie('lang', language, { expires: 7, path:'/' });
    location.reload();
}