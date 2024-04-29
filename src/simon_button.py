import pygame
from src.utility import *

class Button():
    def __init__(self,color,x,y,w=(WIDTH/13)*5,h=(HEIGHT/13)*5):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
    def draw(self, screen=SIMONSCREEN):
        """
        Draws a Button object onto the pygame window.
        Args:
            screen (Surface):pygame Surface drawn onto. Defaults to SIMONSCREEN.
        """
        pygame.draw.rect(screen, self.color, self.rect)
    def collidepoint(self, pos):
        """
        Makes collidepoint accessible to Button objects.
        Args:
            pos (list): provides x,y coordinate for mouse click.

        Returns:
            self.rect returns pygame collidepoint for Button
        """
        return self.rect.collidepoint(pos)
    def light_up(self):
        """
        Lights up the Button object to a brighter color and turns it off after a delay.
        """
        for color in OFFCOLORS:
            if self.color == color:
                self.color = ONCOLORS[OFFCOLORS.index(color)]
    def light_off(self):
        for color in ONCOLORS:
            if self.color == color:
                self.color = OFFCOLORS[ONCOLORS.index(color)]
            
        