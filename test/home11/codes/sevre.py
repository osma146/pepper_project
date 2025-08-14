import paramiko

PEPPER_IP = "192.168.0.135"
PEPPER_USER = "nao"
PEPPER_PASSWORD = "1234"
REMOTE_PATH = "/home/nao/.local/share/PackageManager/apps/home11/event.py"

# Use correct Python binary with NAOqi support
COMMAND = f"/usr/bin/python2.7 {REMOTE_PATH}"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(PEPPER_IP, username=PEPPER_USER, password=PEPPER_PASSWORD)

stdin, stdout, stderr = ssh.exec_command("env")
print(stdout.read().decode())

