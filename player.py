import pygame
from client import ValidateMovementX
from client import ValidateMovementY


class Player():
    def __init__(self, x, y, key, keylocation, width, height, color):
        self.x = x
        self.y = y
        self.Key = key
        self.location = keylocation
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.hit = ""
        self.position = str(self.Key) + str(self.location)
        self.ourTurn = False

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            ValidateMovementX(self.x, self.Key, self.location, 0)

        if keys[pygame.K_RIGHT]:
            ValidateMovementX(self.x, self.Key, self.location, 1)

        if keys[pygame.K_UP]:
            ValidateMovementY(self.y, self.Key, self.location, 0)

        if keys[pygame.K_DOWN]:
            ValidateMovementY(self.y,self.Key, self.location, 1)

        self.rect = (self.x, self.y, self.width, self.height)
