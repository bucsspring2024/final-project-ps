import pygame, random
from src.utility import Utility
from pygame.math import Vector2

class Fruit:
    def __init__(self):
        self.y = random.randint(0, 19)
        self.x = random.randint(0, 19)
        self.pos = Vector2(self.x,self.y)
    def make_fruit(self):
        fruit_rect = pygame.Rect(int(self.pos.x *20),int(self.pos.y *20), 20,20)
        pygame.draw.rect(Utility.screen,(126,166,114),fruit_rect)
        