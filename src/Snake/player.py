
class Player:
    def __init__(self, points=0, size=1):
        self.points = points
        self.size = size
    def __str__(self):
        self.str =  "{self.points}, {self.size}"
        