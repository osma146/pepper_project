(function () {
  // ES5-only for Pepper's old WebKit
  var logEl = document.getElementById('log');
  var wsUrlEl = document.getElementById('wsUrl');
  var connectBtn = document.getElementById('connectBtn');
  var disconnectBtn = document.getElementById('disconnectBtn');
  var clearBtn = document.getElementById('clearBtn');
  var copyBtn = document.getElementById('copyBtn');
  var sendForm = document.getElementById('sendForm');
  var sendInput = document.getElementById('sendInput');
  var statusDot = document.getElementById('statusDot');
  var statusText = document.getElementById('statusText');
  var autoScrollCb = document.getElementById('autoScroll');
  var autoReconnectCb = document.getElementById('autoReconnect');
  var lineCountEl = document.getElementById('lineCount');
  var maxLinesEl = document.getElementById('maxLines');

  var ws = null;
  var reconnectTimer = null;
  var pingTimer = null;
  var paused = false;
  var maxLines = 2000;
  maxLinesEl.innerHTML = String(maxLines);

  function nowTS() {
    var d = new Date();
    function pad(n) { return n < 10 ? '0' + n : '' + n; }
    return pad(d.getHours()) + ':' + pad(d.getMinutes()) + ':' + pad(d.getSeconds());
  }

  function setStatus(kind, text) {
    // kind: 'red' | 'amber' | 'green'
    var color = '#a33';
    if (kind === 'green') { color = '#3aa75f'; }
    else if (kind === 'amber') { color = '#cc9a06'; }
    statusDot.style.backgroundColor = color;
    statusText.innerHTML = text;
  }

  function ensureMaxLines() {
    while (logEl.childNodes.length > maxLines) {
      logEl.removeChild(logEl.firstChild);
    }
    lineCountEl.innerHTML = String(logEl.childNodes.length);
  }

  function addLine(text, klass) {
    if (paused) { return; }
    var line = document.createElement('div');
    line.className = 'line ' + (klass || 'msg-info');

    var ts = document.createElement('span');
    ts.className = 'ts';
    ts.appendChild(document.createTextNode('[' + nowTS() + '] '));
    line.appendChild(ts);

    line.appendChild(document.createTextNode(text));
    logEl.appendChild(line);
    ensureMaxLines();

    if (autoScrollCb.checked) {
      // scroll to bottom
      logEl.scrollTop = logEl.scrollHeight + 200;
    }
  }

  function parseAndLog(raw) {
    // Try JSON {type, level, text}
    try {
      var obj = JSON.parse(raw);
      if (obj && typeof obj === 'object' && obj.text) {
        var lvl = obj.level || 'info';
        var cls = 'msg-info';
        if (lvl === 'warn') cls = 'msg-warn';
        else if (lvl === 'error' || lvl === 'err') cls = 'msg-err';
        else if (lvl === 'sys') cls = 'msg-sys';
        addLine(String(obj.text), cls);
        return;
      }
    } catch (e) { /* plain text */ }
    addLine(String(raw), 'msg-info');
  }

  function connect() {
    if (ws && (ws.readyState === 0 || ws.readyState === 1)) { return; }
    var url = wsUrlEl.value;
    try {
      ws = new WebSocket(url);
    } catch (e) {
      addLine('WebSocket create failed: ' + e, 'msg-err');
      setStatus('red', 'Create failed');
      scheduleReconnect();
      return;
    }

    setStatus('amber', 'Connecting…');
    connectBtn.disabled = true;
    disconnectBtn.disabled = false;

    ws.onopen = function () {
      setStatus('green', 'Connected');
      addLine('** connected to ' + url + ' **', 'msg-sys');
      startPing();
    };

    ws.onmessage = function (evt) {
      parseAndLog(evt.data);
    };

    ws.onclose = function () {
      stopPing();
      setStatus('red', 'Disconnected');
      addLine('** disconnected **', 'msg-sys');
      connectBtn.disabled = false;
      disconnectBtn.disabled = true;
      if (autoReconnectCb.checked) { scheduleReconnect(); }
    };

    ws.onerror = function (evt) {
      setStatus('amber', 'Error');
      addLine('ws error', 'msg-warn');
    };
  }

  function disconnect() {
    stopPing();
    if (reconnectTimer) { clearTimeout(reconnectTimer); reconnectTimer = null; }
    if (ws) {
      try { ws.close(); } catch (e) {}
      ws = null;
    }
  }

  function scheduleReconnect() {
    if (!autoReconnectCb.checked) { return; }
    if (reconnectTimer) { return; }
    reconnectTimer = setTimeout(function () {
      reconnectTimer = null;
      connect();
    }, 1500);
  }

  function startPing() {
    stopPing();
    pingTimer = setInterval(function () {
      if (ws && ws.readyState === 1) {
        try { ws.send('ping'); } catch (e) {}
      }
    }, 30000);
  }
  function stopPing() {
    if (pingTimer) { clearInterval(pingTimer); pingTimer = null; }
  }

  // Handlers
  connectBtn.onclick = connect;
  disconnectBtn.onclick = disconnect;

  clearBtn.onclick = function () {
    logEl.innerHTML = '';
    ensureMaxLines();
  };

  copyBtn.onclick = function () {
    // Select log text and copy via execCommand for old WebKit
    var range = document.createRange();
    range.selectNodeContents(logEl);
    var sel = window.getSelection ? window.getSelection() : document.selection;
    if (sel.removeAllRanges) sel.removeAllRanges();
    if (sel.addRange) sel.addRange(range);
    try {
      var ok = document.execCommand('copy');
      addLine(ok ? '** copied to clipboard **' : '** copy failed **', ok ? 'msg-sys' : 'msg-warn');
    } catch (e) {
      addLine('** copy not supported **', 'msg-warn');
    }
    if (sel.removeAllRanges) sel.removeAllRanges();
  };

  sendForm.onsubmit = function (e) {
    // prevent navigation (HTML4 quirk-safe)
    if (e && e.preventDefault) e.preventDefault();

    var text = sendInput.value;
    if (!text) { return false; }

    // local commands
    if (text === '/clear') { clearBtn.onclick(); sendInput.value = ''; return false; }
    if (text === '/pause') { paused = true; addLine('** paused **', 'msg-sys'); sendInput.value=''; return false; }
    if (text === '/resume') { paused = false; addLine('** resumed **', 'msg-sys'); sendInput.value=''; return false; }

    if (ws && ws.readyState === 1) {
      try { ws.send(text); } catch (e2) { addLine('send failed: ' + e2, 'msg-err'); }
      addLine('> ' + text, 'msg-sys'); // local echo
    } else {
      addLine('not connected', 'msg-warn');
    }
    sendInput.value = '';
    return false;
  };

  // Startup: log banner
  addLine('Pepper Terminal ready. Set WS URL and press Connect.', 'msg-sys');
})();
