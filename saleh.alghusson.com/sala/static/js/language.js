var languages = ["en", "es", "pt", "fr", "de", "ar", "he"];

function checkLanguage(currentLanguage, newLanguage) {
    if(currentLanguage == newLanguage)
        return;
    setLanguage(newLanguage);
}
function setLanguage(language) {
    //Cookies.set('lang', language);
    $.cookie('lang', language, { expires: 7 });
    location.reload();

}