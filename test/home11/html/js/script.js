
// theme toggle (old syntax, no arrow functions)
document.addEventListener('DOMContentLoaded', function() {
    var toggleBtn = document.getElementById('theme-toggle');
    var logo = document.getElementById('logo');
    var body = document.body;

    toggleBtn.addEventListener('click', function() {
    if (body.className.indexOf('dark') === -1) {
        body.className += ' dark';
        logo.src = 'logo_dark.png';
    } else {
        body.className = body.className.replace('dark', '').trim();
        logo.src = 'logo.png';
    }
    });

    // equalize button sizes manually
    var buttons = document.getElementsByClassName('code-btn');

    for (var i = 0; i < buttons.length; i++) {
    var btn = buttons[i];
    btn.style.width = 'auto';
    btn.style.height = 'auto';
    var rect = btn.getBoundingClientRect();
    if (rect.width > maxW) maxW = rect.width;
    if (rect.height > maxH) maxH = rect.height;
    }

    for (var j = 0; j < buttons.length; j++) {
    buttons[j].style.width = maxW + 'px';
    buttons[j].style.height = maxH + 'px';
    }
});

function runCode(n) {
    var headerBox = document.getElementById('header-box');
    var bodyBox = document.getElementById('body-box');

    if (n === 6) {

    if (headerBox.className === '') {

        bodyBox.className = 'debug-box';
    } else if (headerBox.className === 'debug-box') {

        bodyBox.className = '';
    }
    }
}

    // fallback runCode functio
