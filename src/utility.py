import pygame
# Ping Pong
pygame.font.init()
PONGSCREEN = pygame.display.set_mode((900,600))
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)

# Simon Game
FONT = pygame.font.Font('freesansbold.ttf', 30)
WIDTH, HEIGHT = 600,600
SIMONSCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
OFFRED = (184,56,56)
ONRED = (255,56,56)
OFFBLUE = (38,116,174)
ONBLUE = (38,116,255)
OFFYELLOW = (204, 204, 0)
ONYELLOW = (240, 240, 0)
OFFGREEN = (0, 179, 0)
ONGREEN = (0, 230, 0)