import socket
import json

class QGAConnection(object):
    handler = None

    def __init__(self, filename):
        if self.handler is None:
            self.connect(filename)

    def __del__(self):
        if self.handler is not None:
            self.close()

    def close(self):
        self.handler.close()

    def connect(self, filename):
        address = filename
        self.handler = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.handler.connect(address)

    def recieve(self):
        result = self.handler.recv(1<<12)
        return json.loads(result)

    def send(self, command):
        self.handler.send(json.dumps(command))
