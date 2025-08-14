#!/bin/bash
PEPPER_IP=${1:-192.168.0.135}
APP_ID="com.wonder.pepper.temp"

# Show tablet page
ssh nao@$PEPPER_IP "qicli call ALTabletService.showWebview 'http://198.18.0.1/apps/$APP_ID/html/index.html'"

# Start python service in background (screen/nohup)
ssh nao@$PEPPER_IP "nohup python /home/nao/.local/share/PackageManager/apps/$APP_ID/python/service.py --ip 127.0.0.1 >/home/nao/$APP_ID.log 2>&1 &"
echo "[OK] Started."


qicli call ALTabletService.showWebview 'http://198.18.0.1/apps/com.wonder.pepper.temp/index.html'