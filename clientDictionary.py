import socket
import tkinter.dialog

import pygame
import time
import random


import pygame.display
import pygame.mixer_music


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




def build_game_grid():

    for key in game_dictionary.keys():
        for count, index in enumerate(game_dictionary[key]):
            if random.randrange(1, 11) == 10:
                game_dictionary[key][count].color = green
                game_dictionary[key][count].initalcolor = green
                game_dictionary[key][count].island = True


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
    for key in game_dictionary.keys():
        for count,index in enumerate(game_dictionary[key]):
            game_dictionary[key][count].rect = pygame.draw.rect(window, game_dictionary[key][count].color, [game_dictionary[key][count].x, game_dictionary[key][count].y , 100, 100])
    ## Loop to make the seperation between grid pieces
    for x in range(grid_width):
        pygame.draw.rect(window, black, (x * 100 + 50, 0, 2, win_height))
    for y in range(grid_length):
        pygame.draw.rect(window, black, (0, y * 100 + 50, win_height, 2))

def ValidateMovementX(x,key,keylocation,flag):
    global move
    ## moving player left
    if flag == 0:
        ## checking left boundary isn't crossed
        if x - 100 < game_dictionary["a"][0].x:
            return 0
        else:
           if game_dictionary[chr(ord(key)-1)][keylocation].color == red or game_dictionary[chr(ord(key)-1)][keylocation].color == green:
               p.x = x
           else:
               p.x -= 100
               move = False
               game_dictionary[key][keylocation].color = red
               game_dictionary[key][keylocation].initalcolor = red
               p.Key = chr(ord(key) - 1)

    ## moving player right
    else:
        ## checking right boundary isn't crossed
        for k in game_dictionary.keys():
            for count, index in enumerate(game_dictionary[k]):
                None

        if x + 100 > game_dictionary[k][count].x +25:
            return 0
        else:
            if game_dictionary[chr(ord(key) + 1)][keylocation].color == red or game_dictionary[chr(ord(key) + 1)][keylocation].color == green:
                p.x = x
            else:
                p.x +=100
                move = False
                game_dictionary[key][keylocation].color = red
                game_dictionary[key][keylocation].initalcolor = red
                p.Key = chr(ord(key)+1)




def ValidateMovementY(y,key,keylocation,flag):
    global move
    # moving player up
    if flag == 0:
        # checking top boundary
        if y - 100 < game_dictionary["a"][0].y:
            return 0
        else:
            if game_dictionary[key][keylocation-1].color == red or game_dictionary[key][keylocation-1].color == green:
                p.y = y
            else:
                p.y -= 100
                move = False
                game_dictionary[key][keylocation].color = red
                game_dictionary[key][keylocation].initalcolor = red
                p.location = p.location - 1


    # moving player down
    else:
        # checking bottom boundary
        for k in game_dictionary.keys():
            for count, index in enumerate(game_dictionary[k]):
                None
        if y + 100 > game_dictionary[k][count].y +25:
            return 0
        else:
            if game_dictionary[key][keylocation+1].color == red or game_dictionary[key][keylocation+1].color == green:
                p.y = y
            else:
                p.y +=100
                move = False
                game_dictionary[key][keylocation].color = red
                game_dictionary[key][keylocation].initalcolor = red
                p.location = p.location + 1


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





