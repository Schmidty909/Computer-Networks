import socket
import pygame 

width = 1000
height = 800

window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Captain Admiral")

clientNumber = 0


class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = width
        self.color = color
        self.rect = (x,y,width,height)
        self.vel = 5


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
    window.fill((255,255,255))
    p1.draw(window)
    pygame.display.update()


def main():
    run = True
    p = Player(450, 450, 100, 100, (255,0,0))
    clock = pygame.time.Clock()

    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        p.move()
        redrawWindow(p, window)


main()
