
function mail(){
	console.log("here")
	var string1 = "live";
	var string2 = "@";
	var string3 = "salehg";
	var string4 = string3 + string2 + string1;
	
	var com = "mailto:" + string4 + ".com"

	console.log("sorry for the hassle, i didn't want to leave my email address for scrapers")
	document.getElementById("correo electrónico").href = com;
}