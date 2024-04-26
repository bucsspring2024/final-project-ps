import pygame
from src.utility import *

class Ball:
    def __init__(self, x_pos, y_pos, radius, speed, color):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.radius = radius
        self.speed = speed
        self.color = color
        self.x_move = 1
        self.y_move = -1
        self.ball = pygame.draw.circle(PONGSCREEN, self.color, (self.x_pos, self.y_pos), self.radius)
        self.firstTime = 1
    def display(self):
        self.ball = pygame.draw.circle(PONGSCREEN, self.color, (self.x_pos, self.y_pos), self.radius)
    def update(self):
        self.x_pos += self.speed*self.x_move
        self.y_pos += self.speed*self.y_move
        if self.y_pos <= 0 or self.y_pos >= 900:
            self.y_move *= -1
        if self.x_pos <= 0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.x_pos >= 600 and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
    def reset(self):
        self.x_pos = 600//2
        self.y_pos = 900//2
        self.x_move *= -1
        self.firstTime = 1
    def hit(self):
        self.x_move *= -1
    def getRect(self):
        return self.ball