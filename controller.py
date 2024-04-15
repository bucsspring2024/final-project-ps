import pygame
from src.optionprompt import Prompt
from src.bgfile import File_obj
from src.target import Target

class Controller:
    def __init__(self):
        pygame.key.set_repeat(50, 500)
        
        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.background_color = (200, 200, 250)
        self.background.fill(self.background_color)
        
        
    def mainloop(self):
        while(True):
            