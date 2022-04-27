import pygame
from client import ValidateMovementX
from client import ValidateMovementY

# updated code

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
        self.winner = False

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)

    def move(self, board, p, move):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            move = ValidateMovementX(self.x, self.Key, self.location, 0, board, p, move)
        if keys[pygame.K_RIGHT]:
            move = ValidateMovementX(self.x, self.Key, self.location, 1, board, p, move)
        if keys[pygame.K_UP]:
            move = ValidateMovementY(self.y, self.Key, self.location, 0, board, p, move)
        if keys[pygame.K_DOWN]:
            move = ValidateMovementY(self.y,self.Key, self.location, 1, board, p, move)

        self.rect = (self.x, self.y, self.width, self.height)
        return move
