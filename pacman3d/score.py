class Score(object):
    def __init__(self):
        self.points = 0
        self.lives = 3


    def hit(self, amount):
        self.points += amount

    def kill(self):
        self.lives -= 1

    def __str__(self, *args, **kwargs):
        return str(self.points) + '    ' + str(self.lives)

