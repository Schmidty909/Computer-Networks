import pygame
import json
import socket
from _thread import *
import sys
import jsonpickle
game_dictionary = {}
grid_width = 10
grid_length = 10

white = [255, 255, 255]
red = (255, 0, 0)
green = (0, 255, 0)
ocean_blue = (0, 130, 150)
grey = (128, 128, 128)
black = (0, 0, 0)

server= "192.168.1.133"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server,port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for connection, server started")

def generate_dictionary():
    list = []
    character = 97

    for x in range(grid_width + 1):
        game_dictionary[chr(character)] = list
        list = []
        position = 0
        character = 97
        character += x
        for y in range(grid_length ):
            list.append(game_grid(x* 100 + 50, y * 100 + 50, chr(character), position))
            position += 1


class game_grid():

    def __init__(self,x,y,key,location):
        self.x = x
        self.y = y
        self.key = key
        self.location = location
        self.color = ocean_blue
        self.initalcolor = ocean_blue
        self.island = False

def threaded_client(conn):
    print(game_dictionary)
    jsonStr = jsonpickle.encode(game_dictionary)

    conn.send(str.encode(jsonStr))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")
            if not data:
                print("Disconnected")
                break
            else:
                print("Recevied: ", reply)
                print("Sending: ",reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost Connection")
    conn.close()


generate_dictionary()
while True:
    conn, addr = s.accept()
    print("Connnected to:",addr)

    start_new_thread(threaded_client, (conn,))






# import random
# import socket
# from _thread import *
#
# server = "192.168.0.4"
# port = 55555
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#
# try:
#     s.bind((server, port))
# except socket.error as e:
#     str(e)
#
# s.listen(2)
# print("Waiting for connection, Server Started")
#
#
# def threaded_client(conn):
#     reply = ""
#     while True:
#         try:
#             data = conn.recv(2048)
#             reply = data.decode("utf-8")
#
#             if not data:
#                 print("Disconnected")
#                 break
#             else:
#                 print("Received:", reply)
#                 print("Sending: ", reply)
#
#             conn.sendall(str.encode(reply))
#         except:
#             break
#
#     print("Lost Connection")
#     conn.close()
#
# while True:
#     conn, addr = s.accept()
#     print("Connected to:", addr)
#
#     start_new_thread(threaded_client, (conn,))

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
