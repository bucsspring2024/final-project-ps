import random as r
from target import Target

class Prompt:
    def __init__(self,x,y,height,width, prompt, promptvalue):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.prompts = []
        self.prompt = [r.randrange(0,len(self.prompts))]
        self.promptvalue = r.randrange(0,1000)
        self.prompttrust = r.randrange(0, 10) * Target.trustdif
    def __str__(self):
        return "{self.x} , {self.y} , {self.height} , {self.width} , {self.prompt} , {self.promptvalue} , {self.prompttrust}"