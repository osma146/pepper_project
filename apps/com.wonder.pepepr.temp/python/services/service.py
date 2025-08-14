# -*- coding: utf-8 -*-
import qi, argparse, sys, time

APP_ID = "com.wonder.pepper.temp"
EV_SAY = "com/wonder/pepper/temp/say"
EV_TOGGLE = "com/wonder/pepper/temp/toggle_audio"

class TemplateService(object):
    def __init__(self, session):
        self.session = session
        self.mem = session.service("ALMemory")
        self.tts = session.service("ALTextToSpeech")
        # subscribers
        self.mem.subscriber(EV_SAY).signal.connect(self.on_say)
        self.mem.subscriber(EV_TOGGLE).signal.connect(self.on_toggle)
        self.audio_enabled = False

    def on_say(self, data):
        try:
            text = data if isinstance(data, basestring) else "Hello"
            self.tts.say(text)
        except Exception as e:
            print("[ERR] on_say:", e)

    def on_toggle(self, _):
        self.audio_enabled = not self.audio_enabled
        print("[INFO] audio_enabled =", self.audio_enabled)

def main(ip="198.18.0.1", port=9559):
    app = qi.Application(["TemplateService", "--qi-url=tcp://%s:%d" % (ip, port)])
    app.start()
    session = app.session
    TemplateService(session)
    print("[INFO] TemplateService running. Ctrl+C to exit.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="198.18.0.1")
    parser.add_argument("--port", type=int, default=9559)
    args = parser.parse_args()
    main(args.ip, args.port)
