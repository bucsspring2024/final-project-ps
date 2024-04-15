import pygame
from src.optionprompt import Prompt
from src.bgfile import File_obj
from src.target import Target

class Controller:
    def __init__(self):
        pygame.key.set_repeat(50, 500)
        
        self.screen = pygame.display.set_mode()
        self.background = pygame.Surface(pygame.display.get_window_size())
        self.height, self.width = pygame.display.get_window_size() 
        self.background_color = (200, 200, 250)
        self.background.fill(self.background_color)
        self.prompt = Prompt(self.height/3, self.width/5, 50, 250)
        
        
    def mainloop(self):
        while(True):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.prompt.collidepoint == event.pos():
                        