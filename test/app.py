#! /usr/bin/env python
# -*- encoding: UTF-8 -*-

"""Example: Use loadApplication Method"""

import qi
import argparse
import sys
import time



def main(session):
    """
    This example uses the loadApplication method.
    To Test ALTabletService, you need to run the script ON the robot.
    """
    # Get the service ALTabletService.

    try:
        tabletService = session.service("ALTabletService")

        # Display the index.html page of a behavior name j-tablet-browser
        # The index.html must be in a folder html in the behavior folder
        tabletService.loadApplication(args.app)
        tabletService.showWebview()

        

        while True:
            inp = input("Press 'q' then Enter to close the webview: ")
            if inp.strip().lower() == 'q':
                break

        tabletService.hideWebview()

    except Exception as e:
        print ("Error was: ", e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")
    parser.add_argument("--app", type=str, default="myapp",
                        help="Name of the application to load on the tablet")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)