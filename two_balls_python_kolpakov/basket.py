from random import randrange

class Basket:
    def __init__(self):
        self.balls = []
        self.balls.append('white')

        if randrange(2):
            self.balls.append('white')
        else:
            self.balls.append('black')

    def getBall(self):
        if len(self.balls) == 1:
            return self.balls.pop()
        elif len(self.balls) == 2:
            return self.balls.pop(randrange(2))
        else:
            return False
