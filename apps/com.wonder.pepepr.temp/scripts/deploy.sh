#!/bin/bash
set -e
PEPPER_IP=${1:-192.168.0.135}
APP_ID="com.wonder.pepper.temp"

echo "[INFO] Deploying to $PEPPER_IP"
ssh nao@$PEPPER_IP "mkdir -p /home/nao/.local/share/PackageManager/apps/$APP_ID"
scp -r html python manifest.xml package.ini nao@$PEPPER_IP:/home/nao/.local/share/PackageManager/apps/$APP_ID/
echo "[OK] Deployed."
