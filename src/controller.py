import pygame, random, pygame_menu
from src.utility import *
from src.simon_button import Button
from src.simonscore import SimonScore


class Controller:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.difficulty = 550

        
        
    def mainloop(self):
        Controller.menuloop(self)
        Controller.simongameloop(self)        
        
    def simongameloop(self):
        """
        This loop runs the Simon game, creating instance variables, handling events, and updating the display.
        """
        SIMONSCREEN.fill("black")
        red_button = Button(OFFRED, WIDTH/13,HEIGHT/13,)
        blue_button = Button(OFFBLUE, (WIDTH/2 + (WIDTH/13)),HEIGHT/13)
        yellow_button = Button(OFFYELLOW, WIDTH/13,(HEIGHT/2 + HEIGHT/18))
        green_button = Button(OFFGREEN, (WIDTH/2 + WIDTH/13),(HEIGHT/2 + HEIGHT/18))
        buttons = [red_button,blue_button,yellow_button,green_button]
        for button in buttons:
            button.draw()
        player = SimonScore()
        player.update()
        player.updatehighscore()
        button_chain =[random.choice(buttons)]
        current_button_chain = button_chain
        new_sequence = True
        playing = True
        while(playing):
            if new_sequence:
                # Displays new sequence of buttons
                current_button_chain = button_chain[:]
                new_sequence = False
                pygame.time.wait(1000)
                sequencing = True
                while(sequencing):
                    for button in button_chain:
                        button.light_up()
                        button.draw()
                        pygame.display.flip()
                        pygame.time.wait(self.difficulty)
                        button.light_off()
                        button.draw()
                        pygame.display.flip()
                        pygame.time.wait(self.difficulty)
                        sequencing = True
                    sequencing = False
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Handle button clicks
                    for button in buttons:
                        if button.collidepoint(event.pos):
                            clicked_button = button
                            button.light_up()
                            button.draw()
                            pygame.display.flip()
                            pygame.time.wait(200)
                            button.light_off()
                            button.draw()
                            pygame.display.flip()
                            if clicked_button != current_button_chain[0]: 
                                playing = False
                                break
                            else:
                                current_button_chain.pop(0) 
                                if not current_button_chain:  
                                    button_chain.append(random.choice(buttons))
                                    player.points += 1
                                    player.update()
                                    player.updatehighscore()
                                    new_sequence = True
            pygame.display.update()
            self.clock.tick(60)
    def menuloop(self):
        """
        Menu loop loads the start menu of the game using the pygame-menu library. 
        A Play and Quit button are shown on it to start the game or exit the program. 
        A difficulty option is given to decide the speed the sequence plays out.
        """
        menu = pygame_menu.Menu('Simon Says', 600, 400,
        theme=pygame_menu.themes.THEME_GREEN)
        menu.add.button('Play', self.simongameloop)
        menu.add.selector('Difficulty :', [('Easy', 1), ('Medium', 2), ('Hard', 3)], onchange=self.set_difficulty)
        menu.add.button('Quit', pygame_menu.events.EXIT)
        menu.mainloop(SIMONSCREEN)
    def set_difficulty(self, value, *args):
        """
        Function to set the difficulty level based on the selected option.
        """
        if value == 1:
            self.difficulty = 550  # Easy
        elif value == 2:
            self.difficulty = 300  # Medium
        elif value == 3:
            self.difficulty = 50  # Hard
