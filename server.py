import socket
from _thread import *
import pickle
from game import Game
# updated code

grey = (128, 128, 128)

server = "192.168.0.8"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started")


gameLogic = Game()

def threaded_client(conn, playerCount):
    conn.send(str.encode(str(playerCount)))
    reply = ""
    while True:
        try:
            # Read the object sent to us
            data = conn.recv(2048 * 4).decode("latin-1")
            print(data)
            # Store the object we received into our array
            if not data:
                print("Disconnected")
                break
            else:
                if data == "game":
                    reply = gameLogic
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
