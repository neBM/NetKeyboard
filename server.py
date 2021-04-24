from pynput import keyboard
from socketserver import StreamRequestHandler, TCPServer
from json import loads

controller = keyboard.Controller()


class Handler(StreamRequestHandler):
    def handle(self):
        while True:
            m = self.rfile.readline().strip().decode()
            m = loads(m)
            key = keyboard.KeyCode.from_vk(m["keycode"])
            if m["command"] == "press":
                controller.press(key)
            elif m["command"] == "release":
                controller.release(key)


with TCPServer(("", 8000), Handler) as server:
    server.serve_forever()
