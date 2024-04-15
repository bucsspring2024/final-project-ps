import random as r
from target import Target

class Prompt:
    def __init__(self,x,y,height,width):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.prompts = ["Sell some bank information.", 
                        "Get someone in a ponzi scheme.", 
                        "Get someone caught in a lottery scam.", 
                        "Make a fake charity.",
                        "Complete a phishing scam."
                        ]
        self.prompt = [r.randrange(0,len(self.prompts))]
        self.promptvalue = r.randrange(0,1000)
        self.prompttrust = r.randrange(0, 10) * Target.fbitrustdif
    def __str__(self):
        self.str =  "{self.x}, {self.y}, {self.height}, {self.width}, {self.prompt}, {self.promptvalue}, {self.prompttrust}"