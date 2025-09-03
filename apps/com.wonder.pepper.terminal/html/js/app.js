(function () {
  var statusEl = document.getElementById('status');

  function sendEvent(name, payload) {
    // Pepper-side: you’ll listen via ALMemory subscriber
    var xhr = new XMLHttpRequest();
    // Optional: implement a tiny local http->ALMemory bridge if you have one.
    console.log('Raise event', name, payload);
  }

  document.getElementById('btn1').onclick = function () {
    // Raise ALMemory event for Python service to speak
    // Convention: com/wonder/pepper/temp/say
    sendEvent('com/wonder/pepper/temp/say', 'Hello from tablet');
    statusEl.textContent = 'Requested say()';
  };

  document.getElementById('btn2').onclick = function () {
    sendEvent('com/wonder/pepper/temp/toggle_audio', '');
    statusEl.textContent = 'Toggled audio';
  };

  statusEl.textContent = 'Ready';
})();
