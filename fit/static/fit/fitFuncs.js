// Functions for making Popup windows on index.html visible
function overlay() {
    el = document.getElementById("box1");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}

function overlay2() {
    el = document.getElementById("box2");
    el.style.visibility = (el.style.visibility == "visible") ? "hidden" : "visible";
}