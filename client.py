import pygame.display
import pygame.mixer_music
from network import Network
from test import *


class game_grid():
    def __init__(self, x, y, key, location, initialcolor):
        self.x = x
        self.y = y
        self.key = key
        self.location = location
        self.color = initialcolor
        self.initalcolor = initialcolor
        self.rect = pygame.draw.rect(window, self.color, [self.x, self.y, 100, 100])
        self.island = False

    def hover(self):
        global p
        global Key
        global KeyPosition
        position = pygame.mouse.get_pos()
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if self.color != green:
                self.color = red
                Key = self.key
                KeyPosition = self.location
                p.x = self.x + 25
                p.y = self.y + 25
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


class Button():
    def __init__(self, x, y, width, height, text, color, background):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.initalcolor = grey
        self.background = background
        self.rect = (x, y, width, height)

    def draw(self):
        self.rect = pygame.draw.rect(window, self.color, [self.x - 50, self.y, 200, 50])

    def hover(self, color):
        position = pygame.mouse.get_pos()
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.color = color
            window.blit(start, startRect)
            window.blit(text, textRect)
            window.blit(Quit, QuitRect)
        else:
            self.color = self.initalcolor
            window.blit(start, startRect)
            window.blit(text, textRect)
            window.blit(Quit, QuitRect)


def draw_game_grid():

    global board
    # Loops to make Row and Column headers
    counter = 85
    top_character = 65
    for x in range(grid_width):
        top_row_letters = font.render(chr(top_character), True, white)
        window.blit(top_row_letters, (counter, 0))
        counter += 100
        top_character += 1

    counter = 80
    side_numbers = 48
    for y in range(grid_length ):
        side_row_numbers = font.render(chr(side_numbers), True, white)
        window.blit(side_row_numbers, (5, counter))
        counter += 100
        side_numbers += 1
    # Loops to make square pieces
    for key in board.keys():
        for count,index in enumerate(board[key]):
            board[key][count].rect = pygame.draw.rect(window, board[key][count].color, [board[key][count].x, board[key][count].y , 100, 100])
    # Loop to make the seperation between grid pieces
    for x in range(grid_width):
        pygame.draw.rect(window, black, (x * 100 + 50, 0, 2, win_height))
    for y in range(grid_length):
        pygame.draw.rect(window, black, (0, y * 100 + 50, win_height, 2))


def ValidateMovementX(x, key, keylocation, flag,board,p):
    # Moving player left
    if flag == 0:
        # Checking left boundary isn't crossed
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
               p.position = p.Key + str(p.location)

    # Moving player right
    else:
        # Checking right boundary isn't crossed
        for k in board.keys():
            for count, index in enumerate(board[k]):
                None

        if x + 100 > board[k][count].x +25:
            return 0
        else:
            if board[chr(ord(key) + 1)][keylocation].color == red or board[chr(ord(key) + 1)][keylocation].color == green:
                p.x = x
            else:
                p.x += 100
                move = False
                board[key][keylocation].color = red
                board[key][keylocation].initalcolor = red
                p.Key = chr(ord(key)+1)
                p.position = p.Key + str(p.location)


def ValidateMovementY(y, key, keylocation, flag,board,p):
    # Moving player up+

    if flag == 0:
        # Checking top boundary
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
                p.position = p.Key + str(p.location)


    # Moving player down
    else:
        # Checking bottom boundary
        for k in board.keys():
            for count, index in enumerate(board[k]):
                None
        if y + 100 > board[k][count].y +25:
            return 0
        else:
            if board[key][keylocation+1].color == red or board[key][keylocation+1].color == green:
                p.y = y
            else:
                p.y += 100
                move = False
                board[key][keylocation].color = red
                board[key][keylocation].initalcolor = red
                p.location = p.location + 1
                p.position = p.Key + str(p.location)


def main_menu():

    global win_width
    global win_height
    global start, startRect, text, textRect, Quit, QuitRect
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
    window.fill((0, 0, 0))
    for alpha in range(0, 300):
        window.set_alpha(alpha)
        window.blit(window, (0,0))
        pygame.display.update()
        pygame.time.delay(2)


def printStartingText():
    # Choose starting position text
    start_pos_text = font.render("Welcome Admiral!", True, white)
    window.blit(start_pos_text, (1100, 440))
    start_pos_text = font.render("Choose your starting", True, white)
    window.blit(start_pos_text, (1100, 480))
    start_pos_text = font.render("position.", True, white)
    window.blit(start_pos_text, (1100, 520))

# def initializePygame():

