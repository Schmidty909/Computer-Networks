import socket
import pygame
import time
import random


pygame.init()

win_width = 1100
win_height = 1100

playerX = 0
playerY = 0
KEY = "a"

red = (255, 0, 0)
green = (0, 255, 0)
ocean_blue = (0, 130, 150)
grey = (128, 128, 128)
black = (0, 0, 0)

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Captain Admiral")



font = pygame.font.Font('cour.ttf', 40)

clientNumber = 0

grid_width = 10
grid_length = 10




class game_grid():

    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = ocean_blue
        self.initalcolor = ocean_blue
        self.rect = pygame.draw.rect(window, self.color, [self.x, self.y , 100, 100])
        self.island = False
        self.has_player = False
        self.already_been_here = False
    def changeColor(self):
        global playerX
        global playerY
        global Key
        position = pygame.mouse.get_pos()
        if position[0] in range(self.rect.left,self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if(self.color != green):
                self.color = red
            playerX = self.x
            playerY = self.y

        else:
            self.color = self.initalcolor




class Player():
    def __init__(self,x,y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.vel = 20


    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)


    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= 100

        if keys[pygame.K_RIGHT]:
            self.x += 100

        if keys[pygame.K_UP]:
            self.y -= 100


        if keys[pygame.K_DOWN]:
            self.y += 100


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
    for x in range(65, 75, 1):
        top_row_letters = font.render(chr(x), True, grey)
        window.blit(top_row_letters, (counter, 0))
        counter += 100

    counter = 80
    for y in range(48, 58, 1):
        side_row_numbers = font.render(chr(y), True, grey)
        window.blit(side_row_numbers, (5, counter))
        counter += 100
    ## Loops to make square pieces
    for key in game_dictionary.keys():
        for count,index in enumerate(game_dictionary[key]):
            game_dictionary[key][count].rect = pygame.draw.rect(window, game_dictionary[key][count].color, [game_dictionary[key][count].x, game_dictionary[key][count].y , 100, 100])
    ## Loop to make the seperation between grid pieces
    for x in range(grid_width):
        pygame.draw.rect(window, black, (x * 100 + 50, 0, 2, win_height))
    for y in range(grid_length):
        pygame.draw.rect(window, black, (0, y * 100 + 50, win_height, 2))





game_dictionary = {"a": [game_grid(50,50),game_grid(50,150),game_grid(50,250),game_grid(50,350),game_grid(50,450),game_grid(50,550),game_grid(50,650),game_grid(50,750),game_grid(50,850),game_grid(50,950)],
                   "b": [game_grid(150,50),game_grid(150,150),game_grid(150,250),game_grid(150,350),game_grid(150,450),game_grid(150,550),game_grid(150,650),game_grid(150,750),game_grid(150,850),game_grid(150,950)],
                   "c": [game_grid(250,50),game_grid(250,150),game_grid(250,250),game_grid(250,350),game_grid(250,450),game_grid(250,550),game_grid(250,650),game_grid(250,750),game_grid(250,850),game_grid(250,950)],
                   "d": [game_grid(350,50),game_grid(350,150),game_grid(350,250),game_grid(350,350),game_grid(350,450),game_grid(350,550),game_grid(350,650),game_grid(350,750),game_grid(350,850),game_grid(350,950)],
                   "e": [game_grid(450,50),game_grid(450,150),game_grid(450,250),game_grid(450,350),game_grid(450,450),game_grid(450,550),game_grid(450,650),game_grid(450,750),game_grid(450,850),game_grid(450,950)],
                   "f": [game_grid(550,50),game_grid(550,150),game_grid(550,250),game_grid(550,350),game_grid(550,450),game_grid(550,550),game_grid(550,650),game_grid(550,750),game_grid(550,850),game_grid(550,950)],
                   "g": [game_grid(650,50),game_grid(650,150),game_grid(650,250),game_grid(650,350),game_grid(650,450),game_grid(650,550),game_grid(650,650),game_grid(650,750),game_grid(650,850),game_grid(650,950)],
                   "h": [game_grid(750,50),game_grid(750,150),game_grid(750,250),game_grid(750,350),game_grid(750,450),game_grid(750,550),game_grid(750,650),game_grid(750,750),game_grid(750,850),game_grid(750,950)],
                   "i": [game_grid(850,50),game_grid(850,150),game_grid(850,250),game_grid(850,350),game_grid(850,450),game_grid(850,550),game_grid(850,650),game_grid(850,750),game_grid(850,850),game_grid(850,950)],
                   "j": [game_grid(950,50),game_grid(950,150),game_grid(950,250),game_grid(950,350),game_grid(950,450),game_grid(950,550),game_grid(950,650),game_grid(950,750),game_grid(950,850),game_grid(950,950)]
}

def main():
    run = True
    Selection = True
    clock = pygame.time.Clock()
    build_game_grid()


    while Selection:
        clock.tick(30)
        print_game_grid()  ##Drawing inital grid
        for key in game_dictionary.keys():
            for count, index in enumerate(game_dictionary[key]):
                game_grid.changeColor(game_dictionary[key][count])


        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Selection = False
                run = False
                pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:

            if event.type == pygame.MOUSEBUTTONDOWN:
                if window.get_at(pygame.mouse.get_pos())== red:
                    Selection = False
                else:
                    Selection = True


    p = Player(playerX, playerY, 50, 50, grey)

    while run:
        clock.tick(30)
        print_game_grid() ##Drawing inital grid
        p.draw(window) ##Drawing player on grid
        p.move() ## Movement for player
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()




main()
