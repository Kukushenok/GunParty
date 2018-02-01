import pygame
class SpriteRenderer:
    def __init__(self,path):
        self.load(path)
    def load(self,path):
        self.loaded_image = pygame.image.load(path).convert_alpha()
    def render(self,screen,x,y):
        screen.blit(self.loaded_image,(x,y),pygame.Rect(0,0,60,60))
