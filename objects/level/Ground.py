import pygame
class Ground:
    def __init__(self,img):
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.top=0
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        self.mask = pygame.mask.from_surface(self.image)