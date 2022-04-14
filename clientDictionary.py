import socket
import pygame
import time
import random


pygame.init()

win_width = 1050
win_height = 1050

red = (255, 0, 0)
green = (0, 255, 0)
ocean_blue = (0, 130, 150)
grey = (128, 128, 128)
black = (0, 0, 0)

window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Captain Admiral")
DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


font = pygame.font.Font('cour.ttf', 40)

clientNumber = 0

grid_width = 10
grid_length = 10


class game_grid():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.color = red


game_dictionary = {"a": [game_grid(50,50),game_grid(153,50),game_grid(250,50),game_grid(350,50),game_grid(450,50),game_grid(550,50),game_grid(650,50),game_grid(750,50),game_grid(850,50),game_grid(950,50)],
                   "b": [game_grid(50,150),game_grid(150,150),game_grid(250,150),game_grid(350,150),game_grid(450,150),game_grid(550,150),game_grid(650,150),game_grid(750,150),game_grid(850,150),game_grid(950,150)],
                   "c": [game_grid(50,250),game_grid(150,250),game_grid(250,250),game_grid(350,250),game_grid(450,250),game_grid(550,250),game_grid(650,250),game_grid(750,250),game_grid(850,250),game_grid(950,250)]
}





def print_game_grid():
    for key in game_dictionary.keys():
        x = 0
        for index in game_dictionary[key]:
            pygame.draw.rect(window, game_dictionary[key][x].color, [game_dictionary[key][x].x, game_dictionary[key][x].y , 100, 100])
            x += 1


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        print_game_grid()
        pygame.display.update()



main()