def main():

    # Initialize Pygame
    pygame.init()
    pygame.display.set_caption("Captain Admiral")

    global window
    window = pygame.display.set_mode((win_width, win_height))

    global board
    board = {"a": [game_grid(50,50,"a",0,ocean_blue),game_grid(50,150,"a",1,ocean_blue),game_grid(50,250,"a",2,ocean_blue),game_grid(50,350,"a",3,ocean_blue),game_grid(50,450,"a",4,ocean_blue),game_grid(50,550,"a",5,ocean_blue),game_grid(50,650,"a",6,ocean_blue),game_grid(50,750,"a",7,ocean_blue),game_grid(50,850,"a",8,ocean_blue),game_grid(50,950,"a",9,ocean_blue)],
             "b": [game_grid(150,50,"b",0,ocean_blue),game_grid(150,150,"b",1,ocean_blue),game_grid(150,250,"b",2,ocean_blue),game_grid(150,350,"b",3,ocean_blue),game_grid(150,450,"b",4,ocean_blue),game_grid(150,550,"b",5,ocean_blue),game_grid(150,650,"b",6,ocean_blue),game_grid(150,750,"b",7,ocean_blue),game_grid(150,850,"b",8,ocean_blue),game_grid(150,950,"b",9,ocean_blue)],
             "c": [game_grid(250,50,"c",0,ocean_blue),game_grid(250,150,"c",1,ocean_blue),game_grid(250,250,"c",2,ocean_blue),game_grid(250,350,"c",3,green),game_grid(250,450,"c",4,green),game_grid(250,550,"c",5,green),game_grid(250,650,"c",6,green),game_grid(250,750,"c",7,ocean_blue),game_grid(250,850,"c",8,ocean_blue),game_grid(250,950,"c",9,ocean_blue)],
             "d": [game_grid(350,50,"d",0,ocean_blue),game_grid(350,150,"d",1, green),game_grid(350,250,"d",2,ocean_blue),game_grid(350,350,"d",3,ocean_blue),game_grid(350,450,"d",4,ocean_blue),game_grid(350,550,"d",5,ocean_blue),game_grid(350,650,"d",6,green),game_grid(350,750,"d",7,ocean_blue),game_grid(350,850,"d",8,ocean_blue),game_grid(350,950,"d",9,ocean_blue)],
             "e": [game_grid(450,50,"e",0,ocean_blue),game_grid(450,150,"e",1,green),game_grid(450,250,"e",2,ocean_blue),game_grid(450,350,"e",3,ocean_blue),game_grid(450,450,"e",4,ocean_blue),game_grid(450,550,"e",5,ocean_blue),game_grid(450,650,"e",6,ocean_blue),game_grid(450,750,"e",7,ocean_blue),game_grid(450,850,"e",8,green),game_grid(450,950,"e",9,ocean_blue)],
             "f": [game_grid(550,50,"f",0,ocean_blue),game_grid(550,150,"f",1,ocean_blue),game_grid(550,250,"f",2,ocean_blue),game_grid(550,350,"f",3,ocean_blue),game_grid(550,450,"f",4,ocean_blue),game_grid(550,550,"f",5,ocean_blue),game_grid(550,650,"f",6,ocean_blue),game_grid(550,750,"f",7,ocean_blue),game_grid(550,850,"f",8,green),game_grid(550,950,"f",9,ocean_blue)],
             "g": [game_grid(650,50,"g",0,ocean_blue),game_grid(650,150,"g",1,ocean_blue),game_grid(650,250,"g",2,ocean_blue),game_grid(650,350,"g",3,green),game_grid(650,450,"g",4,green),game_grid(650,550,"g",5,green),game_grid(650,650,"g",6,ocean_blue),game_grid(650,750,"g",7,ocean_blue),game_grid(650,850,"g",8,green),game_grid(650,950,"g",9,ocean_blue)],
             "h": [game_grid(750,50,"h",0,ocean_blue),game_grid(750,150,"h",1,ocean_blue),game_grid(750,250,"h",2,ocean_blue),game_grid(750,350,"h",3,ocean_blue),game_grid(750,450,"h",4,green),game_grid(750,550,"h",5,ocean_blue),game_grid(750,650,"h",6,ocean_blue),game_grid(750,750,"h",7,green),game_grid(750,850,"h",8,green),game_grid(750,950,"h",9,ocean_blue)],
             "i": [game_grid(850,50,"i",0,ocean_blue),game_grid(850,150,"i",1,ocean_blue),game_grid(850,250,"i",2,ocean_blue),game_grid(850,350,"i",3,ocean_blue),game_grid(850,450,"i",4,ocean_blue),game_grid(850,550,"i",5,ocean_blue),game_grid(850,650,"i",6,ocean_blue),game_grid(850,750,"i",7,ocean_blue),game_grid(850,850,"i",8,ocean_blue),game_grid(850,950,"i",9,ocean_blue)],
             "j": [game_grid(950,50,"j",0,ocean_blue),game_grid(950,150,"j",1,ocean_blue),game_grid(950,250,"j",2,ocean_blue),game_grid(950,350,"j",3,ocean_blue),game_grid(950,450,"j",4,ocean_blue),game_grid(950,550,"j",5,ocean_blue),game_grid(950,650,"j",6,ocean_blue),game_grid(950,750,"j",7,ocean_blue),game_grid(950,850,"j",8,ocean_blue),game_grid(950,950,"j",9,ocean_blue)]
             }

    global font
    font = pygame.font.Font('cour.ttf', 40)

    n = Network()
    global p
    p = n.getP()

    global move
    move = True
    main = True
    run = True
    Selection = True
    clock = pygame.time.Clock()

    global StartButton
    global QuitButton

    # Create start menu button objects
    StartButton = Button(win_width / 2 - 75, 425, win_width, win_height, "Start", white, grey)
    QuitButton = Button(win_width / 2 - 75, 500, win_width, win_height, "Quit", white, grey)

    while main:

        clock.tick(60)

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

    # Loop to have player select there starting position
    while Selection:
        clock.tick(60)

        # Draw initial grid
        draw_game_grid()

        for key in board.keys():
            for count, index in enumerate(board[key]):
                game_grid.hover(board[key][count])

        # Update our window
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

    # Update our pygame screen
    window.fill(black)
    draw_game_grid()
    pygame.display.update()


    # Start game
    while run:
        clock.tick(30)
        draw_game_grid() # Drawing inital grid
        p.draw(window) # Drawing player on grid
        if move == True:
            p.move(board,p) # Movement for player
            # print(p.position)             # Debug player position
        else:
            for key in board.keys():
                for count, index in enumerate(board[key]):
                    game_grid.Fire(board[key][count])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if window.get_at(pygame.mouse.get_pos()) == red:
                    p.hit = FireKey + str(FireLocation)
                    # print(p.hit)          # Debug hit position
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

if __name__ == "__main__":
    main()

