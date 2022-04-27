from player import Player
import socket
from _thread import *
import pickle
# updated code

grey = (128, 128, 128)

server = "192.168.0.8"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen()
print("Waiting for connection, server started")


class game:
    def __init__(self):
        self.p1Turn = True
        self.p2Turn = False
        self.playerCoords = [" ", " "]
        self.playerHits = [" ", " "]
        self.player1moves = []
        self.player2moves = []
        self.winner = -1

Game = game()
players = [Player(0, 0, "a", 9, 50, 50, grey), Player(0, 0, "a", 9, 50, 50, grey)]


def threaded_client(conn, playerCount):
    conn.send(pickle.dumps(players[playerCount]))
    reply = ""
    while True:
        try:
            # Read the object sent to us
            data = pickle.loads(conn.recv(30000))
            players[playerCount] = data
            # Store the object we received into our array
            if not data:
                print("Disconnected")
                break
            else:
                if players[0].move == False and players[0].Fired == True:
                    players[1].move = True
                    players[1].Fired = False
                    reply = players[1]
                if players[1].move == False and players[1].Fired == True:
                    players[0].move = True
                    players[0].Fired = False
                    reply = players[0]
                # if playerCount == 0 and players[1].ourTurn == False:
                #     players[0].ourTurn = False
                #     players[1].ourTurn = True
                #     Game.playerCoords[0] = players[0].position
                #     Game.playerHits[0] = players[0].hit
                #     players[0].playerid = 0
                #     if Game.playerHits[0] == Game.playerCoords[1]:
                #         Game.p1Turn = False
                #         Game.p2Turn = False
                #         Game.winner = 0
                #         players[0].winner = True
                #     reply = players[0]
                # if playerCount == 1 and players[0].ourTurn == False:
                #     players[1].ourTurn = False
                #     players[0].ourTurn = True
                #     Game.playerCoords[1] = players[1].position
                #     Game.playerHits[1] = players[1].hit
                #     players[1].playerid = 1
                #     if Game.playerHits[1] == Game.playerCoords[0]:
                #         players[1].winner = True
                #     reply = players[1]
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
