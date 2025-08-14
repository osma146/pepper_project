import time
import os

import argparse
import threading



def test():

    a= """
    time.sleep(30)

    while True:
        try:
            import qi
            from naoqi import ALProxy
            tablet = ALProxy("ALTabletService", "127.0.0.1", 9559)
            break  # success
        except:
            time.sleep(2)  # wait and retry


    # get ip
    parser = argparse.ArgumentParser()
    parser.add_argument("--qi-url", type=str, default="tcp://127.0.0.1:9559")
    args = parser.parse_args()

    # open app session
    app = qi.Application(["home", "--qi-url=" + args.qi_url])
    app.start()
    session = app.session
    """
    # open app
    os.system('qicli call ALTabletService.showWebview "http://198.18.0.1/apps/home9/index.html"')




if __name__ == "__main__":

    t = threading.Thread(target=test)
    t.daemon = True
    t.start()
