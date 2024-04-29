from src.utility import *

class SimonScore:
    def __init__(self, points=0):
        self.points = points
        self.text1 = "Total Points: "
        self.text2 = "Highscore: "
        self.file = open("src/highscore.txt", "w")
        self.file.write("0")
        self.file.close()
    def update(self):
        """
        Rewrites and Displays new score to the score counter on screen.
        """
        new_score = str(self.points)
        text = FONT.render(self.text1 + new_score, True, "white")
        SIMONSCREEN.fill(("black"), (WIDTH/13,10,250,25))
        SIMONSCREEN.blit(text, (WIDTH/13,10))
        
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
        new_high = f.read()
        text = FONT.render((self.text2 + new_high), True, "white")
        SIMONSCREEN.fill(("black"), (WIDTH/2 + WIDTH/13, 10, 250,25))
        SIMONSCREEN.blit(text, (WIDTH/2 + WIDTH/13,10))
        