import pygame

class Button:
    def __init__(self,x,y,h,w):
        self.rect = pygame.Rect(x,y,h,w)
    def draw(self, screen):
        pygame.draw.rect(screen, self.rect)