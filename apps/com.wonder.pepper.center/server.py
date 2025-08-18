# -*- coding: utf-8 -*-
from websocket_server import WebsocketServer
from naoqi import ALProxy
import os
import json
import random
import threading
import time
from ars import event_handler

def on_event_page_move(data):
    value = data.get("destination", "")
    if value != "":
            version = random.randint(1, 9999)
            url = 'http://198.18.0.1/apps/home11/{}.html?version={}'.format(value.strip(), version)
            os.system('qicli call ALTabletService.showWebview "{}"'.format(url))


# Called for every client connecting (before handshake)
def new_client(client, server):
    print("🔌 Client connected:", client['address'])
    msg = {"type": "response", "value": "Welcome!"}
    server.send_message(client, json.dumps(msg))

# Called when client disconnects
def client_left(client, server):
    print("❌ Client disconnected:", client['address'])

def run_tag(tag):
    os.system('python /home/nao/.local/share/PackageManager/apps/home11/ars/tag.py --tag {}'.format(tag))
    pass

def command(data):
    threading.Thread(target=lambda: os.system('{} {}'.format(data.get("command_type", ""), data.get("path", "")))).start()
    time.sleep(10)  # Wait for command to finish before allowing new commands




# Called when a message is received
def message_received(client, server, message):
    try:
        data = json.loads(message)
        print("📥 JSON received:", data)

        # Handle commands
        if data.get("type") == "command":
            command(data)
        if data.get("type") == "page_move":
            on_event_page_move(data)
        if data.get("type") == "tag":
            run_tag(data.get("tag", ""))

    except ValueError:
        print("⚠️ Non-JSON received:", message)
        server.send_message(client, "Error: not valid JSON")

# Create server
server = WebsocketServer(port=9001, host='0.0.0.0')
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

print("✅ WebSocket server running on port 9001")
server.run_forever()


