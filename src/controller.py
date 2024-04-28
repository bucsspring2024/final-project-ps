import pygame
import random
from src.utility import *
from src.simon_button import Button
from src.simonscore import SimonScore


class Controller:
    def __init__(self):
        self.clock = pygame.time.Clock()
        
        
    def mainloop(self):
        #Controller.menuloop(self)
        Controller.simongameloop(self)
        #Controller.ponggameloop(self)
    
    def simongameloop(self):
        # red_button = pygame.draw.rect(SIMONSCREEN, OFFRED, Button(WIDTH/13,HEIGHT/13,(WIDTH/13)*5,(HEIGHT/13)*5))
        # blue_button = pygame.draw.rect(SIMONSCREEN, OFFBLUE, Button((WIDTH/2 + (WIDTH/13)),HEIGHT/13,(WIDTH/13)*5,(HEIGHT/13)*5))
        # yellow_button = pygame.draw.rect(SIMONSCREEN, OFFYELLOW, Button(WIDTH/15,(HEIGHT/2 + HEIGHT/18),(WIDTH/13)*5,(HEIGHT/13)*5))
        # green_button = pygame.draw.rect(SIMONSCREEN, OFFGREEN, Button((WIDTH/2 + WIDTH/13),(HEIGHT/2 + HEIGHT/18),(WIDTH/13)*5,(HEIGHT/13)*5))
        red_button = Button(OFFRED, WIDTH/13,HEIGHT/13,(WIDTH/13)*5,(HEIGHT/13)*5)
        blue_button = Button(OFFBLUE, (WIDTH/2 + (WIDTH/13)),HEIGHT/13,(WIDTH/13)*5,(HEIGHT/13)*5)
        yellow_button = Button(OFFYELLOW, WIDTH/15,(HEIGHT/2 + HEIGHT/18),(WIDTH/13)*5,(HEIGHT/13)*5)
        green_button = Button(OFFGREEN, (WIDTH/2 + WIDTH/13),(HEIGHT/2 + HEIGHT/18),(WIDTH/13)*5,(HEIGHT/13)*5)
        buttons = [red_button,blue_button,yellow_button,green_button]
        for button in buttons:
            button.draw()
        player = SimonScore()
        player.update()
        player.updatehighscore()
        buttonchain =[random.choice(buttons)]
        firstTime = True
        while(True):
            if firstTime:
                buttonchain.append(random.choice(buttons))
                firstTime = False
                for button in buttonchain:
                    button.light_up()
                    button.draw()
                    pygame.display.flip()
                    pygame.time.wait(750)
                    button.light_off()
                    button.draw()
                    pygame.display.flip()
                    pygame.time.wait(750)
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    for button in buttons:
                        if button.collidepoint(event.pos):
                            player.points += 1
                            player.update()
                            player.updatehighscore()
                            
            pygame.display.update()
            self.clock.tick(60)
            
    def menuloop(self):
        while(True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pass
                pygame.display.update()
                self.clock.tick(60)