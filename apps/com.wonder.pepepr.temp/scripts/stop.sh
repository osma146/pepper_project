#!/bin/bash
PEPPER_IP=${1:-192.168.0.135}
APP_ID="com.wonder.pepper.temp"
ssh nao@$PEPPER_IP "pkill -f '$APP_ID/python/service.py' || true"
echo "[OK] Stopped."
