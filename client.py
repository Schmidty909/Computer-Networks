import socket
import pygame 

width = 500
height = 500

window = pygame.display.set_mode(width, height)
pygame.display.set_caption("Captain Admiral")

clientNumber = 0


class Submarine():
    def __init__ (self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.color = color
        self.rect(x, y, width, height)
        self.vel = 5
    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
    def move(self):
        keys = pygame.keys.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y += self.vel

        if keys[pygame.K_DOWN]:
            self.y -= self.vel

        self.rect = (self.x, self.y, self.width, self.height)

def redrawWindow(player, win):
    win.fill(255,255,255)
    player.draw(win)
    pygam.display.update()


def main():
    run = True
    p1 = Submarine(50, 50, 100, 100,(255,0,0))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p1.move
        redrawWindow(p1, win)
