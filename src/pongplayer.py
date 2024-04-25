import pygame
from src.utility import *

class Player:
    def __init__(self,x,y,w,h,speed,color):
        self.x_pos = x
        self.y_pos = y
        self.width = w
        self.height = h
        self.speed = speed
        self.color = color
        self.pongRect = pygame.Rect(x,y,w,h)
        self.pong = pygame.draw.rect(PONGSCREEN,self.color, self.pongRect)
    def display(self):
        self.pong = pygame.draw.rect(PONGSCREEN, self.color, self.pongRect)
    def update(self, y_movement):
        self.y_pos = self.y_pos + self.speed*y_movement
        if self.y_pos <= 0:
            self.y_pos = 0
        elif self.y_pos + self.height >= 900:
            self.y_pos = 900 - self.height
        self.pongRect = (self.x_pos, self.y_pos, self.width, self.height)
    def displayScore(self, text, score, x, y, color):
        text = FONT.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x,y)
        PONGSCREEN.blit(text, textRect)
    def getRect(self):
        return self.pongRect