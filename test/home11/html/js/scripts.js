    var ws, statusEl, btnEl, rippleEl, audioState = false;

    function init() {
      statusEl = document.getElementById('status');
      btnEl = document.getElementById('toggleBtn');
      rippleEl = document.getElementById('ripple');
      wsConnect();
    }

    function wsConnect() {
      ws = new WebSocket("ws://198.18.0.1:9001");
      ws.onopen = function() {
        statusEl.innerText = 'Connected';
        btnEl.classList.remove('disabled');
      };
      ws.onmessage = function(e) {
        try {
          var msg = JSON.parse(e.data);
          if (typeof msg.audio_enabled !== 'undefined') {
            setAudioState(msg.audio_enabled);
          }
        } catch(err) {
          console.log('Non-JSON message:', e.data);
        }
      };
      ws.onclose = function() {
        statusEl.innerText = 'Connection closed';
        btnEl.classList.add('disabled');
      };
      ws.onerror = function() {
        statusEl.innerText = 'Error';
        btnEl.classList.add('disabled');
      };
    }

    function setAudioState(enabled) {
      audioState = enabled;
      btnEl.innerText = enabled ? 'Stop Audio Stream' : 'Start Audio Stream';
      // toggle ripple container
      if (enabled) rippleEl.classList.add('active');
      else rippleEl.classList.remove('active');
    }

    function toggleAudio() {
      if (!ws || ws.readyState !== 1) return;
      if (!audioState) {
        ws.send('start_audio');
        setAudioState(true);
        setTimeout(function() {
        //   ws.send('stop_audio');
          setAudioState(false);
        }, 5000);
      }
    }
    
    function sendReconnect() {
      if (!ws || ws.readyState !== 1) return;
      ws.send('reconnect');
      // 可以给用户反馈
      statusEl.innerText = "Reconnect command sent to Pepper...";
    }