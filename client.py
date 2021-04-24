from pynput import keyboard
from json import dumps
from socket import socket, AF_INET, SOCK_STREAM
from sys import argv

address = argv[1]

with socket(AF_INET, SOCK_STREAM) as sock:
    def on_press(key):
        data = dumps(
            {"command": "press", "keycode": _get_keycode(key)}) + "\n"
        sock.sendall(data.encode())

    def on_release(key):
        data = dumps(
            {"command": "release", "keycode": _get_keycode(key)}) + "\n"
        sock.sendall(data.encode())

    def _get_keycode(key):
        try:
            return key.value.vk
        except AttributeError:
            return key.vk

    sock.connect((address, 8000))

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except Exception as e:
            print(e)