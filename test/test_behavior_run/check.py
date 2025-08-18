# Python 2.7 (run from your PC with naoqi python SDK or on Pepper)
from naoqi import ALProxy
IP, PORT = "192.168.0.135", 9559  # robot's CPU IP
system = ALProxy("ALSystem", IP, PORT)
print(system.systemVersion())

# Python 2.7
from naoqi import ALProxy

IP, PORT = "127.0.0.1", 9559   # or your robot IP
mem = ALProxy("ALMemory", IP, PORT)
names = mem.getDataListName()   # <-- no args
print(len(names), "memory keys")


# Python 2.7
from naoqi import ALProxy
IP, PORT = "127.0.0.1", 9559   # or your robot IP

mgr = ALProxy("ALBehaviorManager", IP, PORT)
installed = mgr.getInstalledBehaviors()
print("[COUNT]", len(installed))
for b in installed:
    if b.startswith("test_behavior_run/") or "behavior_1" in b:
        print(" ->", b)