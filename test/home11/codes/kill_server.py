import os

pepper_ip = "192.168.0.135"

def is_server_running():
    check_cmd = f'ssh nao@{pepper_ip} "pgrep -f event.py"'
    return os.system(check_cmd) == 0

def stop_server():
    stop_cmd = f'ssh nao@{pepper_ip} "pkill -f event.py"'
    return os.system(stop_cmd) == 0

if is_server_running():
    print("[INFO] Stopping server...")
    success = stop_server()
    if success:
        print("[SUCCESS] Server stopped.")
    else:
        print("[ERROR] Failed to stop server.")
else:
    print("[INFO] Server is not running.")
