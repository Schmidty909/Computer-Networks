import random
import socket
from _thread import *

server = "192.168.0.4"
port = 55555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, Server Started")


def threaded_client(conn):
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received:", reply)
                print("Sending: ", reply)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost Connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))

# Server side code for Admiral Acknownledgement
# To do:
# 1.) Rewrite code in C++
# 2.) Create board for both players.
# 3.) Receive player movement
#       b.) Verify player input is correct
# 4.) Receive player's torpedo

# gridWidth = 10
# gridLength = 10
# gridOutline = 25
#
# game_grid = []
#
#
# def build_game_grid(array):
#     for x in range(gridWidth):
#         y_grid = []
#         for y in range(gridLength):
#             value = '0'
#             if random.randrange(1, 11) == 10:
#                 value = '#'
#             y_grid.append(value)
#         array.append(y_grid)
#
#     return array
#
#
# def print_game_grid(array):
#     for x in range(gridWidth):
#         for y in range(gridLength):
#             print(array[x][y], end="  ")
#         print()
#
#
# def main():
#     build_game_grid(game_grid)
#     print_game_grid(game_grid)
#
#
# if __name__ == '__main__':
#     main()
