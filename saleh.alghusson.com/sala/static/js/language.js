var languages = ["en", "es", "pt", "fr", "de", "ar", "he"];
var url = window.location.href.replace(/#/g, "");
var index = linkHasLanguage();

function checkLanguage(currentLanguage, newLanguage) {
    if(currentLanguage == newLanguage)
        return;
    setLanguage(newLanguage);
    reloadPage();
}
function setLanguage(language) {
    Cookies.set('language', language);
}
function getLanguage() {
    var language = Cookies.get('language');
    if(language == undefined)
        return 'en';
    else
        return language;
}
function loadPage() {
    //will be called when page first runs or

    //check if link has a language in it
    if(index >= 0){

    } else {    //else add language to link
        var indexOfSlash = nthIndex(url, "/", 3);
        window.location.href = url.substring(0, indexOfSlash) + "/" + getLanguage() + url.substring(indexOfSlash);
    }
}
function reloadPage(){

    //will be called when language is changed
    var newUrl = "";
    //if there is already a language, which should always run
    if(index >= 0){
        var indexOfSlash = nthIndex(url, "/", 3);
        newUrl = url.substring(0, indexOfSlash) + "/" + getLanguage() + url.substring(indexOfSlash+3);
    } else {    //there isn't a language, which shouldn't be true never
        newUrl = url.substring(0, index) + "/" +language+ window.location.pathname.substring(4);
    }
    window.location = newUrl
}
function linkHasLanguage(){
    var index = -1;
    for(var i = 0; i < languages.length; i++) {
        if(index >= 0)
            break;
        index = url.indexOf("/"+languages[i]);
    }
    return index;
}
/* source: https://stackoverflow.com/a/14482123 */
function nthIndex(str, pat, n){
    var L= str.length, i= -1;
    while(n-- && i++<L){
        i= str.indexOf(pat, i);
        if (i < 0) break;
    }
    return i;
}