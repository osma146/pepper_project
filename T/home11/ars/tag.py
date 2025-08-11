#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import argparse
from naoqi import ALProxy

def main():
    parser = argparse.ArgumentParser(description="Play tag animation on Pepper.")
    parser.add_argument("--tag", type=str, required=True, help="Tag name to play")
    args = parser.parse_args()

    tag_name = args.tag

    try:
        motion = ALProxy("ALAnimationPlayer", "127.0.0.1", 9559)
        print("[INFO] Playing tag:", tag_name)
        motion.runTag(tag_name)
        print("[INFO] Done.")
    except Exception as e:
        print("[ERROR] Failed to play tag:", e)

if __name__ == "__main__":
    main()
