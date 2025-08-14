# -*- coding: utf-8 -*-
from naoqi import ALProxy

def raise_event(ip, name, payload=""):
    mem = ALProxy("ALMemory", ip, 9559)
    mem.raiseEvent(name, payload)
