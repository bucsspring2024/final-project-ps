import pygame
from src.utility import *

class Button():
    def __init__(self,color,x,y,w=(WIDTH/13)*5,h=(HEIGHT/13)*5):
        self.rect = pygame.Rect(x,y,w,h)
        self.color = color
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
        Changes the color of the button to the lit up color.
        """
        for color in OFFCOLORS:
            if self.color == color:
                self.color = ONCOLORS[OFFCOLORS.index(color)]
    def light_off(self):
        """
        Changes the color of the button to the turned off color.
        """
        for color in ONCOLORS:
            if self.color == color:
                self.color = OFFCOLORS[ONCOLORS.index(color)]
            
        