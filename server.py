from player import Player
import socket
from _thread import *
import pickle
# updated code

grey = (128, 128, 128)

server = "192.168.1.133"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started")


class gameLogic:
    def __init__(self):
        self.p1Went = False
        self.p2Went = True
        self.playerCoords = [" ", " "]
        self.playerHits = [" ", " "]
        self.player1moves = []
        self.player2moves = []
        self.ready = False


players = [Player(0, 0, "a", 9 , 50, 50, grey), Player(0, 0, "a", 10, 50, 50, grey)]


def threaded_client(conn, playerCount):
    conn.send(pickle.dumps(players[playerCount]))
    reply = ""
    while True:
        try:
            # Read the object sent to us
            data = pickle.loads(conn.recv(2048))
            # Store the object we received into our array
            players[playerCount] = data
            if not data:
                print("Disconnected")
                break
            else:
                if playerCount == 1:
                    reply = players[0]
                else:
                    reply = players[1]
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost Connection")
    conn.close()


currentPlayer = 0


while True:
    conn, addr = s.accept()
    print("Connnected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    if currentPlayer > 1:
        currentPlayer = 0
