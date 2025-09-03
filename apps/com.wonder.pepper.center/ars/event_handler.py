import os
import json
import random
import threading
import time
from ars import event_handler




def move_to_app(data):
    value = data.get("App_destination", "")
    if value != "":
        version = random.randint(1, 9999)
        url = 'http://198.18.0.1/apps/home11/{}.html?version={}'.format(value.strip(), version)
        os.system('qicli call ALTabletService.showWebview "{}"'.format(url))

def run_tag(tag):
    os.system('python /home/nao/.local/share/PackageManager/apps/home11/ars/tag.py --tag {}'.format(tag))
    pass

def command(data):
    threading.Thread(target=lambda: os.system('{} {}'.format(data.get("command_type", ""), data.get("path", "")))).start()
    time.sleep(10)  # Wait for command to finish before allowing new commands

