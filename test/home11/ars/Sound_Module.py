#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import qi
import argparse
import sys
import time
import threading
import websocket
from websocket_server import WebsocketServer
from socket_client import SocketClient
import json
import base64
import subprocess

WS_URL = "ws://wonderconnect.wonderbyte.ai/ws/robot"
WS_HEADERS = [
    "client-identity:client-RNmqg2-5OE6jRuKJ1",
    "client-secret-key:sec-F8vftol0BHp42hCwAdgExNKD"
]

SAMPLE_RATE = 48000
MIC_CHANNELS = 1
MODULE_NAME = "SoundProcessingModule"
TTS_TEXT = "Hello, I am Pepper."

class SoundProcessingModule(object):
    def __init__(self, app, socket_client, log_output=True):
        app.start()
        self.audio_service = app.session.service("ALAudioDevice")
        self.client = socket_client
        self.log_output = log_output
        self._lock = threading.Lock()
        self.audio_playing = False
        self.audio_enabled = False

    def set_playing(self, value):
        with self._lock:
            self.audio_playing = value

    def is_playing(self):
        with self._lock:
            return self.audio_playing

    def set_audio_enabled(self, value):
        with self._lock:
            self.audio_enabled = value
        print("Audio enabled set to", value)

    def is_audio_enabled(self):
        with self._lock:
            return self.audio_enabled

    def startProcessing(self):
        self.audio_service.setClientPreferences(
            MODULE_NAME, SAMPLE_RATE, MIC_CHANNELS, 0
        )
        self.audio_service.subscribe(MODULE_NAME)
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        self.audio_service.unsubscribe(MODULE_NAME)

    def processRemote(self, nbCh, nbSamps, timeStamp, inputBuffer):
        # Only forward audio if enabled
        if not self.is_audio_enabled():
            
            return
        try:
            print('SEND')
            self.client.send_audio("input_audio_buffer.append", inputBuffer)
        except Exception:
            pass

def start_control_ws(session, module, host="0.0.0.0", port=9002):
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--qi-url", type=str, default="tcp://127.0.0.1:9559")
    args = parser.parse_args()

    app = qi.Application(["sound_streamer", "--qi-url=" + args.qi_url])
    app.start()
    session = app.session

    # connect to remote audio service
    ws_conn = websocket.WebSocket()
    ws_conn.connect(WS_URL, header=WS_HEADERS)

    # audio playback process
    player = subprocess.Popen(
        ["aplay", "-f", "S16_LE", "-r", "24000", "-c", "1"],
        stdin=subprocess.PIPE
    )

    client = SocketClient(ws_conn)
    module = SoundProcessingModule(app, client)

    # start local control WebSocket server
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

    # register the service so Pepper will call processRemote()
    session.registerService(MODULE_NAME, module)
    client.send_update_event(ws_conn)
    # give NAOqi a moment then start audio subscription
    time.sleep(5)
    module.startProcessing()