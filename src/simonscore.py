from src.utility import *
from pathlib import Path

class SimonScore:
    def __init__(self, points=0):
        self.points = points
        self.text1 = "Total Points: "
        self.text2 = "Highscore: "
        my_file = Path("src/highscore.txt")
        if my_file.is_file():
            f = open("src/highscore.txt", "r")
            highscore = f.read()
        else:
            highscore = "0"
        self.file = open("src/highscore.txt", "w")
        self.file.write(highscore)
        self.file.close()
        self.text = ""
    def update(self):
        """
        Rewrites and Displays new score to the score counter on screen.
        """
        self.new_score = str(self.points)
        # self.text = FONT.render(self.text1 + self.new_score, True, "white")
        
    def updatehighscore(self):
        """
        Writes new highscore to a file and retrieves it then updates highscore ccounter on screen.
        """
        f = open("src/highscore.txt", "r")
        highscore = f.read()
        f.close()
        if self.points > int(highscore):
            f = open("src/highscore.txt", "w")
            f.write(str(self.points))
            f.close()
        f = open("src/highscore.txt", "r")
        self.new_high = f.read()
        # self.text = FONT.render((self.text2 + self.new_high), True, "white")
        