def ALProxy(name, ip, port):
    """
    Mock function to simulate ALProxy behavior.
    In a real scenario, this would connect to the NAOqi service.
    """
    print(f"Connecting to {name} at {ip}:{port}")
    return {
        "ALSystem": lambda: {"systemVersion": lambda: "1.0.0"},
        "ALMemory": lambda: {"getDataListName": lambda: ["key1", "key2", "key3"]},
        "ALBehaviorManager": lambda: {
            "getInstalledBehaviors": lambda: ["test_behavior_run/behavior_1", "other_behavior"]
        }
    }[name]()