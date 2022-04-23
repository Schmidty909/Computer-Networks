import pygame
import socket
import random
from _thread import *
import sys
import pickle
game_dictionary = {}
grid_width = 10
grid_length = 10

white = [255, 255, 255]
red = (255, 0, 0)
green = (0, 255, 0)
ocean_blue = (0, 130, 150)
grey = (128, 128, 128)
black = (0, 0, 0)

server= "192.168.1.99"
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
def build_game_grid():

    for key in game_dictionary.keys():
        for count, index in enumerate(game_dictionary[key]):
            if random.randrange(1, 11) == 10:
                game_dictionary[key][count].color = green
                game_dictionary[key][count].initalcolor = green
                game_dictionary[key][count].island = True

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
    conn.send(pickle.dumps(game_dictionary))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(20000))
            reply = " "
            if not data:
                print("Disconnected")
                break
            else:
                print("Recevied: ", reply)
                print("Sending: ",reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print("Lost Connection")
    conn.close()


generate_dictionary()
build_game_grid()
while True:
    conn, addr = s.accept()
    print("Connnected to:",addr)

    start_new_thread(threaded_client, (conn,))
