import pygame
from src.pongplayer import Player
from src.utility import *
from src.pongball import Ball


class Controller:
    def __init__(self):
        #self.screen = pygame.display.set_mode((900,900))
        self.clock = pygame.time.Clock()
        
        
    def mainloop(self):
        #Controller.menuloop(self)
        #Controller.simongameloop(self)
        Controller.ponggameloop(self)
    
    def simongameloop(self):
        while(True):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        pass
                pygame.display.update()
                self.clock.tick(60)
                
    def ponggameloop(self):
        p1 = Player(20,0,10,100,10,GREEN)
        p2 = Player(570,0,10,100,10,GREEN)
        ball = Ball(600//2,900//2,7,7,WHITE)
        players = [p1,p2]
        p1Score, p2Score = 0,0
        p1_y_move, p2_y_move = 0,0
        while(True):
            PONGSCREEN.fill(BLACK)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        p2_y_move = -1
                    if event.key == pygame.K_DOWN:
                        p2_y_move = -1
                    if event.key == pygame.K_w:
                        p1_y_move = -1
                    if event.key == pygame.K_s:
                        p1_y_move = -1
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        p2_y_move = 0
                    if event.key == pygame.K_w or event.key == pygame.K_s:
                        p1_y_move = 0
            for player in players:
                if pygame.Rect.colliderect(ball.getRect(), player.getRect()):
                    ball.hit()
            p1.update(p1_y_move)
            p2.update(p2_y_move)
            point = ball.update()
            if point == -1:
                p1Score += 1
            elif point == 1:
                p2Score += 1
            if point:
                ball.reset()
            p1.display()
            p2.display()
            ball.display()
            p1.displayScore("Player 1 : ", p1Score, 100,20,WHITE)
            p2.displayScore("Player 2 : ", p2Score, 500,20,WHITE)
            pygame.display.update()
            self.clock.tick(30)
            
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