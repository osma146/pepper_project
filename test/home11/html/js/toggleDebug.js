    function toggleDebug() {
    var el = document.getElementById("Dbox");
    //alert("Clicked");

    if (el.className === "debug-box") {
        el.className = "";  // add debug
    } else {
        el.className = "debug-box";  // remove debug
    }
    }