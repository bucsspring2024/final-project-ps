import pygame

class Utility:
    def __init__(self):
        self.cell_size = 20
        self.cell_num = 40
        self.screen = pygame.display.set_mode((self.cell_num * self.cell_size, self.cell_num * self. cell_size))
    def __str__(self):
        return "{self.cell_size}, {self.cell_num}"