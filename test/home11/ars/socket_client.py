import audioop, base64, json, time
import threading
from Queue import Queue, Empty

class SocketClient(object):
    IN_RATE = 48000
    OUT_RATE = 24000

    def __init__(self, ws_app):
        self.ws_app = ws_app
        self.send_q = Queue()
        t = threading.Thread(target=self._sender_loop)
        t.daemon = True
        t.start()

    def _sender_loop(self):
        while True:
            try:
                event_name, raw = self.send_q.get(timeout=1)
            except Empty:
                continue
            # time.sleep(0.3)
            raw_bytes = str(raw) if isinstance(raw, bytearray) else raw
            try:
                pcm24k, _ = audioop.ratecv(raw_bytes, 2, 1,
                                           self.IN_RATE, self.OUT_RATE, None)
            except Exception as e:
                print "resample error", e
                continue
            b64 = base64.b64encode(pcm24k).decode('ascii')
            payload = {"type": event_name, "audio": b64}
            message = json.dumps(payload)
            try:
                self.ws_app.send(message)
            except Empty:
                try:
                    self.ws_app.close()
                except:
                    pass
                time.sleep(3)
                self.reconnect_to_cloud()
               
                continue
         
            # print(message)
    def send_audio(self, event_name, raw):
        self.send_q.put((event_name, raw))

    def reconnect_to_cloud(self):
       
        try:
            self.ws_app.close()
        except Exception as e:
            print("eroor disconnect", e)
 
        connected = False
        for _ in range(5):  
            try:
                ws_new = websocket.WebSocket()
                ws_new.connect(WS_URL, header=WS_HEADERS)
                self.ws_app = ws_new
                print("eroor connect")
                connected = True
                break
            except Exception as e:
                print("eroor connect",e)
                time.sleep(3)
        if not connected:
           print('eroor connect')

    def send_update_event(self, ws):
        event = {
            "type": "session.update",
            "session": {
                "turn_detection": {
                    "type": "server_vad",
        
                    "threshold": 0.5,
                  
                    "silence_duration_ms": 100,
                    "interrupt_response": True,
                    "create_response": True
                },
                "input_audio_noise_reduction": {
                    "type": "far_field"
                }
            }
        }
    try:
        ws.send(json.dumps(event))
    except Exception as e:
        print("Failed to send session.update event:", e)