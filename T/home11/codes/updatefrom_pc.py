import os
import shutil
import time
import tempfile

pepper_ip = "192.168.0.135"
source_folder = r"C:\Users\jeffh\OneDrive\Desktop\pepper\main2\home10"  # your real content folder
remote_path = "/home/nao/apps/"
temp_name = "upload_" + str(int(time.time()))

# Use a clean global temp directory (not under OneDrive)
temp_root = os.path.join(os.environ['TEMP'], "pepper_temp")
os.makedirs(temp_root, exist_ok=True)

# Copy source folder to a fresh temp location
temp_local = os.path.join(temp_root, temp_name)
if os.path.exists(temp_local):
    shutil.rmtree(temp_local)
shutil.copytree(source_folder, temp_local)

# Use relative path for scp (safe on Windows terminals)
upload_cmd = f'scp -r "{temp_local}" nao@{pepper_ip}:{remote_path}'
print("[INFO] Uploading:", upload_cmd)
os.system(upload_cmd)

# Launch the HTML app
webview_cmd = f'ssh nao@{pepper_ip} "qicli call ALTabletService.showWebview http://198.18.0.1/apps/{temp_name}/index.html"'
print("[INFO] Launching webview:", webview_cmd)
os.system(webview_cmd)

# Clean up temp folder
try:
    shutil.rmtree(temp_local)
    print("[INFO] Temp folder deleted.")
except Exception as e:
    print("[WARN] Failed to delete temp folder:", e)
