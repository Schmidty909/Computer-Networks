class Game():
    def __init__(self):
        self.p1Turn = True
        self.p2Turn = False
        self.p1Coords = ""
        self.p2Coords = ""
        self.p1Hit = ""
        self.p2Hit = ""
        self.winner = ""

    def getp1Turn(self):
        print(self.p1Turn)
        return self.p1Turn

    def getp2Turn(self):
        return self.p2Turn

    def endTurn(self, player):
        if player == "0":
            self.p1Turn = False
            self.p2Turn = True
        if player == "1":
            self.p1Turn = True
            self.p2Turn = False

    def checkWin(self):
        if self.p1Hit == self.p2Coords:
            self.winner = "Player 1!"
        if self.p2Hit == self.p1Coords:
            self.winner = "Player 2!"
