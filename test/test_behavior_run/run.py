from naoqi import ALProxy

ip, port = "192.168.0.135", 9559
mgr = ALProxy("ALBehaviorManager", ip, port)

behavior_name = "untitled-faea0e/behavior_1"

if mgr.isBehaviorInstalled(behavior_name):
    mgr.runBehavior(behavior_name)
    print("[OK] Behavior launched:", behavior_name)
else:
    print("[ERR] Behavior not found:", behavior_name)
