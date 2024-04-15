import random as r

class Target:
    def __init__(self, name, money, trustdif):
        names = []
        self.name = r.randrange(0, len(names))
        self.money = r.randrange(8000, 20000)
        self.trustdif = r.randrange(1,10)
    def __str__(self):
        return "{name} , {money} , {trustdif}"
        