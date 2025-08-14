var ws = null;
var statusEl = document.getElementById("status");


function connectWebSocket() {
  ws = new WebSocket("ws://198.18.0.1:9001");

  ws.onopen = function() {
    statusEl.innerText = "Connected";
    console.log("WebSocket opened");
  };

  ws.onmessage = function(e) {
    recvMessage(e.data);
  };

  ws.onclose = function() {
    statusEl.innerText = "Disconnected";
    console.log("WebSocket closed");
  };

  ws.onerror = function(err) {
    statusEl.innerText = "Connection Error";
    console.error("WebSocket error", err);
  };
}

function sendMessage(message) {
  if (ws && ws.readyState === 1) {
    ws.send(JSON.stringify(message));
    console.log("Sent message");
  } else {
    console.warn("WebSocket not connected");
    connectWebSocket();
  }
}

function sendMessages(message) {
  var keys = Object.keys(message).map(function(k) { return parseInt(k); });
  keys.sort(function(a, b) { return a - b; });

  for (var i = 0; i < keys.length; i++) {
    var key = keys[i];
    var msg = message[key];
    sendMessage(msg);
  }
}

function recvMessage(e) {
  console.log("Received from server:", e);
  try {
    var data = JSON.parse(e);
    console.log("Received:", data);

    if (data.type === "response") {

      statusEl.innerText = "Server: " + data.value;
    }
  } catch (err) {
    console.warn("Non-JSON message:", e);
  }
}

window.onload = connectWebSocket;
