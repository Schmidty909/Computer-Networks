import socket
import pygame
import time
import random

## James is gay
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

game_grid = []


def build_game_grid(array):
    for x in range(grid_width):
        y_grid = []
        for y in range(grid_length):
            value = '0'
            if random.randrange(1, 11) == 10:
                value = '#'
            y_grid.append(value)
        array.append(y_grid)

    return array


def print_game_grid(array):
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

    for x in range(grid_width):
        for y in range(grid_length):
            if array[x][y] == '#':
                pygame.draw.rect(window, green, (x * 100 + 50, y * 100 + 50, 100, 100))
            else:
                pygame.draw.rect(window, ocean_blue, (x * 100 + 50, y * 100 + 50, 100, 100))
        print()

    for x in range(grid_width):
        pygame.draw.rect(window, black, (x * 100 + 50, 0, 2, win_height))
    for y in range(grid_length):
        pygame.draw.rect(window, black, (0, y * 100 + 50, win_height, 2))


class Board():
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color


class Player():
    def __init__(self, x, y, width, height, color):
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
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.rect = (self.x, self.y, self.width, self.height)


def redrawWindow(p1, window):
    print_game_grid(game_grid)
    p1.draw(window)
    pygame.display.update()


def main():
    run = True
    p = Player(450, 450, 50, 100, (128,128,128))
    clock = pygame.time.Clock()
    build_game_grid(game_grid)

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(p, window)


main()
