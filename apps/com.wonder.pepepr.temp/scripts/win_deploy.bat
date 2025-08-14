@echo off
set PEPPER_IP=192.168.0.135
set APP_ID=com.wonder.pepper.temp
pscp -r html python manifest.xml package.ini nao@%PEPPER_IP%:/home/nao/.local/share/PackageManager/apps/%APP_ID%/