# game_dictionary = {"a": [game_grid(50,50,"a",0),game_grid(50,150,"a",1),game_grid(50,250,"a",2),game_grid(50,350,"a",3),game_grid(50,450,"a",4),game_grid(50,550,"a",5),game_grid(50,650,"a",6),game_grid(50,750,"a",7),game_grid(50,850,"a",8),game_grid(50,950,"a",9)],
#                    "b": [game_grid(150,50,"b",0),game_grid(150,150,"b",1),game_grid(150,250,"b",2),game_grid(150,350,"b",3),game_grid(150,450,"b",4),game_grid(150,550,"b",5),game_grid(150,650,"b",6),game_grid(150,750,"b",7),game_grid(150,850,"b",8),game_grid(150,950,"b",9)],
#                    "c": [game_grid(250,50,"c",0),game_grid(250,150,"c",1),game_grid(250,250,"c",2),game_grid(250,350,"c",3),game_grid(250,450,"c",4),game_grid(250,550,"c",5),game_grid(250,650,"c",6),game_grid(250,750,"c",7),game_grid(250,850,"c",8),game_grid(250,950,"c",9)],
#                    "d": [game_grid(350,50,"d",0),game_grid(350,150,"d",1),game_grid(350,250,"d",2),game_grid(350,350,"d",3),game_grid(350,450,"d",4),game_grid(350,550,"d",5),game_grid(350,650,"d",6),game_grid(350,750,"d",7),game_grid(350,850,"d",8),game_grid(350,950,"d",9)],
#                    "e": [game_grid(450,50,"e",0),game_grid(450,150,"e",1),game_grid(450,250,"e",2),game_grid(450,350,"e",3),game_grid(450,450,"e",4),game_grid(450,550,"e",5),game_grid(450,650,"e",6),game_grid(450,750,"e",7),game_grid(450,850,"e",8),game_grid(450,950,"e",9)],
#                    "f": [game_grid(550,50,"f",0),game_grid(550,150,"f",1),game_grid(550,250,"f",2),game_grid(550,350,"f",3),game_grid(550,450,"f",4),game_grid(550,550,"f",5),game_grid(550,650,"f",6),game_grid(550,750,"f",7),game_grid(550,850,"f",8),game_grid(550,950,"f",9)],
#                    "g": [game_grid(650,50,"g",0),game_grid(650,150,"g",1),game_grid(650,250,"g",2),game_grid(650,350,"g",3),game_grid(650,450,"g",4),game_grid(650,550,"g",5),game_grid(650,650,"g",6),game_grid(650,750,"g",7),game_grid(650,850,"g",8),game_grid(650,950,"g",9)],
#                    "h": [game_grid(750,50,"h",0),game_grid(750,150,"h",1),game_grid(750,250,"h",2),game_grid(750,350,"h",3),game_grid(750,450,"h",4),game_grid(750,550,"h",5),game_grid(750,650,"h",6),game_grid(750,750,"h",7),game_grid(750,850,"h",8),game_grid(750,950,"h",9)],
#                    "i": [game_grid(850,50,"i",0),game_grid(850,150,"i",1),game_grid(850,250,"i",2),game_grid(850,350,"i",3),game_grid(850,450,"i",4),game_grid(850,550,"i",5),game_grid(850,650,"i",6),game_grid(850,750,"i",7),game_grid(850,850,"i",8),game_grid(850,950,"i",9)],
#                    "j": [game_grid(950,50,"j",0),game_grid(950,150,"j",1),game_grid(950,250,"j",2),game_grid(950,350,"j",3),game_grid(950,450,"j",4),game_grid(950,550,"j",5),game_grid(950,650,"j",6),game_grid(950,750,"j",7),game_grid(950,850,"j",8),game_grid(950,950,"j",9)]
# }

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
    generate_dictionary()
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

    build_game_grid()

    while Selection:
        clock.tick(30)

        print_game_grid()  ##Drawing inital grid
        # if pygame.mixer.music.get_busy() == False:
        #     pygame.mixer_music.play()

        for key in game_dictionary.keys():
            for count, index in enumerate(game_dictionary[key]):
                game_grid.hover(game_dictionary[key][count])

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Selection = False
                run = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
                if window.get_at(pygame.mouse.get_pos()) == red:
                    Selection = False

                    game_dictionary[Key][KeyPosition].color = ocean_blue
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
            for key in game_dictionary.keys():
                for count, index in enumerate(game_dictionary[key]):
                    game_grid.Fire(game_dictionary[key][count])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if window.get_at(pygame.mouse.get_pos()) == red:
                    print(f"{FireKey}{FireLocation}")
                    if game_dictionary[FireKey][FireLocation].initalcolor == red:
                        game_dictionary[FireKey][FireLocation].color = red
                        pygame.display.update()
                    else:
                        game_dictionary[FireKey][FireLocation].color = ocean_blue
                        pygame.display.update()

                    move = True

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()



main()

