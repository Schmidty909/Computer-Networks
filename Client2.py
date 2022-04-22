import socket
import tkinter.dialog

import pygame

import time
import random
from network import Network
import pygame.display
import pygame.mixer_music
import jsonpickle
global board

pygame.init()

win_width = 1100
win_height = 1100

playerX = 0
playerY = 0
Key = "a"
KeyPosition = 0
move = True
game_dictionary= {}

white = [255, 255, 255]
red = (255, 0, 0)
green = (0, 255, 0)
ocean_blue = (0, 130, 150)
grey = (128, 128, 128)
black = (0, 0, 0)


window = pygame.display.set_mode((win_width, win_height))

##DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

font = pygame.font.Font('cour.ttf', 40)

clientNumber = 0
# width can't be greater then 26
# Length can't be greater then 9
grid_width = 10
grid_length = 10

class Button():
    def __init__(self,x,y,width,height, text,color,background):
        self.x = x
        self. y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.initalcolor = grey
        self.background = background
        self.rect = (x, y, width, height)
    def draw(self):
        self.rect = pygame.draw.rect(window, self.color, [self.x - 50, self.y, 200, 50])
    def hover(self,color):
        position = pygame.mouse.get_pos()
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,self.rect.bottom):
            self.color = color
            window.blit(start, startRect)
            window.blit(text, textRect)
            window.blit(Quit, QuitRect)

        else:
            self.color = self.initalcolor
            window.blit(start, startRect)
            window.blit(text, textRect)
            window.blit(Quit, QuitRect)


class game_grid():

    def __init__(self,x,y,key,location):
        self.x = x
        self.y = y
        self.key = key
        self.location = location
        self.color = ocean_blue
        self.initalcolor = ocean_blue
        self.rect = pygame.draw.rect(window, self.color, [self.x, self.y , 100, 100])
        self.island = False
    def hover(self):
        global playerX
        global playerY
        global Key
        global KeyPosition
        position = pygame.mouse.get_pos()
        if position[0] in range(self.rect.left,self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if(self.color != green):
                self.color = red
                Key = self.key
                KeyPosition = self.location
                playerX = self.x
                playerY = self.y
        else:
            self.color = self.initalcolor

    def Fire(self):
        global FireKey
        global FireLocation

        Fireposition = pygame.mouse.get_pos()
        if Fireposition[0] in range(self.rect.left,self.rect.right) and Fireposition[1] in range(self.rect.top, self.rect.bottom):
            if(self.color != green):
                self.color = red
                FireKey = self.key
                FireLocation = self.location


        else:
            self.color = self.initalcolor

def print_game_grid():
    ## Loops to make Row and Column headers
    counter = 85
    top_character = 65
    for x in range(grid_width):
        top_row_letters = font.render(chr(top_character), True, grey)
        window.blit(top_row_letters, (counter, 0))
        counter += 100
        top_character += 1

    counter = 80
    side_numbers = 48
    for y in range(grid_length ):
        side_row_numbers = font.render(chr(side_numbers), True, grey)
        window.blit(side_row_numbers, (5, counter))
        counter += 100
        side_numbers += 1
    ## Loops to make square pieces
    for key in board.keys():
        for count,index in enumerate(board[key]):
            board[key][count].rect = pygame.draw.rect(window, board[key][count].color, [board[key][count].x, board[key][count].y , 100, 100])
    ## Loop to make the seperation between grid pieces
    for x in range(grid_width):
        pygame.draw.rect(window, black, (x * 100 + 50, 0, 2, win_height))
    for y in range(grid_length):
        pygame.draw.rect(window, black, (0, y * 100 + 50, win_height, 2))



class Player():
    def __init__(self,x,y,key, keylocation, width, height, color):
        self.x = x
        self.y = y
        self.Key = key
        self.location = keylocation
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 20


    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)


    def move(self):
        keys = pygame.key.get_pressed()
        global move

        if keys[pygame.K_LEFT]:
           ValidateMovementX(self.x,self.Key,self.location,0)

        if keys[pygame.K_RIGHT]:
             ValidateMovementX(self.x,self.Key, self.location,1)


        if keys[pygame.K_UP]:
            ValidateMovementY(self.y,self.Key, self.location,0)


        if keys[pygame.K_DOWN]:
            ValidateMovementY(self.y,self.Key, self.location,1)


        self.rect = (self.x , self.y, self.width, self.height)


def ValidateMovementX(x,key,keylocation,flag):
    global move
    ## moving player left
    if flag == 0:
        ## checking left boundary isn't crossed
        if x - 100 < board["a"][0].x:
            return 0
        else:
           if board[chr(ord(key)-1)][keylocation].color == red or board[chr(ord(key)-1)][keylocation].color == green:
               p.x = x
           else:
               p.x -= 100
               move = False
               board[key][keylocation].color = red
               board[key][keylocation].initalcolor = red
               p.Key = chr(ord(key) - 1)

    ## moving player right
    else:
        ## checking right boundary isn't crossed
        for k in board.keys():
            for count, index in enumerate(board[k]):
                None

        if x + 100 > board[k][count].x +25:
            return 0
        else:
            if board[chr(ord(key) + 1)][keylocation].color == red or board[chr(ord(key) + 1)][keylocation].color == green:
                p.x = x
            else:
                p.x +=100
                move = False
                board[key][keylocation].color = red
                board[key][keylocation].initalcolor = red
                p.Key = chr(ord(key)+1)




