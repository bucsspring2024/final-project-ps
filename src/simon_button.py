import pygame
from src.utility import *

class Button(pygame.Surface):
    def __init__(self, color,x,y,h,w):
        self.button = pygame.draw.rect(SIMONSCREEN, color, (x,y,w,h))
    def light_up(self, button):
        if button.color == OFFRED:
            button.color = ONRED
            pygame.time.wait(750)
            pygame.display.flip()
            button.color == OFFRED
            pygame.display.flip()
        elif button.color == OFFBLUE:
            button.color = ONBLUE
            pygame.time.wait(750)
            pygame.display.flip()
            button.color == OFFBLUE
            pygame.display.flip()
        elif button.color == OFFYELLOW:
            button.color = ONYELLOW
            pygame.time.wait(750)
            pygame.display.flip()
            button.color == OFFYELLOW
            pygame.display.flip()
        elif button.color == OFFGREEN:
            button.color = ONGREEN
            pygame.time.wait(750)
            pygame.display.flip()
            button.color == OFFGREEN
            pygame.display.flip()