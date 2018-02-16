import pygame

import ResourceManager


class ForceIndicator():
    def __init__(self,rect):
        self.loadedImage = pygame.transform.scale(
            ResourceManager.ResourceManager.instResources()["power.png"],(rect[2], rect[3]))
        self.rect = rect
        self.coeff = 0
        self.enabled = True

    def render(self,screen):
        if not self.enabled: return None
        self.image = pygame.transform.scale(ResourceManager.ResourceManager.instResources()["rame.png"], (self.rect[2] + 4, self.rect[3] + 4))
        self.image.blit(self.loadedImage, (2, 2), pygame.Rect(0, 0,int(self.rect[2]*(self.coeff/100)),self.rect[3]))
        screen.blit(self.image,(self.rect[0]-4,self.rect[1]-4))