class Game():
    def __init__(self):
        self.p1Turn = True
        self.p2Turn = False

    def getp1Turn(self):
        return self.p1Turn

    def getp2Turn(self):
        return self.p2Turn
