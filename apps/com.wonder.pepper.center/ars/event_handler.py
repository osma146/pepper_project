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