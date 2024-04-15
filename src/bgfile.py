import pygame

class File_obj(pygame.sprite.Sprite()):
    def __init__(self, x, y, img="file.png"):
         super().__init__()

         self.image = pygame.image.load(img)
         self.rect = self.image.get_rect()
         self.rect.x = x
         self.rect.y = y
    def __str__(self):
        self.str =  ""