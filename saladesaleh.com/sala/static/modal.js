function modal(id) {

    console.log("modal -- " + id);

    var modal = document.getElementById('modal');
    var img = document.getElementById(id);
    var modalImg = document.getElementById("modalImg");
    var captionText = document.getElementById("modalCaption");
    var span = document.getElementsByClassName("modalClose")[0];

    span.onclick = function() {
        console.log("modal3");
        modal.style.display = "none";
    }
    modal.style.display = "block";
    modalImg.src = img.src;
    captionText.innerHTML = img.alt;
}
