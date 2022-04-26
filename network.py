import json
import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "75.187.185.215"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.board = self.connect()

    def getBoard(self):
        return self.board

    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(30000))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(1024).decode("latin-1")
        except socket.error as e:
            print(e)
