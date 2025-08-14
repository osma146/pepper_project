#!/bin/bash
set -e
cd behavior/unpacked_xar
zip -r ../behavior.xar *
echo "[OK] behavior.xar packed."
