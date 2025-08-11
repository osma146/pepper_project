import paramiko

PEPPER_IP = "192.168.0.135"
PEPPER_USER = "nao"
PEPPER_PASSWORD = "nao"
REMOTE_PATH = "/home/nao/.local/share/PackageManager/apps/home11/event.py"

COMMAND = (
    "PYTHONPATH=/opt/aldebaran/lib/python2.7/site-packages "
    f"/usr/bin/python2.7 {REMOTE_PATH}"
)

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(PEPPER_IP, username=PEPPER_USER, password=PEPPER_PASSWORD)

stdin, stdout, stderr = ssh.exec_command(COMMAND)

print("[OUTPUT]")
print(stdout.read().decode())
print("[ERROR]")
print(stderr.read().decode())

ssh.close()