def ValidateMovementY(y,key,keylocation,flag):
    global move
    # moving player up
    if flag == 0:
        # checking top boundary
        if y - 100 < board["a"][0].y:
            return 0
        else:
            if board[key][keylocation-1].color == red or board[key][keylocation-1].color == green:
                p.y = y
            else:
                p.y -= 100
                move = False
                board[key][keylocation].color = red
                board[key][keylocation].initalcolor = red
                p.location = p.location - 1


    # moving player down
    else:
        # checking bottom boundary
        for k in board.keys():
            for count, index in enumerate(board[k]):
                None
        if y + 100 > board[k][count].y +25:
            return 0
        else:
            if board[key][keylocation+1].color == red or board[key][keylocation+1].color == green:
                p.y = y
            else:
                p.y +=100
                move = False
                board[key][keylocation].color = red
                board[key][keylocation].initalcolor = red
                p.location = p.location + 1







def main_menu():

    global win_width
    global win_height
    global  start, startRect, text, textRect, Quit, QuitRect
    pygame.display.set_mode((win_width, win_height))
    pygame.display.set_caption("Menu")

    text = font.render("Admiral Acknowledge", True, white)
    textRect = text.get_rect()
    textRect.center = (win_width // 2, win_height // 2 - 180)

    start = font.render("Start", True, white)
    startRect = start.get_rect()
    startRect.center = (win_width // 2 -25 , win_height // 2 - 100)

    Quit = font.render("Quit", True, white)
    QuitRect = Quit.get_rect()
    QuitRect.center = (win_width // 2 -25, win_height // 2-25 )



def mainSelection():
    StartButton.hover(ocean_blue)
    QuitButton.hover(red)

    pygame.display.update()

def fade(width, height):
    window.fill((0,0,0))
    for alpha in range(0, 300):
        window.set_alpha(alpha)
        window.blit(window, (0,0))
        pygame.display.update()
        pygame.time.delay(5)

def main():
    n = Network()

    global board
    board = n.Board()
    board = jsonpickle.loads(board)

    print("This is the board: " , board)


    global playercount
    playercount = n.send("Count")
    print(playercount)




    main = True
    run = True
    Selection = True
    clock = pygame.time.Clock()
    global  StartButton
    global QuitButton
    StartButton = Button(470, 425, win_width, win_height, "Start", white, grey)
    QuitButton = Button(470, 500, win_width, win_height, "Quit", white, grey)
    # # # Starting the mixer
    # pygame.mixer.init()
    #
    # # Loading the song
    # pygame.mixer.music.load("VaughnSlow.mp3")
    #
    # # Setting the volume
    # pygame.mixer.music.set_volume(0.7)
    #
    # # # Start playing the song
    # pygame.mixer.music.play()

    while main:

        clock.tick(50)
        # if pygame.mixer.music.get_busy() == False:
        #     pygame.mixer_music.play()

        main_menu()
        StartButton.draw()
        QuitButton.draw()

        mainSelection()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main = False
                Selection = False
                run = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if window.get_at(pygame.mouse.get_pos()) == ocean_blue:
                    main = False
                    pygame.display.update()
                    fade(win_width, win_height)
                if window.get_at(pygame.mouse.get_pos()) == red:

                    main = False
                    Selection = False
                    run = False
                    pygame.quit()



    # # # Starting the mixer
    # pygame.mixer.init()
    #
    # # Loading the song
    # pygame.mixer.music.load("cg5.mp3")
    #
    # # Setting the volume
    # pygame.mixer.music.set_volume(0.7)
    #
    # # # Start playing the song
    # pygame.mixer.music.play()

    pygame.display.set_caption("Captain Admiral")


    while Selection:
        clock.tick(30)

        print_game_grid()  ##Drawing inital grid
        # if pygame.mixer.music.get_busy() == False:
        #     pygame.mixer_music.play()

        for key in board.keys():
            for count, index in enumerate(board[key]):
                game_grid.hover(board[key][count])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Selection = False
                run = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if window.get_at(pygame.mouse.get_pos()) == red:
                    Selection = False

                    board[Key][KeyPosition].color = ocean_blue
                    pygame.display.update()

                else:
                    Selection = True


    global p
    global move
    p = Player(playerX +25, playerY +25, Key, KeyPosition, 50, 50, grey)

    while run:
        # if pygame.mixer.music.get_busy() == False:
        #     pygame.mixer_music.play()
        clock.tick(30)
        print_game_grid() ##Drawing inital grid
        p.draw(window) ##Drawing player on grid
        if move == True:
            p.move() ## Movement for player
        else:
            for key in board.keys():
                for count, index in enumerate(board[key]):
                    game_grid.Fire(board[key][count])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if window.get_at(pygame.mouse.get_pos()) == red:
                    print(f"{FireKey}{FireLocation}")
                    if board[FireKey][FireLocation].initalcolor == red:
                        board[FireKey][FireLocation].color = red
                        pygame.display.update()
                    else:
                        board[FireKey][FireLocation].color = ocean_blue
                        pygame.display.update()

                    move = True

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()



main()

