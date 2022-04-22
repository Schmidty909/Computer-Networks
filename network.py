import json
import socket

import jsonpickle

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "192.168.1.133"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print(self.id)
    def Board(self):
        return self.id
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(20000).decode()

        except:
            pass
    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(20000).decode()
        except socket.error as e:
            print(e)

n = Network()

