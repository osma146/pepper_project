import paramiko
import threading
import random
import time
import os

pepper_ip = "192.168.0.135"
pepper_user = "nao"
pepper_password = "1234"
version = random.randint(1, 9999)

event_py_path = "/home/nao/.local/share/PackageManager/apps/home11/event.py"
python_path = "/usr/bin/python2.7"
naoqi_path = "/opt/aldebaran/lib/python2.7/site-packages"
log_file = "/home/nao/event.log"
webview_url = f"http://198.18.0.1/apps/home11/index.html?version={version}"


def ssh_connect():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(pepper_ip, username=pepper_user, password=pepper_password)
    return ssh


def is_server_running():
    try:
        ssh = ssh_connect()
        stdin, stdout, stderr = ssh.exec_command("pgrep -f event.py")
        result = stdout.read().decode().strip()
        ssh.close()
        return bool(result)
    except Exception as e:
        print("[ERROR] Could not check server:", e)
        return False


def run_server():
    try:
        ssh = ssh_connect()
        command = (
            f"bash -lc 'PYTHONPATH={naoqi_path} "
            f"{python_path} {event_py_path} > {log_file} 2>&1 &'"
        )
        ssh.exec_command(command)
        ssh.close()
    except Exception as e:
        print("[ERROR] Could not start server:", e)


def launch_webview():
    try:
        cmd = (
            f'ssh nao@{pepper_ip} '
            f'"bash -lc \\"qicli call ALTabletService.showWebview '
            f'{webview_url}\\" "'
        )
        os.system(cmd)
    except Exception as e:
        print("[ERROR] Could not launch webview:", e)


# Main logic
if not is_server_running():
    print("[INFO] Starting server...")
    threading.Thread(target=run_server).start()
    time.sleep(1)  # Give time for server to start
else:
    print("[INFO] Server already running.")

print("[INFO] Launching webview...")
launch_webview()
