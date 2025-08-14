import qi
import threading

def start_control_ws(session, module, host="0.0.0.0", port=9001):
    def on_message(client, server, message):
        print("ControlWS received:", message)
        if message == "speak":
            tts = session.service("ALTextToSpeech")
            tts.say(TTS_TEXT)
        elif message == "start_audio":
            print("start_audio")
            module.set_audio_enabled(True)
        elif message == "stop_audio":
            module.set_audio_enabled(False)
        elif message == "reconnect":
            module.client.reconnect_to_cloud()

    server = WebsocketServer(port, host=host)
    #server.server.setsockopt(server.SOL_SOCKET, server.SO_REUSEADDR, 1)
    server.set_fn_message_received(on_message)
    print("Control WebSocket Server listening on ws://%s:%d" % (host, port))
    server.run_forever()

def receive_thread(ws_conn, player, module, pcm_buffer, session):
    while True:
        try:
            raw = ws_conn.recv()
        except Exception:
            break
        try:
            msg = json.loads(raw)
        except ValueError:
            continue

        t = msg.get("type", "")
        print(t)
        # handle audio frames
        if t == "response.audio.delta":
            pcm = base64.b64decode(msg.get("delta", ""))
            player.stdin.write(pcm)
            module.set_audio_enabled(False)
        elif t == "input_audio_buffer.speech_started":
            module.set_playing(True)
        elif t == "response.completed":
            module.set_playing(False)
            pcm_buffer[:] = []

    try:
        player.stdin.close()
        player.wait()
    except Exception:
        pass


def sound_module():
    parser = argparse.ArgumentParser()
    parser.add_argument("--qi-url", type=str, default="tcp://127.0.0.1:9559")
    args = parser.parse_args()

    app = qi.Application(["sound_streamer", "--qi-url=" + args.qi_url])
    app.start()
    session = app.session

    ctrl_thread = threading.Thread(
        target=start_control_ws, args=(session, module)
    )
    ctrl_thread.daemon = True
    ctrl_thread.start()

    # start thread to receive and route remote audio
    pcm_buffer = []
    t = threading.Thread(
        target=receive_thread,
        args=(ws_conn, player, module, pcm_buffer, session)
    )
    t.daemon = True
    t.start()